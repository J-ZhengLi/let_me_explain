import cv2
from play_media import PlayMedia
#import time
from threading import Timer
from enum import Enum

class MediaType(Enum):
    STATIC_IMAGE = 0
    # ANIMATED_IMAGE = 1
    VIDEO = 2
    CAMERA = 3

class FaceDetection:
    faces = []
    def __init__(self, cascadeFp='openCV_data/haarcascade_frontalface_alt.xml', factor=1.2):
        self.cascadeFile = cascadeFp
        self.factor = factor

    def detect(self, mediaType):
        # WHY PYTHON DOESN'T HAVE A PROPER SWITCH STATEMENT!
        if mediaType == MediaType.STATIC_IMAGE:
            print('Unsupported yet')
        elif mediaType == MediaType.VIDEO:
            print('Unsupported yet')
        elif mediaType == MediaType.CAMERA:
            # capture video from web cam
            capture = cv2.VideoCapture(0)

            # check if theres a camera attached
            if capture != None and capture.isOpened():
                frame_skip = 0
                playing = False
                pm = PlayMedia()
                while(True):
                    # get image frame by frame
                    _, frame = capture.read()

                    # skip frames to optimize cpu usage
                    frame_skip = (frame_skip + 1) % 2

                    if frame_skip == 1:
                        # Begain face detection
                        cascade = cv2.CascadeClassifier(self.cascadeFile)
                        # convert this frame to grayscale to make detection easier
                        g_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        self.faces = cascade.detectMultiScale(g_frame, self.factor)
                        # End face detection

                    if len(self.faces) > 1:
                        if not playing:
                            pm.playVideoFromFile()
                            playing = True
                    else:
                        playing = False

                    # DEBUG only: Show captured video frame by frame
                    # mark detected faces on debug output
                    for (centerX, centerY, width, height) in self.faces:
                        cv2.circle(frame, (centerX + int(width/2), centerY + int(height/2)), width, (0, 0, 255))
                    cv2.imshow('Debuging, Press Q to quit', frame)
                    if cv2.waitKey(1) == ord('q'):
                        break

                capture.release()
                cv2.destroyAllWindows()
            else:
                print('Cannot find a working webcam')

    def test(self):
        print('hello')