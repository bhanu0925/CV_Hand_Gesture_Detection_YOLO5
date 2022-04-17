import os
import cv2
import time
import uuid

IMAGE_PATH='CollectedImages'

labels=['Peace','GoodJob','Dislike','OK','GoodLuck','CallMe','Victory']

number_of_images=30

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)
    cap=cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    #time.sleep(2)
    i=0
    while(True):
        #for imgnum in range(number_of_images):
        ret,frame=cap.read()
        imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)
        i=i+1
        print(i)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            i=0
            break
    cap.release()