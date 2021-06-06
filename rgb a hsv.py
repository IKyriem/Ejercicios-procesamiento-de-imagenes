import cv2
import numpy as np
import math
#Lectura de imagen
img=cv2.imread('Chalino2pac.jpg',1)
#Mostrar la imagen en RGB
cv2.imshow('RGB', img)
#Asignación del formato HSV
h, s ,v= img.shape

H = np.zeros((h, s))

S = np.zeros((h, s))

V = np.zeros((h, s))

#Transformación de imagen
for i in range(0, h):

	for j in range(0, s):

		R = img[i, j, 2]

		G = img[i, j, 1]

		B = img[i, j, 0]

# RGB -> HSV

		H[i,j] = math.acos((1/2)*((R-G)+(R-B))/(math.pow(R-G,2)+(R-B)*math.sqrt(G-B)))

		rr = np.min(R)

		gg = np.min(G)

		bb = np.min(B)

		x=(rr,gg,bb)
		S[i,j] = (1-(3/(R+G+B))*np.min(x)) #*min(R,G,B)

		V[i,j] = (1/3*(R+G+B))

#Juntar datos guardados
hsv = cv2.merge((H, S, V))

img_out = hsv.astype(np.uint8)
#Mostrar resultados
cv2.imwrite("HSV.jpg", img_out)

cv2.imshow('HSV', img_out)

[H,S,V]=cv2.split(img)

cv2.imshow('H', H)

cv2.imshow('S', S)

cv2.imshow('V', V)

cv2.waitKey(0)

cv2.destroyAllWindows()