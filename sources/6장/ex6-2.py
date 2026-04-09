import cv2

img = cv2.imread('images/bufs.jpg')

cv2.line(img, (100, 50), (500, 50), (255,0,0))
cv2.line(img, (100, 100), (500, 100), (0,255,0), 5)
cv2.line(img, (100, 200), (500, 220), (0,0,255), 30, cv2.LINE_4)
cv2.line(img, (100, 250), (500, 270), (0,0,255), 30, cv2.LINE_8)
cv2.line(img, (100, 300), (500, 320), (0,0,255), 30, cv2.LINE_AA)

cv2.line(img, (600, 50), (600, 350), (0,255,255), 2)
cv2.line(img, (650, 50), (650, 350), (255,0,255), 4)
cv2.line(img, (700, 50), (700, 350), (0,0,0), 6)

cv2.imshow('Lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


  


 
