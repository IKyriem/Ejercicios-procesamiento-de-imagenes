
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') #Metodos para reconocer un rostro y ojos.

img = cv2.imread('guapo.jpg') #Leemos una imagen que esté ubicada en la carpeta donde se guarde el programa.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Se convierte en gris

faces = face_cascade.detectMultiScale(gray, 1.3,5) #detecta el objeto dentro de la imagen con los parámetros dados
for (x,y,w,h) in faces:
	img = cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0), 2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	eyes = eye_cascade.detectMultiScale(roi_gray)
	for(ex, ey, ew, eh) in eyes:
		cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

cv2.imshow('imagen', img) #Mostramos la imagen 
cv2.waitKey(0)
cv2.destroyAllWindows()