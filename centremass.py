import cv2
import os
import numpy as np

FILEPATH = 'nogreen/devtest/'

for image in os.listdir(FILEPATH):
    # fst = image.split(".")[0]
    # if fst.endswith('s'):

    img = cv2.imread(os.path.join(FILEPATH, image), 0)
    ret, threshold = cv2.threshold(img, 127, 255, 0)
    m = cv2.moments(threshold)

    x = int(m['m10'] / m['m00'])
    y = int(m['m01'] / m['m00'])

    cv2.circle(img, (x, y), 5, (255, 255, 255), -1)

    cv2.imshow(image, img)
    cv2.waitKey(0)
