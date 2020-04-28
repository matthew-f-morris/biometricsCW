import cv2
import os
import numpy as np

FILEPATH = 'cropped/training/'

for image in os.listdir(FILEPATH):
    fst = image.split(".")[0]
    if fst.endswith('s'):
        # img = cv2.imread(os.path.join(FILEPATH, image), 0)
        # gabor = cv2.getGaborKernel(
        #     (21, 21), 8.0, np.pi/4, 10.0, 0.5, 0, ktype=cv2.CV_32F)

        # filtered = cv2.filter2D(img, cv2.CV_8UC3, gabor)

        filters = build_filters()

        cv2.imshow('img', img)
        cv2.imshow('filtered', filtered)
        cv2.waitKey(0)

def build_filters():

    filters = []
    ksize = 31
    for theta in np.arange(0, np.pi, np.pi / 32):
        params = {'ksize':(ksize, ksize), 'sigma':1.0, 'theta':theta, 'lambd':15.0,
                  'gamma':0.02, 'psi':0, 'ktype':cv2.CV_32F}
        kern = cv2.getGaborKernel(**params)
        kern /= 1.5*kern.sum()
        filters.append((kern,params))
    return filters