import cv2
import numpy as np

def dibujar(mask,color):
	contornos, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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

captura = cv2.VideoCapture(0)
#valores de azul parte baja
blueBajo1 = np.array([100,100,20], np.uint8)
blueAlto1 = np.array([125,255,255], np.uint8)
#valores de amarillo parte baja
yellowBajo1 = np.array([20,50,50], np.uint8)
yellowAlto1 = np.array([40,255,255], np.uint8)
#valores de rojo parte baja
redBajo1 = np.array([0,100,20], np.uint8)
redAlto1 = np.array([0,255,255], np.uint8)

#Valores de rojo en parte alta
redBajo2 = np.array([175,100,20], np.uint8)
redAlto2 = np.array([179,255,255], np.uint8)

fort = cv2.FONT_HERSHEY_SIMPLEX

while(captura.isOpened()):
	ret, imagen = captura.read()
	if ret == True:
		frameHSV=cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
		maskBlue = cv2.inRange(frameHSV, blueBajo1, blueAlto1)
		maskYellow = cv2.inRange(frameHSV, yellowBajo1, yellowAlto1)
		maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
		maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
		maskRed = cv2.add(maskRed1, maskRed2)
		dibujar(maskBlue,(255,0,0))
		dibujar(maskYellow,(0,255,255))
		dibujar(maskRed,(0,0,255))
		cv2.imshow('video', imagen)
		if cv2.waitKey(1) &0xFF == ord('s'):
			break
	else: break
captura.release()
cv2.destroyAllWindows()