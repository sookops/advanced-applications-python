import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/bufs.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

img_equal = cv2.equalizeHist(img)       # 평활화를 수행하는 내장 함수
hist_equal = cv2.calcHist([img_equal], [0], None, [256], [0, 256])
cv2.imshow('Before', img)
cv2.imshow('Eequalization', img_equal)

plt.subplot(1, 2, 1); plt.plot(hist)
plt.subplot(1, 2, 2); plt.plot(hist_equal)
plt.show()

