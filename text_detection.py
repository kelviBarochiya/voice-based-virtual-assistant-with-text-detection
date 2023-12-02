import cv2
import easyocr
from tkinter import filedialog
import tkinter as tk

def choose_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

image_path = choose_file()

img = cv2.imread(image_path)

reader = easyocr.Reader(['en'], gpu=False)

text_ = reader.readtext(img)

for bbox, text, score in text_:
    if score > 0.25:
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 2)
        cv2.putText(img, text, (bbox[0][0], bbox[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        print(text)

cv2.imshow('Detected Text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
