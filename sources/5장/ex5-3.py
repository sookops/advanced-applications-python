import cv2, sys

img = cv2.imread("images/bufs.jpg")

if img is None:
     print("No image file")
     sys.exit()		

cv2.imshow("BUFS", img)	
cv2.waitKey(5000)		
cv2.destroyAllWindows()	   



