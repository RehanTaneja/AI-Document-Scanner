import easyocr

def extract_text(img):
    """Extract text from image using easyocr."""
    reader = easyocr.Reader(['en'])  # Specify the language (you can add more if needed)
    result = reader.readtext(img)
    
    # Extract the text from the result
    text = " ".join([item[1] for item in result])
    
    return text
