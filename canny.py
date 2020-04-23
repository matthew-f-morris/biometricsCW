import cv2
import os
import numpy as np

FILEPATH = 'nogreen/training/'
MIN = 100
MAX = 10

for image in os.listdir(FILEPATH):
    if image.split(".")[0].endswith('s'):

        img = cv2.imread(os.path.join(FILEPATH, image), 0)

        # 30, 220
        edges = cv2.Canny(img, 50, 150, apertureSize=3)

        cv2.imshow('canny edges', img)
        cv2.waitKey(0)
