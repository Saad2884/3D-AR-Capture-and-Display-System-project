import cv2
import numpy as np
capL = cv2.VideoCapture('stereo.mp4')

while(True):
  ret, frame = capL.read()
  width=768*2
  height=768
  
  leftFrame=frame[1:height,1:int(width/2+1)]
  rightFrame=frame[1:height,int(width/2+1):width]

  #cv2.imshow("Dummy",rightFrame)
  a=cv2.resize(leftFrame, (768, 768))
  b=cv2.resize(rightFrame, (768, 768))

  if ret == True:
    
    cv2.imshow('Right', b)
    cv2.moveWindow('Right',1379+100,0)
    cv2.imshow('Left', a)
    cv2.moveWindow('Left',2404,150)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()