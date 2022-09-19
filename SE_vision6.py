# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 12:54:33 2022

@author: Gustavo
"""

import cv2
import numpy as np

img= cv2.imread("bookpage.jpg",1)
gray= cv2.imread("bookpage.jpg",0)

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('original',img)
cv2.imshow('threshold',threshold)

retval2, threshold2 = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold2',threshold2)

threshold3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('threshold3',threshold3)
 
cv2.waitKey(0)
cv2.destroyAllWindows()