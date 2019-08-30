import requests
import codecs

p = requests.get(
    "http://teaching.bo-yuan.net/test/requests/",
    
)
#得到提示:缺少參數「action」。
p.encoding ="utf8"
print(p.text)


p = requests.get(
    "http://teaching.bo-yuan.net/test/requests/",
    params = {
        "action" : "action"
    }
)
#得到提示:需要DELETE的操作。
p.encoding ="utf8"
print(p.text)


p = requests.delete(
    "http://teaching.bo-yuan.net/test/requests/",
    params = {
        "action" : "action"
    }
)
#得到提示:缺少資料「id」。
p.encoding ="utf8"
print(p.text)



p = requests.delete(
    "http://teaching.bo-yuan.net/test/requests/",
    params = {
        "action" : "action"
    },
    data = {
        "id" : "id"
    }
)
#得到提示:記得去PUT操作。
p.encoding ="utf8"
print(p.text)


p = requests.put(
    "http://teaching.bo-yuan.net/test/requests/",
    params = {
        "action" : "action"
    },
    data = {
        "id" : "id"
    }
)
#得到提示:需要更新資料「name」。
p.encoding ="utf8"
print(p.text)


p = requests.put(
    "http://teaching.bo-yuan.net/test/requests/",
    params = {
        "action" : "action"
    },
    data = {
        "id" : "id",
        "name" : "name"
    }
)
#得到提示:PUT完了，也要PATCH資料。
p.encoding ="utf8"
print(p.text)


p = requests.patch(
    "http://teaching.bo-yuan.net/test/requests/",
    params = {
        "action" : "action"
    },
    data = {
        "id" : "id",
        "name" : "name"
    }
)
#得到提示:需要PATCH的資料是「address」。
p.encoding ="utf8"
print(p.text)


p = requests.patch(
    "http://teaching.bo-yuan.net/test/requests/",
    params = {
        "action" : "action"
    },
    data = {
        "id" : "id",
        "name" : "name",
        "address" : "address"
    }
)
#得到提示:最後POST一筆資料吧。
p.encoding ="utf8"
print(p.text)


p = requests.post(
    "http://teaching.bo-yuan.net/test/requests/",
    params = {
        "action" : "action"
    },
    data = {
        "id" : "id",
        "name" : "name",
        "address" : "address"
    }
)
#得到答案:哈哈，答對了，請把操作過程中的所有指令保留在程式碼中，將檔案繳交上來。
p.encoding ="utf8"
print(p.text)

# f = codecs.open("爬蟲.txt","w","utf8")
# f.write(p.text)
# f.close()

