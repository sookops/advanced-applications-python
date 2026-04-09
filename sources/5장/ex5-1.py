import cv2, sys

img = cv2.imread("images/bufs.jpg")	# 이미지 불러오기	

if img is None:				# 이미지를 불러올 수 없으면
	print("No image file")
	sys.exit()			# 프로그램 종료

cv2.imshow("BUFS", img)			# 읽은 이미지를 화면에 표시
key = cv2.waitKey()			# 키가 입력될 때까지 대기
cv2.destroyAllWindows()			# 생성된 모든 창을 닫음   




