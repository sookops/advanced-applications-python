import cv2
import numpy as np

img = np.full((500, 500, 3), 255, dtype=np.uint8)    # 흰 바탕 이미지 생성

cv2.rectangle(img, (100,100), (300, 300), (0,0,255))
cv2.rectangle(img, (150, 150), (200, 200), (0, 255, 0), -1)
cv2.rectangle(img, (300, 400), (100, 350), (0, 0, 0), 5)
cv2.rectangle(img, (400, 50), (250, 450), (255, 0, 0), 2)

cv2.imshow('Rectangle', img)
cv2.imwrite('Rectangles.jpg', img)      # 이미지 저장
cv2.waitKey(0)
cv2.destroyAllWindows()



  


 
