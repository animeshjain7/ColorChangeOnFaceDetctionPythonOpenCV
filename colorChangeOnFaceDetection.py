import cv2
import numpy as np
from time import sleep
import random
import math
    # color = (math.floor(random.random()*256),math.floor(random.random()*256),math.floor(random.random()*256))
    # download the 'haarcascade_frontalface_default.xml' file from here link->https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml\n",
    # face descriptor\n",
fd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') 
vid = cv2.VideoCapture(0)
while True:
    flag,img = vid.read()
    if flag:
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = fd.detectMultiScale(img_gray,1.1,5)
    
        for x1,y1,w,h in faces:
            cv2.rectangle(
                img ,
                pt1=(x1,y1) ,
                pt2=(x1+w,y1+h), 
                color=tuple(np.random.randint(size=3,low=0,high=255,dtype='int').tolist()), #method 1 to change color
     #method 2  #(math.floor(random.random()*256),math.floor(random.random()*256),math.floor(random.random()*256)),
                thickness=6 
                )
            
        cv2.imshow('Preview',img)
        key = cv2.waitKey(1) 
        if key == ord('x'):    #press x to exit(small x not shift+x)
            break
    else:
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows()"