import pytesseract
import cv2

# Function to extract text using Tesseract OCR
def extract_text(img):
    # Ensure Tesseract is available in the system path or specify the path
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    
    # Convert image to grayscale for better OCR performance
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(imgGray)
    
    return text
