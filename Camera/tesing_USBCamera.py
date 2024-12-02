import cv2
from cv2 import VideoCapture
#camera_index is the video device number of the camera 
camera_index = 0
cam = cv2.VideoCapture(camera_index)

while True:
 ret, image = cam.read()
 cv2.imshow('Imagetest',image)
 k = cv2.waitKey(1) 
 if k != -1:
  break
cv2.imwrite('/home/pi/Desktop/Sensing/Camera/images/test.jpg', image)
cam.release()
cv2.destroyAllWindows()


import PyQt5
print(PyQt5.__file__)