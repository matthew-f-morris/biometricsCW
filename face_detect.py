import cv2
import os
import numpy as np

filepath = 'nogreen/training/'
filename = '016z050pf.jpg'
save = 'cropped/training/'

face_cascade = cv2.CascadeClassifier(
    'E:/Python Install/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    'E:/Python Install/Lib/site-packages/cv2/data/haarcascade_eye.xml')

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

for image in os.listdir(filepath):
    img = cv2.imread(os.path.join(filepath, image))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    i = 0
    index = 10000000
    while i < len(faces):
        face = faces[i]
        print("Face: ", face)
        if(face[1] < index):
            index = i
        i = i + 1

    if(index < 1000000):
        x, y, w, h = faces[index]
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        cv2.imshow('img', img)
        cv2.waitKey()

    else:
        print("No Face!")
