import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

FILEPATH = 'testrun/'

for image in os.listdir(FILEPATH):
    if image.split(".")[1].endswith('png'):
        print("Modifying: ", image)
        img = cv2.imread(os.path.join(FILEPATH, image), 0)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        cl1 = clahe.apply(img)
        cv2.imwrite(os.path.join(
            FILEPATH, image.split('.')[0] + '_histeq.png'), cl1)
