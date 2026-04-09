import cv2

img = cv2.imread('images/lenna.png', cv2.IMREAD_GRAYSCALE)
win_name = "Ex9-2"		# 출력창 이름
cv2.imshow(win_name, img)	# 이미지 표시

def onChange(x):  # 트랙바 콜백 함수 정의
     val = cv2.getTrackbarPos('Brightness', win_name)       
     img2 = cv2.add(img, val-100)       # 상수 덧셈은 첫 번째 채널에만 적용 
     cv2.imshow(win_name, img2)         # 이미지 표시

cv2.createTrackbar('Brightness', win_name, 100, 200, onChange) # 트랙바 생성
cv2.waitKey()
cv2.destroyAllWindows()

