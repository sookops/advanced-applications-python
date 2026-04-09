import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)

ret1, t_bin = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
ret2, t_bininv = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY_INV)
ret3, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print(ret1, ret2, ret3)	# 임계값 출력

plt.subplot(2, 2, 1); plt.imshow(img, cmap='gray')
plt.subplot(2, 2, 2); plt.imshow(t_bin, cmap='gray')
plt.subplot(2, 2, 3); plt.imshow(t_bininv, cmap='gray')
plt.subplot(2, 2, 4); plt.imshow(t_otsu, cmap='gray')
plt.show()
