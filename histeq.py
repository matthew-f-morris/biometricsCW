import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

FILEPATH = 'nogreen/devtest/'

for image in os.listdir(FILEPATH):
    if image.split(".")[0].endswith('e'):
        print("Modifying: ", image)
        img = cv2.imread(os.path.join(FILEPATH, image), 0)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        cl1 = clahe.apply(img)
        cv2.imwrite(os.path.join(FILEPATH, image + 'yeet.png'), cl1)
