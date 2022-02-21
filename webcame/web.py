import cv2

def isOpened():
    image = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not image.isOpened():
        #raise IOError("Cannot open webcam")
        return False
    while True:
        ret, frame = image.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)

        c = cv2.waitKey(1)
        if c == 27:
            break
    return True
