import cv2
import numpy as np

captura = cv2.VideoCapture(0)
#determinar rango de color a detectar
#valores de rojo parte baja
redBajo1 = np.array([0,100,20], np.uint8)
redAlto1 = np.array([0,255,255], np.uint8)

#Valores de rojo en parte alta
redBajo2 = np.array([175,100,20], np.uint8)
redAlto2 = np.array([179,255,255], np.uint8)

while(captura.isOpened()):
	ret, imagen = captura.read()
	if ret == True:
		frameHSV=cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
		maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
		maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
		maskRed = cv2.add(maskRed1, maskRed2)
		maskRedvis = cv2.bitwise_and(imagen, imagen, mask = maskRed)
		#Muestra máscaras
		cv2.imshow('maskRedvis', maskRedvis)
		cv2.imshow('maskRed', maskRed)
		cv2.imshow('video', imagen)
#Función para salir del programa
		if cv2.waitKey(1) &0xFF == ord('s'):
			break
	else: break
captura.release()
cv2.destroyAllWindows()


