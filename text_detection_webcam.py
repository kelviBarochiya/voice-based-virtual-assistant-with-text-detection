import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    custom_config = r'--oem 3 --psm 6 outputbase digits'
    text = pytesseract.image_to_string(thresh, config=custom_config)

    if text.isdigit():
        print(f"Detected Number: {text}")

        cv2.putText(frame, f"Detected Number: {text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        break

    cv2.putText(frame, f"Detected Text/Number: {text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Text/Number Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()























# import cv2
# from PIL import Image
# from pytesseract import pytesseract

# camera = cv2.VideoCapture(0)

# while True:
#     _,image=camera.read()
#     cv2.imshow("image",image)
#     if cv2.waitKey(1)& 0xFF==ord('s'):
#         cv2.imwrite("test1.png ",image)
#         break
# camera.release()
# cv2.destroyAllWindows()

# def tesseract():
#     path_to_tesseract=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     image_path="test1.png"
#     pytesseract.tesseract_cmd=path_to_tesseract
#     text=pytesseract.image_to_string(Image.open(image_path))
#     print(text)
# tesseract()
