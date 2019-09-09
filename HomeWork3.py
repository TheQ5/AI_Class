import cv2
import numpy as np

video = cv2.VideoCapture("homework3.mp4")
while True:
    TrueOrFalse, Slide = video.read()
    
    if TrueOrFalse ==True:

        GraySlide=cv2.subtract(cv2.subtract(Slide[:,:,0], Slide[:,:,2]), Slide[:,:,1])
        # cv2.imshow("www", GraySlide)

        BinSlide = cv2.inRange(GraySlide, 5, 65)
        # cv2.imshow("m2", BinSlide)

        #膨脹侵蝕
        BinSlide = cv2.dilate(BinSlide, np.ones((95, 95)))
        BinSlide = cv2.erode(BinSlide, np.ones((60, 60)))

        #取輪廓數據
        aa,bb=cv2.findContours(BinSlide ,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

        #把輪廓印出來
        for i in aa:
            x, y, w, h =cv2.boundingRect(i)
            cv2.rectangle(Slide, (x, y), (x+w, y+h), (0, 0, 255), 2)      #先把紅框框全部畫上

        cv2.imshow("ShowPage", Slide)         #最後再一次印出
        if cv2.waitKey(30) == 13:
            break
    else:
        break 
cv2.destroyAllWindows()