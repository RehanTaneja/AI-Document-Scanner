# AI-Powered Document Scanner

## Overview
This is an AI-powered document scanner that allows users to scan documents using their webcam or upload an image. The app processes the document, extracts text using **Tesseract OCR**, and displays the extracted content.

## Features
- Upload an image or capture one using the webcam
- Automatically detects and processes the document
- Extracts text from the document using **Tesseract OCR**
- Displays the extracted text in the app

## Technologies Used
- **Streamlit** (for the web app)
- **OpenCV** (for document processing)
- **NumPy** (for image operations)
- **Tesseract OCR** (for text extraction)

## Installation & Usage
### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required packages:
```sh
pip install -r requirements.txt
```

### 2️⃣ Install Tesseract OCR
**Mac:** Install Tesseract using Homebrew:
```sh
brew install tesseract
```
**Windows:** Download and install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki).

### 3️⃣ Run the App Locally
```sh
streamlit run app.py
```

## Deployment on Streamlit Cloud
1. Push the project to a **public GitHub repository**.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and log in.
3. Click **New App**, select your repository, and set `app.py` as the main file.
4. Click **Deploy**.

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


