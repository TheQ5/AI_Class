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
    db="2019-08-27",    #資料庫名稱
    charset="utf8"    #編碼類型
)
cmd=conn.cursor()
p = requests.get(
    "https://udn.com/news/breaknews/1",
)

p.encoding = "utf8"


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
        # print(r.text)
        e=BeautifulSoup(r.text,"html.parser")
        b1=e.find("div",{"id":"story_body_content"})
        txt=""
        for dd in b1.find_all("p"):
            txt += dd.text
        
        cmd.execute(
            "INSERT INTO `udn_news`(`url`,`title`,`content`) VALUES(%s,%s,%s)"
        ,(a4.find("a").attrs["href"],a4.find("a").text,txt))
        conn.commit()

        new_id = cmd.lastrowid
        k = jieba.analyse.extract_tags(txt)
        for kk in k:
            cmd.execute(
                "INSERT INTO `udn_keyword`(`news_id`,`keyword`) VALUES(%s,%s)"
            ,(new_id,kk))
            conn.commit()
conn.close()

UserKey = input("請輸入你要找的關鍵字")

cmd.execute("SELECT * FROM `udn_keyword` WHERE `keyword` = %s",(UserKey))
conn.commit()
x=cmd.fetchall()
print(X)