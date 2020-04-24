import cv2
import os
import numpy as np

FILEPATH = 'testrun/'
SAVE = 'testrun/'

for image in os.listdir(FILEPATH):
    if image.split(".")[1].endswith('png') and image.split(".")[0].count('_') == 0:
        img = cv2.imread(os.path.join(FILEPATH, image), 0)
        mask = np.zeros(img.shape[:2], np.uint8)
        img[img > 0] = 255

        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.imwrite(os.path.join(
            SAVE, image.split('.')[0] + '_white.png'), img)
