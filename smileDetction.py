# Smile detection
import cv2
from time import sleep

# face descriptor
fd = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
sd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')


vid = cv2.VideoCapture(0)

while True:
    flag, img = vid.read()
    if flag:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = fd.detectMultiScale(
            image=img_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(180, 180)
        )

        for x1, y1, w, h in faces:

            # shallow copy new array will be gernerated
            face = img_gray[y1:y1+h, x1:x1+w].copy()
            cv2.rectangle(image=img, pt1=(x1, y1), pt2=(x1+w, y1+h),
                         color=(0, 0, 255), #face color red
                         thickness=6)

            smiles = sd.detectMultiScale(
                image=face,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(50, 50))

            if len(smiles) == 1:
                xs, ys, ws, hs = smiles[0]
                cv2.rectangle(image=img, pt1=(x1+xs, y1+ys), pt2=(x1+xs+ws, y1+ys+hs),
                              color=(0, 255, 0), #smile color green
                              thickness=2)

        cv2.imshow('Preview', img)
        key = cv2.waitKey(1)
        if key == ord('x'):  # Press 'x' to exit
            break
    else:
        break
    sleep(0.1)
vid.release()
cv2.destroyAllWindows()