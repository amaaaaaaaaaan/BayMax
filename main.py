import cv2

cap=cv2.VideoCapture(0)

cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    face= cascade.detectMultiScale(frame,1.1)
    for x,y,w,h in face:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255),1)
        cv2.circle(frame,(x+w//2,y+h//2),1,(255,0,0),3)
        print(x,y)
    cv2.imshow('aaaaa',frame)
    
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break