import pymysql
'''连接数据库，包括数据库ip、端口、用户名、密码、数据库'''
conn =pymysql.connect(host='localhost',user='root',passwd='Nc1952',db='heartdiag',port=3306,charset='utf8')  #password为具体的密码，database为要链接的具体数据库
'''创建游标'''
cur =conn.cursor()
i = 1
while i <= 100:
    insertSql = "insert into all_chs (ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9,ch10,ch11,ch12,ch13,ch14,ch15,ch16,ch17,ch18,ch19,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch29,ch30,ch31,ch32,ch33,ch34,ch35,ch36) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    cur.execute((insertSql), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 2, 3, 4))
    conn.commit()
    i += 1
print("已经插入完成")
cur.close()
conn.close()