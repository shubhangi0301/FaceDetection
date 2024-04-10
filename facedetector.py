import cv2

face_cascade = cv2.CascadeClassifier('index.xml')

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
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 150, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xFF
    if k == ord('r'):
        break
cap.release()
cv2.destroyAllWindows()
