import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/cat.bmp', cv2.IMREAD_GRAYSCALE)

img_norm = cv2.normalize(img, None, 100, 255, cv2.NORM_MINMAX)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 256])

cv2.imshow('Before', img)
cv2.imshow('Normalize', img_norm)

plt.subplot(1, 2, 1); plt.plot(hist)
plt.subplot(1, 2, 2); plt.plot(hist_norm)
plt.show()
