import cv2
import numpy as np

img = cv2.imread('guapo.jpg')
original = img.copy()
img = np.array(img, dtype=np.float64) # converting to float to prevent loss
img = cv2.transform(img, np.matrix([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
img[np.where(img > 255)] = 255 # normalizing values greater than 255 to 255
img = np.array(img, dtype=np.uint8) # converting back to int
cv2.imshow("original", original)
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()