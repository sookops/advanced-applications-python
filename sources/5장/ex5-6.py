import cv2
import numpy as np

img = cv2.imread("images/bufs.jpg")
print(type(img))
print(img.shape)
print(img.dtype)

img = cv2.imread("images/beach_ball.png", cv2.IMREAD_UNCHANGED)
print(img.shape)
print(img.dtype)
