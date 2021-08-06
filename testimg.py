import cv2
import pytesseract

pytesseract.pytesseract.pytesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img=cv2.imread('./assets/images/CG-RECTO.PNG')
img=cv2.cvtColor(img,cv2.COLOR_BGR5552RGB)
cv2.imshow('Result',img)

cv2.waitKey(0)