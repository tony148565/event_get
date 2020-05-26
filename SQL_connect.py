# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#pymysql套件

import pymysql
Endpoint = "db-testing.csvceebtmmcx.ap-northeast-1.rds.amazonaws.com"
port = 3306
dbname = "activity"
user = "admin"
password = "321password"
conn = pymysql.connect(
        host=Endpoint, user=user, port=port, passwd=password, db=dbname, charset="utf8mb4")
print("....")

#建立操作游標
course = conn.cursor()
#SQL語法（查詢資料庫版本）
sql = 'SELECT VERSION()'
#執行語法
course.execute(sql)
#選取第一筆結果
data = course.fetchone()

print ("Database version : %s " % data)
#關閉連線
conn.close()


#MySQLdb套件
"""
import MySQLdb
conn = MySQLdb.connect(host="db-testing.csvceebtmmcx.ap-northeast-1.rds.amazonaws.com", 
                       user="admin",
                       passwd="321password",
                       db="activity")
# 欲查詢的 query 指令
query = "SELECT * FROM ActivityMain"#.format(#my_head)
# 執行查詢
cursor = conn.cursor()
cursor.execute(query)
#印出結果
print(cursor.fetchall())
"""