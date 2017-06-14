# coding:utf-8
import MySQLdb as mdb

# 将con设为全局连接
con = mdb.connect('localhost', 'root', 'xzj123', 'webpy',charset = 'utf8')

with con:

    # 获取连接的cursor,只有获取了cursor才能进行各种操作      获取操作游标
    cur = con.cursor()
    # 创建一个数据表 writerd(id,name)
    # cur.execute('CREATE TABLE IF NOT EXISTS\
    #             Writers(Id INT  PRIMARY KEY AUTO_INCREMENT,Name VARCHAR (25))')
    # 以下插入了5条数据
    cur.execute("INSERT INTO study(dwmc,dz,tel,jianjie) VALUES('振杰之家','HOME','186052','python learning')")
    cur.execute("INSERT INTO study(dwmc,dz,tel,jianjie) VALUES('ABC','北京','010','java')")
    cur.execute("INSERT INTO study(dwmc,dz,tel,jianjie) VALUES ('BAT','中国','001','net')")

