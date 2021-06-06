import cv2
import os
import imutils

pnombre='Franco'
dataPath='C:\Users\Franco\Pictures\TMPI\IdOjosYCara\Data'
pPath = dataPath = '/' pnombre

if not os.path.exists(pPath):
	print ('Carpeta creada: ', pPath)
	os.makedirs(pPath)

cap = cv2.VideoCaptura(0, cv2.CAP_DSHOW)
faceClassif = cv2.CascadeClassifier('C:\Users\Franco\Pictures\TMPI\IdOjosYCara\haarcascade_frontalface_default.xml')

count = 0

while True:
	ret,frame = cap.read()
	if ret = False: break
	frame = imutils.resize(frame, width = 640)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	face = faceClassif.detectMultiScale(gray, 1.3,5)

	for(x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),2)
		rostro = auxFrame[y:y+h, x: x+w]
		rostro = cv2.resize(rostro,(150,150), interpolation = cv2.INTER_CUBIC)
		cv2.imwrite(pPath + '/rostro_().jpg',format(count, rostro))
		count = count +1

	cv2.imshow('frame',frame)
	k = cv2.waitKey(1)

	if k==27 or count >=300
	break

cap.release()
cv2.destroyAllWindows()