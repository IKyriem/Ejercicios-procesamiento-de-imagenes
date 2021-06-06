import numpy as np
import cv2



cap = cv2.VideoCapture(0)
def verify_alpha_channel(frame):
    try:
        frame.shape[3] # looking for the alpha channel
    except IndexError:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    return frame

def apply_sepia(frame, intensity=0.5):
    frame = verify_alpha_channel(frame)
    frame_h, frame_w, frame_c = frame.shape
    sepia_bgra = (20, 66, 112, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)
    return frame

def apply_invert(frame):
    return cv2.bitwise_not(frame)

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA) 
    #cv2.imshow('frame',frame)

    sepia = apply_sepia(frame.copy(), intensity=.8)
    cv2.imshow('sepia',sepia)

    invert = apply_invert(frame.copy())
    cv2.imshow('invert', invert)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()