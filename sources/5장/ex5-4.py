import cv2, sys

img = cv2.imread("images/bufs.jpg")

if img is None:
     print("No image file")
     sys.exit()		

cv2.imshow("BUFS", img)	
while True:
     if cv2.waitKey(0) == 27:  # ESC 검사
          break
cv2.destroyAllWindows()	   
