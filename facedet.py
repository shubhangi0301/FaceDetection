import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\Admin\OneDrive - vit.ac.in\Documents\VSCode\MISC\FaceDetection\index.xml')

if face_cascade.empty():
    print("Error: Failed to load cascade classifier.")
else:
    print("Cascade classifier loaded successfully.")

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 4), 10)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
