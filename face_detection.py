import cv2
from enum import Enum

class MediaType(Enum):
    STATIC_IMAGE = 0
    # ANIMATED_IMAGE = 1
    VIDEO = 2
    CAMERA = 3

class FaceDetection:
    
    def __init__(self, cascadeFp='openCV_data/haarcascade_frontalface_default.xml', factor=1.2):
        self.cascadeFile = cascadeFp
        self.factor = factor

    def detect(self, mediaType):
        # WHY PYTHON DOESN'T HAVE A PROPER SWITCH STATEMENT!
        if mediaType == MediaType.STATIC_IMAGE:
            print('Unsupport yet')
        elif mediaType == MediaType.VIDEO:
            print('Unsupport yet')
        elif mediaType == MediaType.CAMERA:
            # capture video from web cam
            capture = cv2.VideoCapture(0)

            # check if theres a camera attached
            if capture != None and capture.isOpened():
                while(True):
                    # get image frame by frame
                    _, frame = capture.read()

                    print('before showing')

                    # DEBUG only: Show captured video frame by frame
                    cv2.imshow('Debug', frame)

                    if cv2.waitKey(1):
                        break

                capture.release()
                cv2.destroyAllWindows()
            else:
                print('Cannot find a working webcam')