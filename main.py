# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Import modules
from PIL import Image
import pytesseract

# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Create an image object of PIL library
image = Image.open('C:/Users/monis/OneDrive/Pictures/Saved Pictures/Tesser.jpg')

# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')

# Print the text
print(image_to_text)

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#   tesseract()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
