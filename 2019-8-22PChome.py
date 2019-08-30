import requests
import prettytable
import json
import os

#請使用者輸入關鍵字
Keyword = input("請輸入關鍵字")

#取得網站資訊
Flag = True
Page = "1"
while Flag == True :
	os.system("cls")
	p = requests.get(
	    "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=" + Keyword + "&page=" + Page +"&sort=sale/dc"
	)

	#設定編碼並載入到變數 j
	p.encoding = "utf8"
	j = json.loads(p.text)

	#建立商品表格GoodTable
	GoodTable = prettytable.PrettyTable(["商品","價格"], encoding="utf-8")

	#取得商品資訊
	GoodList = j["prods"]
	for GoodDict in GoodList:

		#將取得的商品名稱及價格轉換成List型態,ADD到表格列中
		TableList = [GoodDict["name"] , GoodDict["originPrice"]]
		GoodTable.add_row(TableList)

	#商品名稱向左對齊並輸出表格	
	GoodTable.align["商品"]="l"
	print(GoodTable)

	#使用者選擇商品頁面
	Page = input("請輸入商品頁數")

	#判斷輸入的合理性(須是大於0的數字)
	if str.isdigit(Page) and Page>="1":
		Flag = True
	else:
		Flag = False
print("輸入大於0的數字")