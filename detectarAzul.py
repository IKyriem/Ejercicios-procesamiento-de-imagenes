import cv2
import numpy as np

captura = cv2.VideoCapture(0)
#determinar rango de color a detectar
#valores de azul parte baja
blueBajo1 = np.array([100,100,20], np.uint8)
blueAlto1 = np.array([125,255,255], np.uint8)

while(captura.isOpened()):
	ret, imagen = captura.read()
	if ret == True:
		frameHSV=cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
		maskBlue = cv2.inRange(frameHSV, blueBajo1, blueAlto1)
		contornos, _ = cv2.findContours(maskBlue,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		#cv2.drawContours(imagen, contornos, -1, (255, 0, 0), 3)
		for c in contornos:
			area = cv2.contourArea(c)
			if area > 300:
				M= cv2.moments(c)
				if(M["m10"]==0): M["m00"]=1
				x=int (M["m10"]/M["m00"])
				y=int (M["m01"]/M["m00"])
				cv2.circle(imagen,(x,y),7,(0,255,0), -1)
				fort = cv2.FONT_HERSHEY_SIMPLEX
				cv2.putText(imagen,'{},{}'.format(x,y),(x+10,y), fort, 0.75, (0,255,0),1,cv2.LINE_AA)
				nuevoContorno = cv2.convexHull(c)
				cv2.drawContours(imagen,[nuevoContorno], 0, (255, 0, 0), 3)

		#maskBluevis = cv2.bitwise_and(imagen, imagen, mask = maskBlue)
		#cv2.imshow('maskBluevis', maskBluevis)
		#cv2.imshow('maskBlue', maskBlue)
		cv2.imshow('video', imagen)
		if cv2.waitKey(1) &0xFF == ord('s'):
			break
	else: break
captura.release()
cv2.destroyAllWindows()