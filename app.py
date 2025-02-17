import streamlit as st
import cv2
import numpy as np
from scanner import scan_document
from ai_enhancements import extract_text

# Set the app title
st.title("AI-Powered Document Scanner")

# File uploader to upload images
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    if img is None:
        st.error("Error loading image. Please try again with a valid image file.")
    else:
        st.image(img, caption="Uploaded Image", use_column_width=True)
        
        # Process the scanned document
        processed_img = scan_document(img)
        if processed_img is not None:
            st.image(processed_img, caption="Processed Document", use_column_width=True)
            
            # Enhance document using AI (OCR)
            text = extract_text(processed_img)
            st.subheader("Extracted Text")
            st.text_area("Text from Document", value=text, height=200)
        else:
            st.error("Error processing document. Ensure the image is clear and well-lit.")
else:
    st.info("Please upload an image to begin document scanning.")

# Instructions for the user
st.sidebar.info(
    """
    **How to Use:**
    1. Upload a document image.
    2. The app will process and detect the document's edges.
    3. It will extract and display the text using AI enhancement (OCR).
    """
)
