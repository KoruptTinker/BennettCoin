import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('recognizer/trainingdata.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
cam = cv2.VideoCapture(0)
#font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 4, 1, 3, 5 )
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255,0,255)
a=0
while True:
    ret, im =cam.read()
    if ret is True:
        gray=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,100),2)
            Id, conf =  recognizer.predict(gray[y:y+h,x:x+w])
            if(conf<=50):
                if(Id==1):
                    Id="Digvijay"
                    print(Id,'recognised')
                    
                    a=2
                    break
                elif(Id==2):
                    Id="Samarth"
                    print(Id,'recognised')
                    
                    a=2
                    break
                elif(Id==3):
                    Id="Brijesh"
                    print(Id, "recognised")
                    a=2
                    break
            else:
                Id="Unknown"
            
            cv2.putText(im,str(Id), (x,y+h),font,1,(0,255,255))
        cv2.imshow('im',im)
        cv2.waitKey(100);
    if(a==2):
        break
cam.release()
cv2.destroyAllWindows()
