import mysql.connector
from db_credentials import getCredentials
from ai_prediction import get_redication_price

creds = getCredentials()
mydb = mysql.connector.connect(
    host=creds["host"],
    user=creds["user"],
    passwd=creds["passwd"],
    database=creds["database"]
)


# =
# ============
# Result Table
# ============
# result param:  Important details parsed from an item page
# NOTE: qid is always set to "1" for the time being.
def insertOneIntoResultTable(result):

    mycursor = mydb.cursor(buffered=True)

    sid = findSellerIdByName(result["seller"])
    if sid != None:
        result["seller"] = sid[0]
    else:
        insertOneIntoSellerTable(result["seller"])
        result["seller"] = findSellerIdByName(result["seller"])[0]

    bid = findBrandIdByName(result["brand"])
    if bid != None:
        result["brand"] = bid[0]
    else:
        insertOneIntoBrandTable(result["brand"])
        result["brand"] = findBrandIdByName(result["brand"])[0]

    sql = "INSERT INTO results(price, url, name, image_link, bid, sid, qid) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    val = (result["price"], result["url"], result["item_name"],
           result["image_link"], result["brand"], result["seller"], "1",)
    mycursor.execute(sql, val)

    mydb.commit()
    #print(mycursor.rowcount, " Result record inserted.")

# Make InsertMany for Result


def findResultsByQueryId(query_id):
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * FROM results WHERE q_id = %s;"
    val = (query_id, )
    mycursor.execute(sql, val)

    mydb.commit()

    output = mycursor.fetchall()

    for x in output:
        print(x)


def findResultPricesByQueryId(query_id):
    print("bottom text")

# ===========
# Query Table
# ===========


def insertOneIntoQueryTable(query):
    mycursor = mydb.cursor(buffered=True)

    sql = "INSERT INTO queries (search_term) VALUES (%s);"
    val = (query["search_term"])
    mycursor.execute(sql, val)

    mydb.commit()
    #print(mycursor.rowcount, " Query record inserted.")

# ============
# Seller Table
# ============


def insertOneIntoSellerTable(seller):
    mycursor = mydb.cursor(buffered=True)

    sql = "INSERT INTO sellers (name) VALUES (%s);"
    val = (seller, )
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def findSellerIdByName(name):
    mycursor = mydb.cursor(buffered=True)

    sql = "SELECT id FROM sellers WHERE name = %s;"
    val = (name, )

    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.fetchone()

# =====
# Brand Table


def insertOneIntoBrandTable(brand):
    mycursor = mydb.cursor(buffered=True)

    sql = "INSERT INTO brands (name) VALUES (%s);"
    val = (brand, )
    mycursor.execute(sql, val)

    mydb.commit()
    #print(mycursor.rowcount, "record inserted.")


def findBrandIdByName(name):
    mycursor = mydb.cursor(buffered=True)

    sql = "SELECT id FROM brands WHERE name = %s;"
    val = (name, )

    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.fetchone()
# to get the result to the backend


def get_results(term=' '):
    cursor = mydb.cursor(buffered=True)
    term = term.replace(' ', '%')
    dataQuery = """
        SELECT r.image_link as image, b.name as brand, r.name as itemName, 0 as predictionPrice,\
        max(DATE_FORMAT(date,'%Y-%m-%d')) as todayDateTable,\
        DATE_FORMAT(NOW()+ INTERVAL 30 DAY, '%Y-%m-%d %T.%f') as predictionDate, concat('$', min(r.price))  as itemPrice,\
        s.name as storeName, r.url as storeLink\
        FROM results r join sellers s on r.sid = s.id join brands b on r.bid = b.id\
        and r.price in (select min(price) from results where name like concat('%',%s,'%') group by sid)\
        or DATE_FORMAT(date,'%Y-%m-%d') in (select max(DATE_FORMAT(date,'%Y-%m-%d')) from results where r.bid = b.id group by r.sid)\
        WHERE r.name like concat('%',%s,'%')\
        group by s.name;
        """
    val = (term, term,)

    cursor.execute(dataQuery, val)

    columns = cursor.description

    cursor.close()

    return [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]


def get_data_ai(term=' '):
    cursor = mydb.cursor(buffered=True)
    term = term.replace(' ', '%')
    dataQuery2 = "select r.price as price ,s.name as name from results r join sellers s on r.sid = s.id where r.name like concat('%',%s,'%') order by s.name;"
    val = (term,)
    cursor.execute(dataQuery2, val)
    table_rows = cursor.fetchall()
    sql2 = "select price from results where name like concat('%',%s,'%') order by id desc limit 30;"
    cursor.execute(sql2, val)
    future_prices = cursor.fetchall()
    cursor.close()
    return get_redication_price(table_rows, future_prices)
