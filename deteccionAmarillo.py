import cv2
import numpy as np

captura = cv2.VideoCapture(0)
#determinar rango de color a detectar
#valores de amarillo parte baja
yellowBajo1 = np.array([20,50,50], np.uint8)
yellowAlto1 = np.array([40,255,255], np.uint8)

while(captura.isOpened()):
	ret, imagen = captura.read()
	if ret == True:
		frameHSV=cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
		maskYellow = cv2.inRange(frameHSV, yellowBajo1, yellowAlto1)
		maskYellowvis = cv2.bitwise_and(imagen, imagen, mask = maskYellow)
		cv2.imshow('maskYellowvis', maskYellowvis)
		cv2.imshow('maskYellow', maskYellow)
		cv2.imshow('video', imagen)
		if cv2.waitKey(1) &0xFF == ord('s'):
			break
	else: break
captura.release()
cv2.destroyAllWindows()