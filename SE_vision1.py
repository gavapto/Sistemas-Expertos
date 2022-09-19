# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 13:44:11 2022

@author: Gustavo
"""

import cv2
import numpy as np 

img= cv2.imread("caballo1.jpg",0)

cv2.imshow("un caballito",img)
cv2.waitKey(0)
cv2.destroyAllWindows()