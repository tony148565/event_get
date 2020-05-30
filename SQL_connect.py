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
    print(query)  # 字串 = %s 數字 = %d
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
    #print(type(result))
    #print(result)
    return result



# id目前的使用狀況，要用前記得+=1


def insertdata(push_main, push_add, push_book):
    #print("run!!")
    #idflag = {"activityID": 3, "bookingID": 0, "addressID": 0}
    #idflag["activityID"] += 1
    push_main['activityID'] = check_main(push_main)
    push_add['addressID'] = check_add(push_add)
    push_main['addressID'] = push_add.get('addressID')
    push_book['bookingID'] = check_booking(push_book)
    push_main['bookingID'] = push_book.get('bookingID')
    if final_check('ActivityMain', push_main.get('activityID')):
        insertIntoDatabase("ActivityMain", push_main)
    if final_check('Address', push_main.get('addressID')):
        insertIntoDatabase("ActivityMain", push_main)
    if final_check('Booking', push_main.get('bookingID')):
        insertIntoDatabase("ActivityMain", push_main)
    #dic = {"activityID": idflag["activityID"], "name": "測試", "activityURL": "https://...", "startDate": "2020-01-01", "endDate": "2020-01-01"}
    #insertIntoDatabase("ActivityMain", dic)
    #select("ActivityMain")
    # 確認執行
    conn.commit()


def check_main(push):
    listd = select("ActivityMain")
    print(len(listd))
    for i in listd:
        if i[1] == push.get('name'):
            return i[0]
    return len(listd)+1


def check_add(push):
    lista = select("Address")
    print(len(lista))
    for i in lista:
        if i[1] == push.get('eastLongitude') and i[2] == push.get('northLatitude'):
            return i[0]
    return len(lista)+1


def check_booking(push):
    listb = select("Booking")
    for i in listb:
        if i[1] == push.get('bookingURL'):
            return i[0]
    return len(listb)+1


def final_check(table, uid):
    listd = select(table)
    if uid < len(listd):
        return False
    else:
        return True
