import cv2

img = cv2.imread('images/4star.jpg') 			# 검색하려는 도형
shapes = cv2.imread('images/shapestomatch.jpg') 	# 여러 도형이 존재하는 이미지

# 그레이 스케일로 변환
gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gShapes = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)

# 이진화 이미지 생성
ret, bImg = cv2.threshold(gImg, 127, 255, cv2.THRESH_BINARY_INV)
ret, bShapes = cv2.threshold(gShapes, 127, 255, cv2.THRESH_BINARY_INV)

# 바깥쪽 외곽선의 꼭지점 좌표 저장
cImg, hier = cv2.findContours(bImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cShapes, hier = cv2.findContours(bShapes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

matchs = []		# 외곽선과 매칭 점수를 보관할 리스트
for con in cShapes:	# 각 도형과 매칭을 위한 반복문
     # 대상 도형과 여러 도형 중 하나와 매칭 실행
     score = cv2.matchShapes(cImg[0], con, cv2.CONTOURS_MATCH_I3, 0.0)
     # 매칭 점수와 외곽선 정보 저장
     matchs.append( (score, con) )
     # 해당 도형의 외곽선 시작 지점에 매칭 점수 표시
     cv2.putText(shapes, '%.2f'%score, tuple(con[0][0]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1 )

# 매칭 점수로 정렬
matchs.sort(key=lambda x : x[0])		 

# 가장 작은 매칭 점수를 얻는 도형의 외곽선에 선 그리기
cv2.drawContours(shapes, [matchs[0][1]], -1, (0,255,0), 3)

cv2.imshow('target', img)
cv2.imshow('Match Shape', shapes)
cv2.waitKey()
cv2.destroyAllWindows()
