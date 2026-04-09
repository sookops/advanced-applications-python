import cv2
import numpy as np
img = np.full((500, 500, 3), 255, dtype=np.uint8)    # 흰 바탕 이미지 생성

cv2.putText(img, "Plain-1", (20, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))
cv2.putText(img, "Plain-1.5", (120, 30), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,0))
cv2.putText(img, "Plain-2", (250, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0))

cv2.putText(img, "Simplex", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))        
cv2.putText(img, "Duplex", (20, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,255))          

cv2.putText(img, "Complex Small", (20, 180), \
	cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255))   
cv2.putText(img, "Complex", (20, 220), cv2.FONT_HERSHEY_COMPLEX, 1, \
	(255,0,0))
cv2.putText(img, "Triplex", (20, 260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,255,0))

cv2.putText(img, "Script Simplex", (20, 330), \
	cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,0)) 
cv2.putText(img, "Hershey Script Complex", (20, 370), \
	cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0,0,0)) 

cv2.putText(img, "Hershey Plain &Italic", (20, 430), \
	cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC, 1, (0,0,0)) 
cv2.putText(img, "Hershey Complex & Italic", (20, 470), \
	cv2.FONT_HERSHEY_COMPLEX | cv2.FONT_ITALIC, 1, (0,0,0)) 

cv2.imshow('draw text', img)
cv2.waitKey()
cv2.destroyAllWindows()

  


 
