# coding:utf-8
import MySQLdb as mdb
import sys

# 将con设为全局连接
con = mdb.connect('localhost', 'root', 'xzj123', 'webpy',charset = 'utf8')

with con:

    # 第一步仍是获取连接的cursor游标对象，用于执行查询
    cur = con.cursor()
    #类似与其他语言的query函数，execute是python中的执行查询函数
    cur.execute("delete FROM study WHERE dz LIKE '%北京%'")