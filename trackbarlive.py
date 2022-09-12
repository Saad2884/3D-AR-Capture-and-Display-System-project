import cv2
import numpy as np

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

def bgremove(frame):
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
    return f

cap1 = cv2.VideoCapture(0)
cap1.set(4, 1280)
cap1.set(3, 720)
w = int(cap1.get(3))
h = int(cap1.get(4))


cap2 = cv2.VideoCapture(1)
cap2.set(4, 1280)
cap2.set(3, 720)
w2 = int(cap2.get(3))
h2 = int(cap2.get(4))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('recordingL.avi', fourcc, 20.0, (w, h))
out2 = cv2.VideoWriter('recordingR.avi', fourcc, 20.0, (w2, h2))

while(cap1.isOpened()):
    ret, L = cap1.read()
    ret1, R = cap2.read()
    
    if (ret == True and ret1==True):
        #out1.write(L)
        L=bgremove(L)
        R=bgremove(R)
        
        cv2.imshow('LEFT', L)
        cv2.imshow('RIGHT', R)

        if cv2.waitKey(20)=='27':
            break;
    else:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()