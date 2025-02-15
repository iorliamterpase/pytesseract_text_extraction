# 📝 Text Extraction Using Pytesseract 🚀

This project extracts text from images using **Tesseract OCR (Pytesseract)**, an open-source Optical Character Recognition (OCR) engine.

# Features
✅ **Extract Text from Images** (JPG, PNG, etc.)  
✅ **Supports Multiple Languages**  
✅ **Works with No Internet Connection**  
✅ **Preprocessing for Better OCR Accuracy**  

---
## 🛠 Installation

### 1️⃣ **Clone the Repository**
https://github.com/iorliamterpase/pytesseract_text_extraction.git
cd pytesseract_text_extraction

2️⃣ Install Tesseract OCR
Download and install pytessract 

Windows: Download and install  pytessract  from Tesseract OCR 

pip install Tesseract in your working environment

3️⃣ Set Up a Virtual Environment (Optional)

python -m venv venv

source venv/bin/activate  # For Mac/Linux


venv\Scripts\activate     # For Windows

4️⃣ Install Dependencies

pip install -r requirements.txt

Configuration(add prefix to the tesseract path)
Modify Tesseract path in Windows (if needed) inside text_extraction.py:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

 Usage
Run the OCR Script
bash
python text_extraction.py --image path/to/image.jpg

