# Code taken from https://stackoverflow.com
# /questions/48379205/how-to-manual-convert-bgr-image-to-grayscale-python-opencv
# The RBG to greyscale conversion done here is called luminosity conversion
# res - https://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/

import cv2
import numpy as np

# <-- absolute dir the script is in
file_path = "C:/Users/Anantha RamaKrishnan/PycharmProjects/" \
            "Principles of Digital Image Processing/resources/images/batman.jpg"

# Read as BGR
img = cv2.imread(file_path)

# img.shape gives [H, W, D] we here take height and width
H, W = img.shape[:2]

# Generate a 2-d array of the size of the image
gray = np.zeros((H, W), np.uint8)

# Here the 3-d array the RGB values are multiplied and summed (Averaged for greyscale) and the values are clipped
# between 0 - 255
for i in range(H):
    for j in range(W):
        gray[i, j] = np.clip(0.07 * img[i, j, 0] + 0.72 * img[i, j, 1] + 0.21 * img[i, j, 2], 0, 255)

# another simpler way of doing the above is to create a 3-d array full of weights, multiply and sum it with np.sum
# and cv2.convertScaleAbs
w = np.array([[[0.07, 0.72,  0.21]]])
gray2 = cv2.convertScaleAbs(np.sum(img*w, axis=2))

# (3) display
cv2.imshow("img", img)
cv2.imshow("gray", gray)
cv2.imshow("gray2", gray2)
cv2.waitKey()
