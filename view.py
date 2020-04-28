import cv2
import os
import numpy as np

FILEPATH = 'cropped/training/'

for image in os.listdir(FILEPATH):
    fst = image.split(".")[0]
    if fst.endswith('s'):
        img = cv2.imread(os.path.join(FILEPATH, image))
        img2 = cv2.bilateralFilter(img, 9, 15, 15)

        cv2.imshow('img', img)
        cv2.imshow('img2', img2)
        cv2.waitKey(0)
