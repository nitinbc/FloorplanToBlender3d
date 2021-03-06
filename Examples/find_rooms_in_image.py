import cv2
import numpy as np
import sys
sys.path.insert(0,'..')
from FloorplanToBlenderLib import * # floorplan to blender lib
from subprocess import check_output
import os
import imutils

'''
Find rooms in image
'''

img = cv2.imread("../Examples/example.png")
height, width, channels = img.shape
blank_image = np.zeros((height,width,3), np.uint8) # output image same size as original

# grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = detect.wall_filter(gray)

gray = ~gray

rooms, colored_rooms = detect.find_rooms(gray.copy())

doors, colored_doors = detect.find_details(gray.copy())

gray_rooms =  cv2.cvtColor(colored_doors,cv2.COLOR_BGR2GRAY)

# get box positions for rooms
boxes, gray_rooms = detect.detectPreciseBoxes(gray_rooms, blank_image)

cv2.imshow('colssoroed', img)
cv2.imshow('coloroed', gray_rooms)
cv2.waitKey()
cv2.destroyAllWindows()
