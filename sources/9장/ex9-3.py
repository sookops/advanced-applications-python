import cv2

img1 = cv2.imread('images/small_lenna.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('images/circle.jpg', cv2.IMREAD_GRAYSCALE)

img3 = cv2.subtract(img1, img2)

cv2.imshow('original', img1)
cv2.imshow('circle', img2)
cv2.imshow('subtract', img3)

cv2.waitKey()
cv2.destroyAllWindows()

