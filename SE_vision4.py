# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:49:23 2022

@author: Gustavo
"""
import cv2
import numpy as np

img= cv2.imread("caballo1.jpg",1)

px= img[100,100]

img[100,100]=[0,0,0]

print(px)
print(img.shape)
print(img.size)
print(img.dtype)

cara=img[0:80,55:95]

img[0:80,0:40]=cara
for x in range(7):
    img[80:160,(x*40):(x*40)+40]=cara

cv2.imshow("caballito",img)
cv2.waitKey(0)
cv2.destroyAllWindows()