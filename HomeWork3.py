import cv2
import numpy as np

video = cv2.VideoCapture("homework3.mp4")
while True:
    TrueOrFalse, Slide = video.read()
    
    if TrueOrFalse ==True:

        #把圖片轉換成灰階
        GraySlide = cv2.cvtColor(Slide, cv2.COLOR_BGR2GRAY)

        #模糊化
        GraySlide=cv2.blur(GraySlide, (5, 10))
        # GraySlide=cv2.medianBlur(GraySlide, 9)
        #範圍內的像素設為白色
        BinSlide = cv2.inRange(GraySlide, 50, 65)
        cv2.imshow("m2", BinSlide)
       
        #模糊化
        # BinSlide=cv2.blur(BinSlide, (10, 10))        

        #膨脹侵蝕
        BinSlide = cv2.dilate(BinSlide, np.ones((90, 90)))
        BinSlide = cv2.erode(BinSlide, np.ones((60, 60)))

        #取輪廓數據
        aa,bb=cv2.findContours(BinSlide ,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

        #把輪廓印出來
        for i in aa:
            x, y, w, h =cv2.boundingRect(i)
            # if area = cv2.contourArea(cnt)
            cv2.rectangle(Slide, (x, y), (x+w, y+h), (0, 0, 255), 2)      #先把紅框框全部畫上

        cv2.imshow("m4", Slide)         #最後再一次印出
        if cv2.waitKey(30) == 13:
            break
    else:
        break 
cv2.destroyAllWindows()






        # m2=np.full(b.shape,255,np.uint8)



        #把藍色凸顯出來
        # a, m2[:,:,0]=cv2.threshold(b[:,:,0], 100, 255, cv2.THRESH_BINARY)
        # a, m2[:,:,1]=cv2.threshold(b[:,:,1], 5, 0, cv2.THRESH_BINARY)
        # a, m2[:,:,2]=cv2.threshold(b[:,:,2], 5, 0, cv2.THRESH_BINARY)


        
        # aa, bb = cv2.threshold(m1, 120, 225, cv2.THRESH_TOZERO_INV)

        # cc, dd = cv2.threshold(bb, 100, 225, cv2.THRESH_BINARY)

        
        # cv2.imshow("pi", m3)
        # cv2.imshow("pic", m2)
        # cv2.imshow("pic2", m1)
        # cv2.imshow("pic1", bb)
        # cv2.imshow("pic2", dd)
        