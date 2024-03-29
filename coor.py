import pyautogui as p
import time

while 1:
	time.sleep(2)
	x,y=p.position()
	print(x,y)