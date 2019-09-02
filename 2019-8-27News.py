from bs4 import BeautifulSoup
import requests
import codecs
import pymysql
import jieba
import jieba.analyse


conn=pymysql.connect(
    host="localhost", #從其他地方存取要找到IP位置
    user="root",      #選擇資料庫>按上方的伺服器>選擇使用者帳號
    passwd="",        #密碼,顯示否則為空
    db="2019-8-27",    #資料庫名稱
    charset="utf8"    #編碼類型
)
cmd=conn.cursor()
p = requests.get(
    "https://udn.com/news/breaknews/1",
)

p.encoding = "utf8"

#取得網址資料
x = BeautifulSoup(p.text,"html.parser")
a1 = x.find("div",{
    "id" : "breaknews_body"
})
a2=a1.find("dl").find_all("dt")
for a3 in a2:
    a4 = a3.find("h2")
    if a4 !=None:
        r = requests.get(
            "https://udn.com"+a4.find("a").attrs["href"],
        )
        r.encoding = "utf8"
        e=BeautifulSoup(r.text,"html.parser")
        b1=e.find("div",{"id":"story_body_content"})
        txt=""
        for dd in b1.find_all("p"):
            txt += dd.text

        #把第一頁資料放進資料表
        cmd.execute(
            "INSERT INTO `udn_news`(`url`,`title`,`content`) VALUES(%s,%s,%s)"
        ,(a4.find("a").attrs["href"],a4.find("a").text,txt))
        conn.commit()

        #把第一頁關鍵字放進資料表
        new_id = cmd.lastrowid
        k = jieba.analyse.extract_tags(txt)
        for kk in k:
            cmd.execute(
                "INSERT INTO `udn_keyword`(`news_id`,`keyword`) VALUES(%s,%s)"
            ,(new_id,kk))
            conn.commit()

#顯示進度
print("第", 1 ,"頁搜尋完畢")

#第2~10頁資料
times = 0
while times < 9:

    p = requests.get(
        "https://udn.com/news/get_breaks_article/"+ str(times+2) +"/1/",
    )

    p.encoding = "utf8"

    #取得網頁資料
    x = BeautifulSoup(p.text,"html.parser")
    a1 = x.find_all("dt",{
        "class" : "lazyload"
    })
    for i in a1:
        r = requests.get(
            "https://udn.com"+i.find("a").attrs["href"],
        )
        r.encoding = "utf8"


        e=BeautifulSoup(r.text,"html.parser")
        title = e.find("h1").text   
        b1=e.find("div",{"id":"story_body_content"})
        txt = ""
        for dd in b1.find_all("p"):
            txt += dd.text

        #把2~10頁新聞放進資料夾
        cmd.execute(
            "INSERT INTO `udn_news`(`url`,`title`,`content`) VALUES(%s,%s,%s)"
        ,(i.find("a").attrs["href"],title,txt))
        conn.commit()

        #把2~10頁關鍵字放進資料夾
        new_id = cmd.lastrowid
        k = jieba.analyse.extract_tags(txt)
        for kk in k:
            cmd.execute(
                "INSERT INTO `udn_keyword`(`news_id`,`keyword`) VALUES(%s,%s)"
            ,(new_id,kk))
            conn.commit()

    #顯示進度
    print("第",times+2,"頁搜尋完畢")
    times += 1
    
#透過關鍵字找新聞
UserKey = input("請輸入你要找的關鍵字:")

cmd.execute("SELECT `title`,`url` FROM `udn_news` WHERE `content` OR `title` LIKE CONCAT('%%', %s, '%%')",(UserKey))
conn.commit()
x=cmd.fetchall()

#將結果製作成表格
table = prettytable.PrettyTable(["標題","url"],encoding = "utf8")
for i in x:
    table.add_row(i)
print(table)

conn.close()