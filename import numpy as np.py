import numpy as np

import cv2

img=cv2.imread('guapo.jpg',1)

cv2.imshow('RGB', img)

w, h ,c= img.shape

Y = np.zeros((w, h))

I = np.zeros((w, h))

Q = np.zeros((w, h))

for i in range(0, w):

	for j in range(0, h):

		R = img[i, j, 2]

		G = img[i, j, 1]

		B = img[i, j, 0]

# RGB -> YIQ

		Y[i,j] = int((0.299*R) + (0.587 * G) + (0.114 * B))

		I[i,j] = int((0.596 * R) - (0.274 * G) - (0.322 * B))

		Q[i,j] = int((0.211 * R) - (0.523 * G) + (0.312 * B))

yiq = cv2.merge((Y, I, Q))

img_out = yiq.astype(np.uint8)

cv2.imwrite("YIQ.jpg", img_out)

cv2.imshow('YIQ', img_out)

[Y,I,Q]=cv2.split(img)

cv2.imshow('Y', Y)

cv2.imshow('I', I)

cv2.imshow('Q', Q)

cv2.waitKey(0)

cv2.destroyAllWindows()