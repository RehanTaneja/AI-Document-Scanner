import streamlit as st
import cv2
import numpy as np
from scanner import scan_document
from ai_enhancements import extract_text

# Set the app title
st.title("AI-Powered Document Scanner")

# File uploader to upload images or take photos directly from webcam
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

# Option to use webcam to capture an image
use_webcam = st.checkbox("Use Webcam")

if uploaded_file is not None:
    img = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    st.image(img, caption="Uploaded Image", use_column_width=True)
elif use_webcam:
    st.write("Click to capture an image")
    img = scan_document()  # Capture image from webcam and process it
    st.image(img, caption="Scanned Image", use_column_width=True)

# If an image is processed, display the scanned document
if uploaded_file or use_webcam:
    processed_img = scan_document(img)
    st.image(processed_img, caption="Processed Document", use_column_width=True)

    # Enhance document using AI (OCR)
    text = extract_text(processed_img)
    st.subheader("Extracted Text")
    st.text_area("Text from Document", value=text, height=200)

# Instructions for the user
st.sidebar.info("""
    **How to Use:**
    1. Upload a document image or capture one using the webcam.
    2. The app will process and detect the document's edges.
    3. It will extract and display the text using AI enhancement (OCR).
""")
