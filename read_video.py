import cv2 as cv

video = cv.VideoCapture('videos/carros1.mp4')

while True:

    leu_certo, frame = video.read()

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):

        break

video.release()

cv.destroyAllWindows()
