import cv2
import numpy as np

# Webcam dimensions
FRAME_WIDTH = 480
FRAME_HEIGHT = 640

def scan_document(img=None):
    """Captures an image from the webcam or processes the given image to detect and warp the document."""
    if img is None:
        cap = cv2.VideoCapture(0)
        cap.set(3, FRAME_WIDTH)
        cap.set(4, FRAME_HEIGHT)
        cap.set(10, 150)  # Set brightness
        
        success, img = cap.read()
        cap.release()  # Ensure webcam is released
        
        if not success:
            print("Error: Could not capture image from webcam.")
            return None

    img = cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT))
    processed_img = preprocess_image(img)
    biggest = get_contours(processed_img)
    
    if biggest.size == 0:
        print("Warning: No document detected. Returning original image.")
        return img  # Return original if no contours detected
    
    img_warp = warp_perspective(img, biggest)
    return img_warp

def preprocess_image(img):
    """Preprocess the image to enhance edges for contour detection."""
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)
    img_canny = cv2.Canny(img_blur, 200, 200)
    kernel = np.ones((5, 5))
    img_dilate = cv2.dilate(img_canny, kernel, iterations=2)
    img_erode = cv2.erode(img_dilate, kernel, iterations=1)
    return img_erode

def get_contours(img):
    """Finds the largest 4-sided contour (document)."""
    biggest = np.array([])
    max_area = 0
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if len(approx) == 4 and area > max_area:
                biggest = approx
                max_area = area
    
    return biggest

def warp_perspective(img, biggest):
    """Applies a perspective transformation to get a bird's-eye view of the document."""
    if biggest.shape[0] != 4:
        print("Error: Document edges not detected correctly.")
        return img

    biggest = np.array(biggest, dtype=np.float32).reshape((4, 2))
    pts1 = biggest
    pts2 = np.float32([[0, 0], [FRAME_WIDTH, 0], [0, FRAME_HEIGHT], [FRAME_WIDTH, FRAME_HEIGHT]])
    
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    img_output = cv2.warpPerspective(img, matrix, (FRAME_WIDTH, FRAME_HEIGHT))

    # Crop and resize for better visualization
    img_cropped = img_output[20:img_output.shape[0]-20, 20:img_output.shape[1]-20]
    img_cropped = cv2.resize(img_cropped, (FRAME_WIDTH, FRAME_HEIGHT))
    
    return img_cropped
