import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
	#captura de video cuadro a cuadro
	ret, frame = cap.read()
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	cv2.imshow('frame', rgb)
	b, g, r = cv2.split(rgb)
	cv2.imshow('B', b)
	cv2.imshow('G', g)
	cv2.imshow('R', r)
	if cv2.waitKey(1) &0xFF == ord ('q'):
		break
cap.release()
cv2.destroyAllWindows



