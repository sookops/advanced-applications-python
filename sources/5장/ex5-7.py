import cv2
    
img = cv2.imread("images/bufs.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("BUFS_Gray", img)		
cv2.imwrite("bufs_gray.jpg", img)		# 파일로 저장
cv2.waitKey()					
cv2.destroyAllWindows()	




