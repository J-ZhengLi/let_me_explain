import cv2
from ffpyplayer.player import MediaPlayer

class PlayMedia:

    def playVideoFromFile(self, fileName='rick_trim.mp4'):
            # load video file
            video = cv2.VideoCapture(fileName)
            # load audio from the video file
            audio = MediaPlayer(fileName)

            while video.isOpened():
                ret, frame = video.read()
                audio.get_frame()
                # If still have frame to retrive
                if ret:
                    # show output in fullscreen
                    cv2.namedWindow('output', cv2.WND_PROP_FULLSCREEN)
                    cv2.setWindowProperty('output', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('output', frame)

                    if cv2.waitKey(38) == ord('q'):
                        break
                else:
                    break

            video.release()
            cv2.destroyAllWindows()