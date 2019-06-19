#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 8 13:06:56 2018

@author: shadabhussain
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

from skimage import data
img =  data.astronaut()

# 1) Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 2) Color
color = cv2.bilateralFilter(img, 9, 300, 300)

# 3) Cartoon
cartoon = cv2.bitwise_and(color, color, mask=edges)


cv2.imshow("Image", img)
cv2.imshow("Cartoon", cartoon)
cv2.imshow("color", color)
cv2.imshow("edges", edges)


#plt.imshow(img)
#plt.imshow(cartoon)
#plt.imshow(color)
plt.imshow(edges)
