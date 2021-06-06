import numpy as np
import matplotlib.pyplot as pyplot
import cv2

#Carga de imagen a color
img = cv2.imread('2C1.jpg', 1)
[B, G, R] = cv2.split(img)
cv2.imshow ('imageR', R)
cv2.imshow ('imageG', G)
cv2.imshow ('imageB',B)

cv2.waitKey(0)
cv2.destroyAllWindows()
