import cv2
import numpy as np

# The following code is setting up the webcam

# Webcam dimensions
frameWidth = 480
frameHeight = 640

def scan_document(img=None):
    # Open webcam if no image is passed
    if img is None:
        cap = cv2.VideoCapture(0)
        cap.set(3, frameWidth)
        cap.set(4, frameHeight)
        cap.set(10, 150)  # Set the brightness
        success, img = cap.read()
        cap.release()  # Release webcam once we capture an image
    
    # Preprocess image for edge detection
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgThresh = prepProcessing(img)
    biggest = getContours(imgThresh)
    imgWarp = getWarp(img, biggest)
    
    return imgWarp

# Image preprocessing for edge detection
def prepProcessing(img):
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGrey, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgErode = cv2.erode(imgDial, kernel, iterations=1)
    return imgErode

# Extracting contours to identify the document edges
def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    return biggest

# Warp perspective to get a bird's-eye view of the document
def getWarp(img, biggest):
    if biggest is None or len(biggest) != 4:
        return img
    biggest = np.array(biggest, dtype=np.float32).reshape((4, 2))
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [frameWidth, 0], [0, frameHeight], [frameWidth, frameHeight]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (frameWidth, frameHeight))
    imgCropped = imgOutput[20:imgOutput.shape[0]-20, 20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped, (frameWidth, frameHeight))
    return imgCropped
