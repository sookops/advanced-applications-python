import cv2

img1 = cv2.imread("images/cat.bmp")	
img2 = cv2.imread("images/cat.bmp", cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('Color', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Gray', cv2.WINDOW_NORMAL)

cv2.imshow('Color', img1)
cv2.imshow('Gray', img2)
 
cv2.moveWindow('Color', 100, 300)
cv2.moveWindow('Gray', 800, 300)
 
cv2.waitKey()      # 아무키나 누를 때까지 대기
cv2.resizeWindow('Color', 600, 300)
cv2.resizeWindow('Gray', 500, 600)

cv2.waitKey()
cv2.destroyWindow('Color')

cv2.waitKey() 
cv2.destroyAllWindows()	

  


 
