import cv2
import matplotlib.pyplot as plt

# 컬러 영상 출력
imgBGR = cv2.imread("images/cat.bmp")
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)
plt.axis('off')	    # 축을 표시하지 않음
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread("images/cat.bmp", cv2.IMREAD_GRAYSCALE)
plt.imshow(imgGray, cmap='gray')
plt.axis('off')	    # 축을 표시하지 않음
plt.show()

 
