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
    push_main['activityID'] = check_main(push_main)
    push_add['addressID'] = check_add(push_add)
    push_main['addressID'] = push_add.get('addressID')
    push_book['bookingID'] = check_booking(push_book)
    push_main['bookingID'] = push_book.get('bookingID')

    if final_check('Address', push_main.get('addressID')):
        push_add['addressID'] = str(check_add(push_add))
        insertIntoDatabase("Address", push_add)
    if final_check('Booking', push_main.get('bookingID')):
        push_book['bookingID'] = str(check_booking(push_book))
        insertIntoDatabase("Booking", push_book)
    if final_check('ActivityMain', push_main.get('activityID')):
        push_main['activityID'] = str(push_main.get('activityID'))
        push_main['addressID'] = str(push_add.get('addressID'))
        push_main['bookingID'] = str(push_book.get('bookingID'))
        insertIntoDatabase("ActivityMain", push_main)

    # 確認執行
    conn.commit()


def check_main(push):
    listd = select("ActivityMain")
    #print("ActivityMain")
    #print(len(listd))
    #print(listd)
    for i in listd:
        if i[1] == push.get('name'):
            print("same event")
            return i[0]
    return len(listd)+1


def check_add(push):
    lista = select("Address")
    #print("Address")
    #print(len(lista))
    for i in lista:
        if i[5] == push.get('fullAddress'):
            print("same address")
            return i[0]
    return len(lista)+1


def check_booking(push):
    listb = select("Booking")
    #print("Booking")
    #print(len(listb))
    for i in listb:
        if i[1] == push.get('bookingURL'):
            print("same url")
            return i[0]
    return len(listb)+1


def final_check(table, uid):
    listd = select(table)
    print(type(uid))
    print(uid)
    uuid = int(uid)
    if uuid <= len(listd):
        return False
    else:
        return True
