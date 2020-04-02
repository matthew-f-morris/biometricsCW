import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

filepath = 'images/training/'
save = 'cropped/training/'
# resize = 50

for image in os.listdir(filepath):
    img = cv2.imread(filepath + image)

    # width = int(img.shape[1] * resize / 100)
    # height = int(img.shape[0] * resize / 100)
    # dim = (width, height)
    # img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    crop = img[300:, 600:-550]
    h = crop.shape[0]
    w = crop.shape[1]

    cv2.imwrite(os.path.join(save, image), crop)
