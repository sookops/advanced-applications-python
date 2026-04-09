import cv2

img1 = cv2.imread('images/mano.jpg')
img2 = cv2.imread('images/cat.bmp')

alpha = 0.5

dst1 = cv2.add(img1, img2)
dst2 = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0)

cv2.imshow('add operation', dst1)
cv2.imshow('50% blending', dst2)

cv2.waitKey();
cv2.destroyAllWindows()

