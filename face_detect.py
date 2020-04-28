import cv2
import os
import numpy as np
from PIL import Image

FILEPATH = 'cropped/training/'
# save = 'cropped/training/'

face_cascade = cv2.CascadeClassifier(
    'E:/Python Install/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# img = cv2.imread(os.path.join(filepath, filename))
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# for image in os.listdir(filepath):
#     img = cv2.imread(os.path.join(filepath, image))
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = img[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray, minSize=(30, 30))
#         if len(eyes) == 0:
#             print("No face")
#         else:
#             print(1 < eyes.shape[0] < 3)
#             for (ex, ey, ew, eh) in eyes:
#                 cv2.rectangle(roi_color, (ex, ey),
#                               (ex+ew, ey+eh), (0, 255, 0), 2)

#     cv2.imshow('img', img)
#     cv2.waitKey()

for image in os.listdir(FILEPATH):

    fst = image.split(".")[0]
    if fst.endswith('f'):

        img = cv2.imread(os.path.join(FILEPATH, image))

        img = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        img = cv2.resize(img, None, fx=0.25, fy=0.25,
                         interpolation=cv2.INTER_AREA)
        net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
        # lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        # lab_planes = cv2.split(lab)
        # clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(6, 6))
        # lab_planes[0] = clahe.apply(lab_planes[0])
        # lab = cv2.merge(lab_planes)
        # img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            img, 1.05, 2, minSize=(95, 95), maxSize=(200, 200))

        # i = 0
        # index = 10000000

        # while i < len(faces):
        #     face = faces[i]
        #     print("Face: ", face)
        #     if(face[1] < index):
        #         index = i
        #     i = i + 1

        # if(index < 1000000):
        #     x, y, w, h = faces[index]
        #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #     roi_gray = gray[y:y+h, x:x+w]
        #     roi_color = img[y:y+h, x:x+w]

        #     cv2.imshow('img', img)
        #     cv2.waitKey()

        # else:
        #     print("No Face!")
        #     cv2.imshow('noface', img)
        #     cv2.waitKey()

        if(len(faces) != 0):
            b = (0, 0, 0, 0)
            wid = 0

            for(x, y, w, h) in faces:
                if(w > wid):
                    b = (x, y, x+w, y+h)
                    wid = w

            cv2.rectangle(img, (b[0], b[1]), (b[2], b[3]), (255, 0, 0), 2)
            roi_color = img[y:y+h, x:x+w]
            print("Face: ", (x, y, w, h), "     : ", image)

            cv2.imshow('img', img)
            cv2.waitKey()

        else:
            print("No Face!")
            cv2.imshow('noface', img)
            cv2.waitKey()
