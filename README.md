# AI-Powered Document Scanner

## Overview
This is an AI-powered document scanner that allows users to scan documents using their webcam or upload an image. The app processes the document, extracts text using **EasyOCR**, and displays the extracted content.

## Features
- Upload an image or capture one using the webcam
- Automatically detects and processes the document
- Extracts text from the document using **EasyOCR**
- Displays the extracted text in the app

## Technologies Used
- **Streamlit** (for the web app)
- **OpenCV** (for document processing)
- **NumPy** (for image operations)
- **EasyOCR** (for text extraction)

## Installation & Usage
### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required packages:
```sh
pip install -r requirements.txt
```

## Deployment on Streamlit Cloud
Published at https://ai-document-scanner-gekztbdaf9ma7kl7dovnde.streamlit.app/ 

## Folder Structure
```
📂 document-scanner
 ├── 📄 app.py              # Streamlit app
 ├── 📄 scanner.py          # Document scanning functions
 ├── 📄 ai_enhancements.py  # OCR processing
 ├── 📄 requirements.txt    # Required dependencies
 ├── 📄 README.md           # Project documentation
```

## Contributing
Feel free to open issues or submit pull requests!

## License
This project is open-source under the **MIT License**.

---

🚀 **Happy Scanning!**


