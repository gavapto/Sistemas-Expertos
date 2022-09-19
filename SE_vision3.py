# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 13:44:11 2022

@author: Gustavo
"""

import cv2
import numpy as np 

img= cv2.imread("caballo1.jpg",1)

cv2.line(img,(100,0),(200,200),(255,255,255),5)

cv2.rectangle(img,(50,150),(200,200),(255,0,0),10)

cv2.circle(img,(100,100),70,(0,0,255),8)

pts=np.array([[10,20],[100,100],[35,67],[200,79]])
cv2.polylines(img,[pts],True,(0,255,0),12)

font= cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Juan",(20,100),font,3,(255,255,0),3, cv2.LINE_AA)

cv2.imshow("caballo rayado", img)
cv2.waitKey(0)
cv2.destroyAllWindows()