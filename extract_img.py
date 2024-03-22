from PIL import Image
from pytesseract import pytesseract

pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"


class ExtractImg:
    def __init__(self) -> None:
        pass

    def image_to_string(image: Image) -> str:
        text = pytesseract.image_to_string(image)
        return text[:-1]
