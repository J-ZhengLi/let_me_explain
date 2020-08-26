from face_detection import FaceDetection, MediaType

def main():
    fd = FaceDetection()
    fd.detect(MediaType.CAMERA)

if __name__ == "__main__":
    main()