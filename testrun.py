import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from PIL import Image
import sys

FILEPATH = 'testrun/'
GREEN_RANGE_MIN_HSV = (100, 80, 70)
GREEN_RANGE_MAX_HSV = (185, 255, 255)

# crop = img[300:, 600:-550]
# crop = img[320:, 700:-800]    for the side on pictures from the original images
# crop = img[:, 80:]            further cropping


def rgb_to_hsv(r, g, b):
    maxc = max(r, g, b)
    minc = min(r, g, b)
    v = maxc
    if minc == maxc:
        return 0.0, 0.0, v
    s = (maxc-minc) / maxc
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, s, v


for image in os.listdir(FILEPATH):

    img = cv2.imread(os.path.join(FILEPATH, image))
    print("Modifying: ", image)

    img = img[300:, 1030:-850]
    cv2.imshow('img', img)
    cv2.waitKey(0)

    img = img.convert('RGBA')

    pix = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b, a = pix[x, y]
            h_ratio, s_ratio, v_ratio = rgb_to_hsv(
                r / 255.0, g / 255.0, b / 255.0)
            h, s, v = (h_ratio * 360, s_ratio * 255, v_ratio * 255)

            min_h, min_s, min_v = GREEN_RANGE_MIN_HSV
            max_h, max_s, max_v = GREEN_RANGE_MAX_HSV
            if min_h <= h <= max_h and min_s <= s <= max_s and min_v <= v <= max_v:
                pix[x, y] = (0, 0, 0, 1)

    cv2.imshow('img', img)
    cv2.waitKey(0)

    img[img > 0] = 255

    cv2.imshow('img', img)
    cv2.waitKey(0)
