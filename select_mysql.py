# coding:utf-8
import MySQLdb as mdb

# 将con设为全局连接
con = mdb.connect('localhost', 'root', 'xzj123', 'webpy',charset = 'utf8')

with con:

    # 第一步仍是获取连接的cursor游标对象，用于执行查询
    cur = con.cursor()
    #类似与其他语言的query函数，execute是python中的执行查询函数
    cur.execute("SELECT * FROM study WHERE dz LIKE '%北京%'")

    #使用fetchall函数，将结果集（多维元组）存入rows里面
    rows = cur.fetchall()
    # print rows
    # print type(rows)
    for row in rows:
        # print type(row)
        # for item in row:
        #     print item
        print row[0],row[1],row[2],row[3],row[4]