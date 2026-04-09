import cv2
import numpy as np

img = np.full((500, 500, 3), 0, dtype=np.uint8)    # 검은 바탕 이미지 생성
win_name = "Paper"	    # 출력창 이름
cv2.imshow(win_name,img)    # 이미지 표시

def onChange(x):    # 트랙바 콜백 함수 정의
    r = cv2.getTrackbarPos('R',win_name)   # 트랙바 위치 읽기            
    g = cv2.getTrackbarPos('G',win_name)               
    b = cv2.getTrackbarPos('B',win_name)        
    img[:] = [b,g,r]            # 기존 이미지에 새로운 픽셀 값 적용
    cv2.imshow(win_name, img)   # 이미지 갱신

cv2.createTrackbar('R', win_name, 0, 255, onChange)  # 트랙바 생성
cv2.createTrackbar('G', win_name, 0, 255, onChange)
cv2.createTrackbar('B', win_name, 0, 255, onChange)

cv2.waitKey()
cv2.destroyAllWindows()

