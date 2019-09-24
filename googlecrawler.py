#!/usr/bin/env python
# coding: utf-8

# In[12]:


# import requests
# h = {
#     "accept-language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
# }
# url = "https://www.google.com/search?ei=6nKJXe6lBIuOr7wPpeeK-Ao&yv=3&q=%E6%B5%A3%E7%86%8A&tbm=isch&vet=10ahUKEwjuwtDtqOjkAhULx4sBHaWzAq8QuT0ISSgB.6nKJXe6lBIuOr7wPpeeK-Ao.i&ved=0ahUKEwjuwtDtqOjkAhULx4sBHaWzAq8QuT0ISSgB&ijn=1&start=100&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc"
# response = requests.get(url, headers = h)
# response.text


# # In[13]:


# from bs4 import BeautifulSoup
# import json
# html = BeautifulSoup(response.text)
# div = html.find("div", class_="rg_meta")
# print("盒子:", div)
# print("網址:", json.loads(div.text)["ou"])


# In[15]:


import requests
from bs4 import BeautifulSoup
import json

imgs_url = []
page = 0
while True:    
    url = ("https://www.google.com/search?ei=ydGJXc6WI_nEmAXM9JOABg&yv=3&q=%E6%96%B0%E5%9E%A3%E7%B5%90%E8%A1%A3&tbm=isch&vet=10ahUKEwiOn-iqg-nkAhV5IqYKHUz6BGAQuT0ITCgB.ydGJXc6WI_nEmAXM9JOABg.i&ved=0ahUKEwiOn-iqg-nkAhV5IqYKHUz6BGAQuT0ITCgB&ijn="
            + str(page) + "&start="
            + str(page * 100) +"&asearch=ichunk&async=_id:rg_s,_pms:s,_jsfs:Ffpdje,_fmt:pc")
    print("第幾頁:", page + 1)
    print("網址:", url)
    h = {
        "accept-language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    }
    response = requests.get(url, headers=h)
    
    html = BeautifulSoup(response.text)
    divs = html.find_all("div", class_="rg_meta")
    
    if len(divs) == 0:
        print("應該是最後一頁了")
        break
    
    print("這頁有幾張?", len(divs))
    for d in divs:
        img = json.loads(d.text)["ou"]
        imgs_url.append(img)
    page = page + 1


# In[16]:


import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

base = "shin"
if not os.path.exists(base):
    os.makedirs(base)
saved = ["jpg", "jpeg", "png"]
for i, iurl in enumerate(imgs_url):
    for f in saved:
        if f.upper() in iurl or f in iurl:
            try:
                iresponse = requests.get(iurl, stream=True, verify=False)
                fn = os.path.join(base, str(i) + "." + f)
                with open(fn, "wb") as f:
                    # .read: .raw是一個檔案, 使用read去讀取
                    f.write(iresponse.raw.read())
            except:
                print("放棄:", iurl)


# In[ ]:




