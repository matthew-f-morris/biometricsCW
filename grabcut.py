import numpy as np
import cv2
import os

FILEPATH = 'nogreen/training/'

newmask = cv2.imread('images/mask.png', 0)
mask = np.zeros(newmask.shape[:2], np.uint8)

mask[newmask == 0] = 0
mask[newmask == 255] = 1

for image in os.listdir(FILEPATH):

    img = cv2.imread(os.path.join(FILEPATH, image))

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    mask, bgdModel, fgdModel = cv2.grabCut(
        img, mask, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)

    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    cv2.imshow('canny edges', img)
    cv2.waitKey(0)
