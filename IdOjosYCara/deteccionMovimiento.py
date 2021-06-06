import numpy as np 
import cv2

video = cv2.VideoCapture('videoExamen.avi')
i=0

while True:
	ret, frame = video.read()
	if ret == False: break
	if i == 20:
		bgGray = gray
	if i > 20:
		dif = cv2.absdiff(gray,bgGray)
		_,th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
		cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX)

		for c in cnts:
			area =  cv2.contourArea(c)
			if area > 9000:
				x,y,w,h = cv2.boundingRect(c)
				cv2.rectangle(frame, (x,y), (w+w, y+h),(0,255,0),2)

	cv2.imshow('Frame', frame)

	i=i+1
	if cv2.waitKey(30) & 0xFF == ord('q'):
		break
video.release()
