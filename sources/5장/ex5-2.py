import cv2, sys

img = cv2.imread("images/bufs.jpg", cv2.IMREAD_GRAYSCALE)	

if img is None:			
	print("No image file")
	sys.exit()		

cv2.imshow("BUFS", img)	
cv2.waitKey()		
cv2.destroyAllWindows()	   




