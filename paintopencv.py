#!/home/drk/anaconda3/bin/python
#modules used
import random
import numpy as np
import cv2 as cv
import math
import time
#black image (y,x)
img = np.zeros((720,1048,3), np.uint8)
#creates a window named image
cv.namedWindow('image')
#select the font
font = cv.FONT_HERSHEY_SIMPLEX
#(b,g,r)
while(1):
	cv.imshow("image",img)
	cv.putText(img,"Welcome Welcome",(200,350),font,2,(142,251,42),3,cv.LINE_AA)
	cv.putText(img,"Press S to Start",(400,500),font,1,(42,251,142),1,cv.LINE_AA)
	if cv.waitKey(1) & 0xFF == ord("s"):
		img = np.zeros((720,1048,3), np.uint8)
		break
while(1):
	cv.imshow("image",img)
	cv.putText(img,"You have to draw something",(20,350),font,2,(142,251,42),1,cv.LINE_AA)
	cv.putText(img,"using 8 different modes ",(50,400),font,1,(142,251,42),1,cv.LINE_AA)
	cv.putText(img,"Press Space to Continue",(70,600),font,1,(42,251,142),1,cv.LINE_AA)
	if cv.waitKey(1) & 0xFF == 32:
		img = np.zeros((720,1048,3), np.uint8)*255
		break
while(1):
	cv.imshow("image",img)
	cv.putText(img,"TIPS",(20,100),font,2,(142,251,42),1,cv.LINE_AA)
	cv.putText(img,"1. First Change the Canvas Color and then draw on it",(50,150),font,1,(142,251,42),1,cv.LINE_AA)
	cv.putText(img,"2. Use canvas color brush in mode 6 to erase",(50,200),font,1,(142,251,42),1,cv.LINE_AA)
	cv.putText(img,"COMMANDS",(20,300),font,2,(42,251,12),1,cv.LINE_AA)
	cv.putText(img,"Press ESC to Get OUT",(50,350),font,1,(42,251,12),0,cv.LINE_AA)
	cv.putText(img,"Press R to Reset",(50,400),font,1,(42,251,12),0,cv.LINE_AA)
	cv.putText(img,"Press S to Save",(50,450),font,1,(42,251,12),0,cv.LINE_AA)
	cv.putText(img,"Press Space to Continue",(50,700),font,1,(42,251,142),1,cv.LINE_AA)
	cv.putText(img,"MODES",(600,300),font,2,(42,25,142),1,cv.LINE_AA)
	cv.putText(img,"0-rectangle",(600,350),font,1,(42,25,142),0,cv.LINE_AA)
	cv.putText(img,"1-lines",(600,400),font,1,(42,25,142),0,cv.LINE_AA)
	cv.putText(img,"2-one point lines",(600,450),font,1,(42,25,142),0,cv.LINE_AA)
	cv.putText(img,"3-concentric circles",(600,500),font,1,(42,25,142),0,cv.LINE_AA)
	cv.putText(img,"4-circle",(600,550),font,1,(42,25,142),1,cv.LINE_AA)
	cv.putText(img,"5-brush",(600,600),font,1,(42,25,142),1,cv.LINE_AA)
	cv.putText(img,"6-one point circles",(600,650),font,1,(42,25,142),0,cv.LINE_AA)
	cv.putText(img,"7-eraser",(600,700),font,1,(42,25,142),0,cv.LINE_AA)
	if cv.waitKey(1) & 0xFF == 32:
		img = np.ones((720,1048,3), np.uint8)*255
		break
drawing = False
mode = True
ix,iy = -1,-1
b,g,r = (0,0,0)
t = 1
b3,g3,r3=(255,255,255)
def nothing(x):
    pass
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
switch = 'Draw: 0 \n Canvas:1 \n Menu'
cv.createTrackbar(switch,'image',0,2,nothing)
cv.createTrackbar('T','image',1,500,nothing)
cv.createTrackbar('M','image',0,7,nothing)
def trackbar():
	global b,g,r,t,b1,g1,r1,t1,b2,g2,r2,t2,b3,g3,r3,s,mode
	s = cv.getTrackbarPos(switch,'image')
	if s==0:
		r = cv.getTrackbarPos('R','image')
		g = cv.getTrackbarPos('G','image')
		b = cv.getTrackbarPos('B','image')
		t = cv.getTrackbarPos('T','image')
		mode = cv.getTrackbarPos('M','image')
	elif s==1:
		r3 = cv.getTrackbarPos('R','image')
		g3 = cv.getTrackbarPos('G','image')
		b3 = cv.getTrackbarPos('B','image')
		img[:]=[b3,g3,r3]
	elif s==2:
		img1 = np.zeros((720,1048,3), np.uint8)*255
		while(1):
			cv.imshow('image',img1)
			cv.putText(img1,"TIPS",(20,100),font,2,(142,251,42),1,cv.LINE_AA)
			cv.putText(img1,"1. First Change the Canvas Color and then draw on it",(50,150),font,1,(142,251,42),1,cv.LINE_AA)
			cv.putText(img1,"2. Use canvas color brush in mode 6 to erase",(50,200),font,1,(142,251,42),1,cv.LINE_AA)
			cv.putText(img1,"COMMANDS",(20,300),font,2,(42,251,12),1,cv.LINE_AA)
			cv.putText(img1,"Press ESC to Get OUT",(50,350),font,1,(42,251,12),0,cv.LINE_AA)
			cv.putText(img1,"Press R to Reset",(50,400),font,1,(42,251,12),0,cv.LINE_AA)
			cv.putText(img1,"Press S to Save",(50,450),font,1,(42,251,12),0,cv.LINE_AA)
			cv.putText(img1,"Press Space to Continue",(50,700),font,1,(42,251,142),1,cv.LINE_AA)
			cv.putText(img1,"MODES",(600,300),font,2,(42,25,142),1,cv.LINE_AA)
			cv.putText(img1,"0-rectangle",(600,350),font,1,(42,25,142),0,cv.LINE_AA)
			cv.putText(img1,"1-lines",(600,400),font,1,(42,25,142),0,cv.LINE_AA)
			cv.putText(img1,"2-one point lines",(600,450),font,1,(42,25,142),0,cv.LINE_AA)
			cv.putText(img1,"3-concentric circles",(600,500),font,1,(42,25,142),0,cv.LINE_AA)
			cv.putText(img1,"4-circle",(600,550),font,1,(42,25,142),1,cv.LINE_AA)
			cv.putText(img1,"5-brush",(600,600),font,1,(42,25,142),1,cv.LINE_AA)
			cv.putText(img1,"6-one point circles",(600,650),font,1,(42,25,142),0,cv.LINE_AA)
			cv.putText(img1,"7-eraser",(600,700),font,1,(42,25,142),0,cv.LINE_AA)
			if cv.waitKey(1) & 0xFF == 32:
				img1 = np.ones((720,1048,3), np.uint8)*255
				break
def draw_func(event,x,y,flags,param):
	global ix,iy,drawing,mode
	if event == cv.EVENT_LBUTTONDOWN:
		drawing = True
		ix,iy = x,y
	elif event == cv.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == 0:
				cv.rectangle(img,(ix,iy),(ix,iy),(b,g,r),t)
			elif mode == 1:
				pass
			elif mode == 2:
				t1 = t
				if t1 == 0:
					t1 = t
				cv.line(img,(ix,y),(x,iy),(b,g,r),t1)
			elif mode == 3:
				radius =int(pow(((x-ix)**2+(y-iy)**2),0.5))
				cv.circle(img,(ix,iy),radius,(b,g,r),t)
			elif mode == 5 :
				cv.circle(img,(x,y),t,(b,g,r),-1)
			elif mode == 6:
				radius =int(pow(((x-ix)**2+(y-iy)**2),0.5))
				cv.circle(img,(x,y),radius,(b,g,r),t)
			elif mode == 7 :
				cv.circle(img,(x,y),t,(b3,g3,r3),-1)
	elif event == cv.EVENT_LBUTTONUP:
		drawing = False
		if mode == 0:
			cv.rectangle(img,(ix,iy),(x,y),(b,g,r),t)
		elif mode == 1:
			cv.line(img,(ix,iy),(x,y),(b,g,r),t)
		elif mode == 2:
			pass
		elif mode == 3:
			radius =int(pow(((x-ix)**2+(y-iy)**2),0.5))
			cv.circle(img,(ix,iy),radius,(b,g,r),t)
		elif mode == 4:
			radius =int(pow(((x-ix)**2+(y-iy)**2),0.5))
			cv.circle(img,(ix,iy),radius,(b,g,r),t)
		elif mode == 5:
			cv.circle(img,(x,y),t,(b,g,r),-1)
		elif mode == 6:
			pass
		elif mode == 7:
			cv.circle(img,(x,y),t,(b3,g3,r3),-1)

img = np.ones((720,1048,3),np.uint8)*255
while(1):
	cv.imshow("image",img)
	k = cv.waitKey(1) & 0xFF
	if k == 27:
		break
	elif k == ord('r'):
		img = np.ones((720,1048,3), np.uint8)*255
	elif k == ord('s'):
		n = random.randint(1,100)
		n = str(n)
		x = 'untitled'+n+'.png'
		cv.imwrite(x,img)
	elif k == ord('v'):
			cap = cv.VideoCapture(0)
			if not cap.isOpened():
				print("Cannot open camera")
				exit()
			print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
			print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
			ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,1280)
			ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,720)
			while True:
				ret, frame = cap.read()
				if not ret:
					print("Can't receive frame (stream end?). Exiting ...")
					break
				gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
				cv.imshow('image',gray)
				if cv.waitKey(1) == ord('q'):
					break
				trackbar()
				cv.setMouseCallback("image", draw_func)
			cap.release()
	trackbar()
	cv.setMouseCallback("image", draw_func)
cv.destroyAllWindows()
