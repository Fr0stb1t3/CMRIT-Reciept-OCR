import pytesseract
from pytesseract import Output
import cv2
import re
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # change path to where you have it
path = r'Tesser.jpeg' # image i took
img = cv2.imread(path)
receipt_ocr = {}

#Regex patterns
usnPattern = r'\d\w\w\d\d?\w\w\d\d\d'
studentNamePattern = r'Student Name \. (\.+)'
classPattern = r'Class :\.+'
recptPattern = r' Rept. No. : \d+'
partiPattern = r'(\d) (\w+) ' # incomplete regex for particulars, someone fix

#Commented Code here is to View Boxes for the given data
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# n_boxes = len(d['level'])
# for i in range(n_boxes):
#     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#     img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)
#cv2.destroyAllWindows()


#actual working part
extracted_text = pytesseract.image_to_string(img, lang = 'eng')
splits  = extracted_text.splitlines()
USN = re.search(usnPattern,extracted_text).group()
receipt_ocr['Adm No'] = USN
for i in splits:
    if re.search(studentNamePattern,i) != None :
        receipt_ocr['Student Name'] = re.search(studentNamePattern,i).group()
        break
# receipt_ocr['Class'] = re.search(classPattern,splits)
# receipt_ocr['Receipt No'] = re.search(recptPattern,splits)
print(receipt_ocr)