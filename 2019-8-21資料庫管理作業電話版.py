import pymysql
import os
import prettytable

conn=pymysql.connect(
host="localhost", #從其他地方存取要找到IP位置
user="root",      #選擇資料庫>按上方的伺服器>選擇使用者帳號
passwd="",        #密碼,顯示否則為空
db="python_ai_2018",    #資料庫名稱
charset="utf8"    #編碼類型
)

cmd=conn.cursor()


#進度提示:SELECT * FROM `member` LEFT JOIN `tel` ON `member`.`id` =`tel`.`member_id`

i=-1
while i != "0":

    if i == "1":
        pt=prettytable.PrettyTable(['編號','名子','生日','地址'], encoding='utf8')
        # pt.add_row(['AAA','1212-12-12','AAA'])
        cmd.execute("SELECT * FROM `member`")
        x=cmd.fetchall()
        for i in x:
            pt.add_row (i)                                                           #i數值已是串列
            # print("")
            pt.align['名子','生日','座號']="c"
        print(pt)
        
    elif i == "2":
        pt=prettytable.PrettyTable(['編號','名子','生日','地址'], encoding='utf8')
        cmd.execute("SELECT * FROM `member`")
        x=cmd.fetchall()
        for i in x:
            pt.add_row (i)   
            pt.align['名子','生日','座號']="c"
        print(pt)

        name = input("請輸入姓名")
        birthday = input("請輸入生日"+"格式:西元年-月-日")
        address = input("請輸入地址")

        cmd.execute(
            "INSERT INTO `member`(`name`,`birthday`,`address`) VALUES(%s,%s,%s)",       #%s不用用引號括起來
            (name,birthday,address)
        )   #指令操作變數.execute(SQL指令, 要帶入SQL中的變數)
        conn.commit()
        


    elif i == "3":
        pt=prettytable.PrettyTable(['編號','名子','生日','地址'], encoding='utf8')
        cmd.execute("SELECT * FROM `member`")
        x=cmd.fetchall()
        for i in x:
            pt.add_row (i)   
            pt.align['名子','生日','座號']="c"
        print(pt)
        x = input("請輸入要修改的ID")
        print("(1) 修改姓名")
        print("(2) 修改生日")
        print("(3) 修改地址")
        y = input("操作")
        if y == "1" :
            NewName = input("新名子")
            cmd.execute(
                "UPDATE `member` SET `name`=%s where `id`= %s",(NewName,x)
            )
        if y == "2" :
            NewBirthday = input("新生日")
            cmd.execute(
                "UPDATE `member` SET `birthday`=%s where `id`= %s",(NewBirthday,x)
           
            )
        if y == "3" :
            NewAddress = input("新地址")
            cmd.execute(
                "UPDATE `member` SET `address` = %s where `id`= %s",(NewAddress,x)
            )
        conn.commit()
       

    elif i == "4":
        pt=prettytable.PrettyTable(['編號','名子','生日','地址'], encoding='utf8')
        cmd.execute("SELECT * FROM `member`")
        x=cmd.fetchall()
        for i in x:
            pt.add_row (i)   
            pt.align['名子','生日','座號']="c"
        print(pt)
        x = input("請輸入要刪除的ID")
        cmd.execute(
            "delete  from `member` where `id`= %s",(x)
        )
        conn.commit()
        
    else:
        print("請輸入數字0-4")
    
    print("(0) 離開程式")
    print("(1) 顯示會員列表")
    print("(2) 新增會員資料")
    print("(3) 更新會員資料")
    print("(4) 刪除會員資料")
    i = input("操作")
    os.system("cls")


conn.close()      #關閉連線,否則會無法釋放資源