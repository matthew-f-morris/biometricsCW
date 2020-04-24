import cv2
import os
import numpy as np

FILEPATH = 'testrun/'

for image in os.listdir(FILEPATH):
    fst, snd = image.split(".")
    if fst.count('_') == 0 and snd.endswith('png'):

        img = cv2.imread(os.path.join(FILEPATH, image), 0)
        ret, threshold = cv2.threshold(img, 0, 255, 0)
        m = cv2.moments(threshold)

        x = int(m['m10'] / m['m00'])
        y = int(m['m01'] / m['m00'])

        cv2.circle(threshold, (x, y), 5, (127, 127, 127), -1)

        cv2.imshow('img', threshold)
        cv2.waitKey(0)
