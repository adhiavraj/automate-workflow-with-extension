import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'(DriveNameLetter):\\Tesseract-OCR\\tesseract.exe'

downloads_folder = os.path.expanduser(r'(DriveNameLetter):\\Users\\(your_user_name)\Downloads')
screenshot_path = os.path.join(downloads_folder, 'screenshot.jpeg')

image_path = screenshot_path

image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

custom_config = r'--oem 3 --psm 6'
extracted_text = pytesseract.image_to_string(gray_image, config=custom_config)

print(extracted_text)