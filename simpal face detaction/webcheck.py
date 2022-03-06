import cv2


def check():
    image = cv2.VideoCapture(0)
    # Check if the webcam is opened correctly
    if not image.isOpened():
        # raise IOError("Cannot open webcam")
        return False

    return True
