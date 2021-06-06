import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)
salida = cv2.VideoWriter('videoSalida.avi', cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

while (cap.isOpened()):
	ret, imagen = cap.read()
	if ret == True:
		cv2.imshow('video', imagen)
		salida.write(imagen)
		if cv2.waitKey(1) &0xFF == ord('s'):
			break
	else: break

cap = cv2.VideoCapture('C:\\Users\\Franco\\Pictures\\TMPI\\videoSalida.avi')

img_index = 0

while (cap.isOpened()):
	ret, frame = cap.read()

	if ret == False:
		break
	cv2.imwrite('mijeta'+ str(img_index)+ '.png', frame)
	img_index += 1

cap.release()
cv2.destroyAllWindows()
