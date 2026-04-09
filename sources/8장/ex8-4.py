import matplotlib.pyplot as plt
import cv2

imgBGR = cv2.imread("images/lenna.png")
bgr = cv2.split(imgBGR)      # 채널 분리

rgb = [bgr[2], bgr[1], bgr[0]]
gbr = [bgr[1], bgr[0], bgr[2]]

imgRGB = cv2.merge(rgb)
imgGBR = cv2.merge(gbr)

# 영상 출력
plt.subplot(1, 3, 1)
plt.title('RGB')
plt.axis('off')
plt.imshow(imgRGB)
plt.subplot(1, 3, 2)
plt.title('BGR')
plt.axis('off')
plt.imshow(imgBGR)
plt.subplot(1, 3, 3)
plt.title('GBR')
plt.axis('off')
plt.imshow(imgGBR)
plt.show()



