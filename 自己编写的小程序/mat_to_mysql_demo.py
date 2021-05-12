import scipy.io as scio
import pymysql

############数据库操作###########################################
import pymysql
db = pymysql.Connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       passwd = '123456',
                       db = 'database',)
# 使用cursor()方法获取操作游标
cursor = db.cursor()
dataFile = r'.\data.mat'            #同级目录下的相对路径
data = scio.loadmat(dataFile)
print(data.keys())
data_set = data["Bz"]

insert_number = 1000                #设置单次写入数据库的数据量
for col_num in range(0, len(data_set), insert_number):
    # 获得单行的16个数据，转换成元组列表
    insert_val = []
    for col_simple in range(insert_number):
        val_simple = (tuple(data_set[col_num:col_num+insert_number][col_simple]))
        insert_val.append(val_simple)
    insertSql = "insert into all_chs (ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9,ch10,ch11,ch12,ch13,ch14,ch15,ch16) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    cursor.executemany(insertSql, insert_val)
    db.commit()
    # print("success")
cursor.close()
db.close()
