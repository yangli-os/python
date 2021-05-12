import pymysql
from dbutils.pooled_db import PooledDB
import traceback
from threading import Thread


# 基础类
class mysql_pool:
    """
    用于连接和关闭
    """

    def __init__(self):
        self.pool = self.create_pool()

    def create_pool(self):
        """
        创建数据库连接池
        :return: 连接池
        """
        pool = PooledDB(creator=pymysql,
                        maxconnections=0,  # 连接池允许的最大连接数，0和None表示不限制连接数
                        mincached=4,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
                        maxcached=0,  # 链接池中最多闲置的链接，0和None不限制
                        maxusage=1,  # 一个链接最多被重复使用的次数，None表示无限制
                        blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待:True，等待:False，不等待然后报错
                        host='localhost',
                        port=3306,
                        user='root',
                        passwd='Nc1952',
                        db='heartdiag',
                        use_unicode=True,
                        charset='utf8')
        return pool

    def save_mysql(self, sql, args):
        """
        保存数据库
        :param sql: 执行sql语句
        :param args: 添加的sql语句的参数 list[tuple]
        """
        try:
            db = self.pool.connection()  # 连接数据池
            cursor = db.cursor()  # 获取游标
            # insertSql = "insert into all_chs (ch17,ch18,ch19,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch29,ch30,ch31,ch32) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            cursor.execute(sql, args)
            db.commit()
            cursor.close()
            db.close()
        except:
            traceback.print_exc()

if __name__ == "__main__":
    insert = insertSql = "insert into all_chs (ch17,ch18,ch19,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch29,ch30,ch31,ch32) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
    data = (17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)
    A = mysql_pool()
    A.save_mysql(insert, data)