import cv2 

cap = cv2.VideoCapture('videoPrueba.mp4')

while(cap.isOpened()):
	ret, imagen = cap.read()
	if ret == True:
		cv2.imshow('video', imagen)
		if cv2.waitKey(30) == ord('s'):
			break
	else: break
cap.release()
cv2.destroyAllWindows()