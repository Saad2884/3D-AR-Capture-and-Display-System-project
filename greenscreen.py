import cv2
cap1 = cv2.VideoCapture('green.webm')
while(True):
    ret, L = cap1.read()
    cv2.imshow('video',L)
    if cv2.waitKey(1) == ord('q'):
        break
cap1.release()
cv2.destroyAllWindows()