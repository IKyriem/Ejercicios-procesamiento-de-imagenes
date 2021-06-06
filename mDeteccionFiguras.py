import cv2

image = cv2.imread('balon.jpg')
#Escala de grises
gray = cv2.cvtColor(image, cv2.cv2.COLOR_BGR2GRAY)
#Identificacion de bordes por binarización
#umbralización
#_,th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#canny
canny = cv2.Canny(gray,10,150)
#conjuncion de vertices
#dilatacion y erosion
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
#encontrar contornos
contornos, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contornos,-1,(0,255,0),3)
for c in contornos:
	epsilon = 0.01 * cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, epsilon, True)
	print (len(approx)) #Cantidad de lados
	#Etiquetar cada figura
	x,y,w,h = cv2.boundingRect(approx)
	if len(approx) == 3:
		cv2.putText(image, 'Triangulo', (x,y-5),1,1,(0,255,0),1)
	if len(approx) == 4:
		aspect_ratio = float(w)/h
		print (aspect_ratio)
		if aspect_ratio >=1:
			cv2.putText(image, 'Cuadrado', (x,y-5),1,1,(0,255,0),1)
	else:
		cv2.putText(image, 'Circulo', (x,y-5),1,1,(0,255,0),1)
	if len(approx) == 5:
		cv2.putText(image, 'Pentagono', (x,y-5),1,1,(0,255,0),1)
	if len(approx) == 6:
		cv2.putText(image, 'Hexagono', (x,y-5),1,1,(0,255,0),1)
	if len(approx)>10:
		cv2.putText(image, 'Circulo', (x,y-5),1,1,(0,255,0),1)
	cv2.drawContours(image,[approx], 0, (0,255,0),3)
	cv2.imshow('image', image)
	cv2.waitKey(0)


cv2.imshow('imagen', image)
#cv2.imshow('TH', th)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()