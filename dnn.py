import cv2
import os
import numpy as np

FILEPATH = 'cropped/training/'
# save = 'cropped/training/'

face_cascade = cv2.CascadeClassifier(
    'E:/Python Install/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

PROTOTXT = 'E:/Biometrics/proto.txt'
MODEL = 'E:/Biometrics/res10_300x300_ssd_iter_140000.caffemodel'

crap = None
worst = 1.0

for image in os.listdir(FILEPATH):

    fst = image.split(".")[0]

    if fst.endswith('f'):

        img = cv2.imread(os.path.join(FILEPATH, image))

        # img = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        # img = cv2.resize(img, None, fx=0.25, fy=0.25,
        #                  interpolation=cv2.INTER_AREA)

        net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
        (h, w) = img.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(
            img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()

        for i in range(0, detections.shape[2]):

            confidence = detections[0, 0, i, 2]

            if confidence > 0.5:

                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                text = "{:.2f}%".format(confidence * 100)
                y = startY - 10 if startY - 10 > 10 else startY + 10

                img = cv2.bilateralFilter(img, 9, 15, 15)
                img = img[startY:endY, startX:endX]
                img = cv2.resize(img, None, fx=4, fy=4)

                cv2.rectangle(img, (0, 0), ((endX - startX)*4, (endY - startY)*4),
                              (0, 0, 255), 2)
                # cv2.putText(img, text, (20, 20),
                #             cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

                if confidence < worst:
                    crap = img.copy()
                    worst = confidence

        cv2.imshow("Output: Non Interpolated", img)
        cv2.waitKey(0)

cv2.imshow("Worst", crap)
cv2.waitKey(0)
