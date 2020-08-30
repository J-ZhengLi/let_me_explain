import cv2
import platform
from random import choice
from os import walk, system
from os.path import join
from ffpyplayer.player import MediaPlayer

class PlayMedia:

    def __init__(self, volume=None):
        if volume != None:
            print('change volume')
            # change system volume just for fun
            if platform.system() == 'Linux':
                print('isLinux')
                system('amixer set Master unmute')
                system('amixer set Master ' + str(volume) + '%')
    
    def playRandomVideoFromFolder(self, folderPath='data'):
        fn_list = []
        print(platform.system())

        # get a list of filenames from the folder
        (_, _, filenames) = next(walk(folderPath))
        for f in filenames:
            # get the path of each file
            fn_list.append(join(folderPath, f))
        
        # Choose a random file to play
        self.playVideoFromFile(choice(fn_list), False)

    def playVideoFromFile(self, fileName='data/rick', fullscreen=False):
            # load video file
            video = cv2.VideoCapture(fileName)
            # calculate delay base on the video's frame rate
            fps = video.get(cv2.CAP_PROP_FPS)
            delay = int(1000 / (fps + 1))
            # load audio from the video file
            audio = MediaPlayer(fileName)

            while video.isOpened():
                ret, frame = video.read()
                # Play sound
                audio.get_frame()
                # If still have frame to retrive
                if ret:
                    if fullscreen:
                        cv2.namedWindow('output', cv2.WND_PROP_FULLSCREEN)
                        cv2.setWindowProperty('output', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('output', frame)

                    if cv2.waitKey(delay) == ord('q'):
                        break
                else:
                    break

            video.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    pm = PlayMedia()
    pm.playRandomVideoFromFolder()