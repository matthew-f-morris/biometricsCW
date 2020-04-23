import cv2
import os
import numpy as np

FILEPATH = 'nogreen/training/'

for image in os.listdir(FILEPATH):
    fst = image.split(".")[0]
    if fst.endswith('s'):
        img = cv2.imread(os.path.join(FILEPATH, image))
        cv2.imshow('img', img)
        cv2.waitKey(0)
