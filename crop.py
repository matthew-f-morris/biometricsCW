import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

FILEPATH = 'testrun/'
SAVE = 'testrun/'
# crop = img[300:, 600:-550]
# crop = img[320:, 700:-800]    for the side on pictures from the original images
# crop = img[:, 80:]            further cropping

for image in os.listdir(FILEPATH):
    # fst = image.split(".")[0]

    # if fst.endswith('o'):
    img = cv2.imread(os.path.join(FILEPATH, image))

    img = img[300:, 950:-850]
    cv2.imshow('canny edges', img)
    cv2.waitKey(0)

    # cv2.imwrite(os.path.join(SAVE, image), img)
