import cv2

capture = cv2.VideoCapture('webCam.avi')

while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        cv2.imshow("gato0", frame)
        if (cv2.waitKey(30) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
