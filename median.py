# import cv2
# import os
# import numpy as np

# FILEPATH = 'images/training/'
# # filename = '016z050pf.jpg'
# # save = 'cropped/training/'

# images = []
# for image in os.listdir(FILEPATH):
#     img = cv2.imread(os.path.join(FILEPATH, image))
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     images.append(gray)

# med = np.median(images, axis=(0))


# cv2.imshow('img', med)
# cv2.waitKey()


from PIL import Image
import glob
import numpy as np
import os

first = True
FILEPATH = 'images/training/'
length = 0

for img in os.listdir(FILEPATH):
    temp = np.asarray(Image.open(os.path.join(FILEPATH, img)))
    temp = temp.astype('uint32')
    if first:
        sumImage = temp
        first = False
    else:
        sumImage = sumImage + temp
        
    length = length + 1

avgArray = sumImage / length
avgImg = Image.fromarray(avgArray.astype('uint8'))
avgImg.show()
