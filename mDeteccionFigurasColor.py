import cv2
import numpy as np

def figColor(imageHSV):
	blueBajo1 = np.array([100,100,20], np.uint8)
	blueAlto1 = np.array([125,255,255], np.uint8)
	#Valores de naranja parte baja
	orangeBajo1 = np.array([11,100,20], np.uint8)
	orangeAlto1 = np.array([19,255,255], np.uint8)
#valores de amarillo parte baja
	yellowBajo1 = np.array([15,100,100], np.uint8)
	yellowAlto1 = np.array([45,255,255], np.uint8)
	#Valores de verde parte baja
	greenBajo1 = np.array([36,100,20], np.uint8)
	greenAlto1 = np.array([70,255,255], np.uint8)
#valores de rojo parte baja
	redBajo1 = np.array([0,100,20], np.uint8)
	redAlto1 = np.array([10,255,255], np.uint8)

#Valores de rojo en parte alta
	redBajo2 = np.array([175,100,20], np.uint8)
	redAlto2 = np.array([180,255,255], np.uint8)

	#Valores de rosa parte alta
	pinkBajo1 = np.array([146,100,100], np.uint8)
	pinkAlto1 = np.array([170,255,255], np.uint8)

	#Buscar colores de la imagen de acuerdo a sus limites
	maskBlue = cv2.inRange(imageHSV, blueBajo1, blueAlto1)
	maskYellow = cv2.inRange(imageHSV, yellowBajo1, yellowAlto1)		maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
	maskRed1 = cv2.inRange(imageHSV, redAlto1, redAlto2)
	maskRed2 = cv2.inRange(imageHSV, redBajo2, redAlto2)
	maskRed = cv2.add(maskRed1, maskRed2)
	maskOrange = cv2.inRange(imageHSV, orangeAlto1, orangeBajo1)
	maskGreen = cv2.inRange(imageHSV, greenAlto1, greenBajo1)
	maskPink = cv2.inRange(imageHSV, pinkAlto1, pinkBajo1)
	#deteccion de colores en la imagen
	cntsRed, _ = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsBlue, _ = cv2.findContours(maskBlue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsYellow, _ = cv2.findContours(maskYellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsOrange, _ = cv2.findContours(maskOrange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsGreen, _ = cv2.findContours(maskGreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntsPink, _ = cv2.findContours(maskPink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#etiquetado de color
	color = 'x'
	if len(cntsRed)>0: color = 'Rojo'
	elif len(cntsOrange)>0: color = 'Naranja'
	elif len(cntsYellow)>0: color = 'Amarillo'
	elif len(cntsGreen)>0: color = 'Verde'
	elif len(cntsPink)>0: color = 'Rosa'
	elif len(cntsBlue)>0: color = 'Azul'

	return color