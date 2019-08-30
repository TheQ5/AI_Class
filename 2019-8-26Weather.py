from bs4 import BeautifulSoup
import requests
import codecs

# f = codecs.open("2019-08-26.html","r","utf-8")
# data = f.read()
# f.close()
p = requests.get(
    "https://www.cwb.gov.tw/V7/forecast/f_index.htm?_=1566877180829"
)

p.encoding = "utf-8"
x = BeautifulSoup(p.text , "html.parser")
# print(x)
a1 = x.find("div",{
    "class" : "NorthArea"
})
# print (a1)

a2 = a1.find("table").find_all("td")
# print(a2)
a5 = a2[1::4]
a3 = a2[::4]

for i in a3:
    a4 = i.find("a").text
    print(a4)
for i in a5:
    a6 = i.find("a").text
    print(a6)

# location = a2.find("td", {
#     "width" : "60%"
# })









