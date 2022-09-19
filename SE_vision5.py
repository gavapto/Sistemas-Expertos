# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:06:24 2022

@author: Gustavo
"""

import cv2
import numpy as np

img= cv2.imread("caballo1.jpg",1)
img2= cv2.imread("caballo2.jpg",1)
tay0= cv2.imread("sisi.jpg",1)

ca1=img[:225,:310]
ca2=img2[:,:310]
tay= cv2.resize(tay0,(100,100))
rows,columns, channels=tay.shape
roi=ca1[:rows,:columns]
print(ca2.size)
print(ca1.size)
print(tay.size)

add= ca2+ca1
add2=cv2.add(ca1,ca2)
peso=cv2.addWeighted(ca1, 0.6, ca2, 0.6, 0)

cv2.imshow("1",img)
cv2.imshow("2",img2)
cv2.imshow("suma",add)
cv2.imshow("suma 2.0",add2)
cv2.imshow("suma 3.0",peso)

img2gray= cv2.cvtColor(tay, 0)
ret,mask=cv2.threshold(img2gray,220,255, cv2.THRESH_BINARY_INV)
mask_inv=cv2.bitwise_not(mask)
#img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
#img2_fg= cv2.bitwise_and(tay, tay, mask=mask)

#dst=cv2.add(img1_bg,img2_fg)
#peso[:rows,:columns]=dst


cv2.imshow("suma final",peso)
cv2.waitKey(0)
cv2.destroyAllWindows()