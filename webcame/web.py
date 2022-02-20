import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
video = cv2.VideoCapture(0)

# Check if the webcam is opened correctly or not
if not video.isOpened():
    raise IOError("Cannot open webcam")

while True:
    check, frame = video.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5);
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3);
        #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    cv2.imshow('Face Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
    #if c == ord('q'):
        break

video.release()
cv2.destroyAllWindows()



