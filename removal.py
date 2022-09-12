import cv2
import numpy as np
video = cv2.VideoCapture("video2.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('record2.avi', fourcc, 20.0, (1280, 720))


def nothing():
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 300, 300)
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

while True:
    ret, frame = video.read()
    #frame = cv2.resize(frame, (1280, 720))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    #l_green = np.array([l_h, l_s, l_v])
    #u_green = np.array([u_h, u_s, u_v])
    l_green = np.array([44, 12, 27])
    u_green = np.array([91, 255, 255])
    mask = cv2.inRange(hsv, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    f = frame-res
    #cv2.imshow("frame", frame)
    #cv2.imshow("mask", mask)
    cv2.imshow("res", f)
    out.write(f)
    k = cv2.waitKey(50)
    if k == ord('q'):
        break
video.release()
out.release()
cv2.destroyAllWindows()