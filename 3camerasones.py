import cv2
cap1 = cv2.VideoCapture('0001-0200_L.mp4')
cap2 = cv2.VideoCapture('0001-0200_R.mp4')
cap3 = cv2.VideoCapture('0001-0200LEFT.mp4')
cap4 = cv2.VideoCapture('0001-0200RIGHT.mp4')
lap_w=1366;
lap_h=768
lcd_w=1024;
lcd_h=768;
while(True):
 
    ret, L = cap1.read()
    ret, R = cap2.read()
    ret, LEFT = cap3.read()
    ret, RIGHT = cap4.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    #gray2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)
    #gray3 = cv2.cvtColor(frame3, cv2.COLOR_RGB2GRAY)
    cv2.imshow('L-3D', L)
    cv2.moveWindow('L-3D',lap_w+int((lcd_w-lcd_h)/2),0)
    
    cv2.imshow('R-3D', R)
    cv2.moveWindow('R-3D',lap_w+lcd_w,int((lcd_w-lcd_h)/2)+15)
    
    cv2.imshow('LEFT', LEFT)
    cv2.moveWindow('LEFT',-lcd_w+int((lcd_w-lcd_h)/2),0)
    
    cv2.imshow('RIGHT', RIGHT)
    cv2.moveWindow('RIGHT',-2*lcd_w+int((lcd_w-lcd_h)/2),0)
    
    if cv2.waitKey(1) == ord('q'):
        break


cap1.release()
cap2.release()
cap3.release()
cap4.release()
cv2.destroyAllWindows()