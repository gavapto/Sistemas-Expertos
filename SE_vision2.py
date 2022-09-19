# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 13:44:11 2022

@author: Gustavo
"""

import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
     break
 
cv2.waitKey(0)
cv2.destroyAllWindows() 