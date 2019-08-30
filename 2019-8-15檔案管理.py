import os
import codecs
os.chdir("F:\\python")
r=-1
while r != "0": 

	os.system("cls")#每次執行cmd都會清空畫面
	if r == "1":
		for d in os.listdir(os.getcwd()):
			if os.path.isdir(os.getcwd()+"\\"+d) == False:
				print(d)
		print("")		
	elif r == "2":
		for d in os.listdir(os.getcwd()):
			if os.path.isdir(os.getcwd()+"\\"+d) != False:
				print(d)
		print("")	
	elif r == "3":
		i=0
		p=[""]
		for d in os.listdir(os.getcwd()):
			if os.path.isdir(os.getcwd()+"\\"+d) == False:
				i += 1
				print(i,d)
				p.append(d)
	
		print("")			
		t=input("輸入引索")
		print("==================檔案開始==================")
		q = codecs.open(p[int(t)] , "r" , "utf8" )
		print(q.read()) 
		q.close()
		print("==================檔案結束==================")
		print("")

	elif r == "4":
		i=0
		p=[]
		for d in os.listdir(os.getcwd()):
			if os.path.isdir(os.getcwd()+"\\"+d)==False:
				print(i,d)
				p.append(d)
				i+=1
		print("")
		t=input("請輸入引索")
		if os.path.exists(p[int(t)]):
			os.remove(p[int(t)])
			os.system("cls")

	elif r == "5":
		i=0
		p=[""]
		for d in os.listdir(os.getcwd()):
			if os.path.isdir(os.getcwd()+"\\"+d)==False:
				i+=1
				print(i,d)
				p.append(d)
		t = input("請輸入引索")
		os.system("start " + p[int(t)])
		print("")

	elif r == "6":
		i=0
		p=[""]
		for d in os.listdir(os.getcwd()):
			if os.path.isdir(os.getcwd()+"\\"+d) != False:
				i += 1
				print(i,d)
				p.append(d)
				
		print("")	

		t = input("請輸入引索")
		print("")
		os.chdir(os.getcwd()+"\\"+p[int(t)])
		os.system("cls")

		# for d2 in os.listdir(os.getcwd()):
		# 	print("============")
		# 	print(d2)
		# 	print("")


			
	elif r == "7":
		i=0
		p=[""]
		for d in os.listdir(os.getcwd()):
			if os.path.isdir(os.getcwd()+"\\"+d)!=False:
				i+=1
				print(i,d)
				p.append(d)
				
		print("")
		t=input("請輸入引索")
		if os.path.exists(p[int(t)]):
			os.rmdir(p[int(t)])
			os.system("cls")


	elif r == "8":
		x = os.path.dirname(os.getcwd())
		os.chdir(x)
		print("")



	print("工作路徑:"+os.getcwd())
	print("(0)","離開程式")
	print("(1)","列出檔案")
	print("(2)","列出資料夾")
	print("(3)","顯示檔案內容")
	print("(4)","刪除檔案")
	print("(5)","執行檔案")
	print("(6)","進入資料夾")
	print("(7)","刪除資料夾")
	print("(8)","回上層目錄")
	r = input("操作:")
	
	


