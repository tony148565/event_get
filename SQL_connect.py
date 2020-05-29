#MySQLdb套件
import MySQLdb
conn = MySQLdb.connect(host="db-testing.csvceebtmmcx.ap-northeast-1.rds.amazonaws.com",
                       user="admin",
                       passwd="321password",
                       db="activity",
                       charset="utf8")


def insertIntoDatabase(table, dataDic):
    """
    將資料輸入到指定的table裡
    輸入要新增資料的table跟字典型態的輸入資料
    會直接新增資料至table中
    """
    # 欲查詢的 query 指令
    query = "Insert into " + table + " ("
    for colunm in dataDic.keys():
        query += colunm
        query += ", "
    query = query[:-2]
    query += ") values ("
    val = []
    for colunm in dataDic.values():
        if colunm != "number" and colunm != "price":
            val.append(colunm)
            query += "%s, "
        else:
            val.append(colunm)
            query += "%d, "
    query = query[:-2]
    query += ");"
    print(query)#字串 = %s 數字 = %d
    print(val)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query, tuple(val))


    #印出結果
    print(cursor.rowcount, "record inserted.")


def select(table):
    """印出table裡的所有資料"""
    # 欲查詢的 query 指令
    query = "SELECT * FROM " + table
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)


#id目前的使用狀況，要用前記得+=1
idFlag = {"activityID": 1, "bookingID": 0, "addressID": 0}
idFlag["activityID"] += 1
dic = {"activityID": idFlag["activityID"], "name": "測試", "activityURL": "https://...", "startDate": "2020-01-01", "endDate": "2020-01-01"}
insertIntoDatabase("ActivityMain", dic)
select("ActivityMain")
#確認執行
conn.commit()