from PIL import Image
from pytesseract import pytesseract
import enum
import os



os.environ['TESSDATA_PREFIX'] = r"C:\Program Files (x86)\Tesseract-OCR\tessdata"


class OSType(enum.Enum): 
    MAC = 0
    WINDOWS = 1

class Language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'

class ImageReader:

    def __init__(self, os_type: OSType):
        if os_type == OSType.MAC:
            print('Running on mac\n')

        if os_type == OSType.WINDOWS:
            windows_path = r'C:\Users\HP\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'  # Correct path
            pytesseract.tesseract_cmd = windows_path
            print('Running on Windows\n')

    def extract_text(self, image: str, lang: str) -> str:
        if not os.path.exists(image):
            raise FileNotFoundError(f"Error: File not found at {image}")

        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang)  # Correct parameter
        return extracted_text


if __name__ == '__main__':
    ir = ImageReader(OSType.WINDOWS)  # Use renamed OSType
    try:
        text = ir.extract_text(r'C:\Users\HP\OneDrive\Desktop\My_Projects\text_extractor\text4.png', lang='eng')
        processed_text=' '.join(text.split())
        print(processed_text)  # Print the extracted text
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")
