import cv2
import numpy as np

img_gray = np.zeros((240, 240), dtype=np.uint8)
img_gray[50:70, :] = 45
img_gray[110:130, :] = 115
img_gray[170:190, :] = 160

img_color = np.full((240, 240, 3), (0, 255, 255), dtype=np.uint8)
img_color[50:70, :] = (255, 0, 0)
img_color[110:130, :] = (0, 255, 0)
img_color[170:190, :] = (0, 0, 255)

cv2.imshow('Gray', img_gray)
cv2.waitKey()
cv2.imshow('Color', img_color)
cv2.waitKey()
cv2.destroyAllWindows()




