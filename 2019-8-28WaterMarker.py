import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


FilePath = input("請輸入圖片檔名(路徑):")
WaterMark = input("請輸入浮水印內容:")
WaterMark_size = input("請輸入浮水印尺寸(px):")
BorW = input("請根據背景的顏色,選擇對應的對比色:[0]黑色 [1]白色:")

pic=cv2.imread( FilePath , 1)

if BorW == "0":
    pic = Image.fromarray(pic)
    font = ImageFont.truetype("font/kaiu.ttf", int(WaterMark_size))
    ImageDraw.Draw(pic).text((3,3), WaterMark, (0, 0, 0), font)
    pic = np.array(pic) 

    cv2.imshow("test", pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
elif BorW == "1":
    pic = Image.fromarray(pic)
    font = ImageFont.truetype("font/kaiu.ttf", int(WaterMark_size))
    ImageDraw.Draw(pic).text((0,0), WaterMark, (255, 255, 255), font)
    pic = np.array(pic) 

    cv2.imshow("test", pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()