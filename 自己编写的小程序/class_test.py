import time

############数据库操作###########################################
import pymysql
db = pymysql.Connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       passwd = '123456',
                       db = 'database',)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
class Equip_control():
    def __init__(self, EQUIE_ON,parent=None):
        if EQUIE_ON == 1:
            while True:
                insertSql = "insert into all_chs (ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch17,ch18,ch19,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch29,ch30,ch31,ch32,ch33,ch34,ch35,ch36) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
                cursor.execute((insertSql), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1,2, 3, 4))
                db.commit()
        else:
            return
print("完成")
cursor.close()  # 关闭游标和数据库
db.close()
