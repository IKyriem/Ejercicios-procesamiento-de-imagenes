import numpy as np
import cv2

cap = cv2.VideoCapture('C:\\Users\\Franco\\Pictures\\TMPI\\PP2\\videoPositivas.mp4')

img_index = 0

while (cap.isOpened()):
	ret, frame = cap.read()

	if ret == False:
		break
	cv2.imwrite('frames'+ str(img_index)+ '.png', frame)
	img_index += 1

cap.release()
cv2.destroyAllWindows()

