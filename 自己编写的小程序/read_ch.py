#读取heartdiag数据库表all_chs全部数据
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
cursor.execute("select * from all_chs")
des = cursor.description
print("表的描述:", des)
# data = cursor.fetchall()  # 全量查询结果
# print(des)

