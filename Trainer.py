
import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create();
path='F:/CSE/User/'
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faceSamples=[]
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        faceNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces=detector.detectMultiScale(faceNp)
        #If a face is there then append that in the list as well as Id of it
        for (x,y,w,h) in faces:
            faceSamples.append(faceNp[y:y+h,x:x+w])
            Ids.append(Id)
            cv2.imshow("Training",faceNp)
            cv2.waitKey(10) 
    return faceSamples,Ids


faces,Ids = getImagesAndLabels(#insert image location here
    )
recognizer.train(faces, np.array(Ids))
recognizer.save('recognizer/trainingdata.yml')
cv2.destroyAllWindows()
