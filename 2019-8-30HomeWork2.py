import cv2
import numpy as numpy

#如果不使用顏色反轉,會出現幾個像素的黑點

#取得指定圖片
pic = cv2.imread("homework2.png", 1)

#指定只有純紅色在範圍內
pic2 = cv2.inRange(pic, (0, 0, 254),(0, 0, 255) )

#顏色反轉
pic3 = cv2.bitwise_not(pic2)

#顯示圖像
cv2.imshow("Img", pic3)
cv2.waitKey(0)
cv2.destroyAllWindows()