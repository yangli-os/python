import pymysql
db = pymysql.Connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       passwd = 'Nc1952',
                       db = 'heartdiag',
                       charset='utf8')

cursor = db.cursor() #创建一个游标
# 创建游标对象
print("connect success")
truncateTable = 'truncate table all_chs'        #链接数据库表
cursor.execute(truncateTable)
db.commit()
insertSql = "insert into all_chs (ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch17,ch18,ch19,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch29,ch30,ch31,ch32,ch33,ch34,ch35,ch36) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
cursor.execute((insertSql),(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1,2,3,4))
cursor.close()      #关闭游标和数据库
db.commit()
db.close()