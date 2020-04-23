import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

FILEPATH = 'nogreen/devtest/'
SAVE = 'nogreen/devtest/'
# crop = img[300:, 600:-550]
# crop = img[320:, 700:-800]    for the side on pictures from the original images
# crop = img[:, 80:]            further cropping

for image in os.listdir(FILEPATH):
    fst = image.split(".")[0]

    if fst.endswith('e'):
        img = cv2.imread(os.path.join(FILEPATH, image))

        crop = img[300:, 1030:-850]
        cv2.imshow('canny edges', crop)
        cv2.waitKey(0)

        cv2.imwrite(os.path.join(SAVE, image), crop)
