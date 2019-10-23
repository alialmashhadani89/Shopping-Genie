import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ss1517",
    passwd="passtext",
    database="shopping_genie"
)


# ============
# Result Table
# ============
# result param:  Important details parsed from an item page
# NOTE: qid is always set to "1" for the time being.
def insertOneIntoResultTable(result):

    mycursor = mydb.cursor(buffered=True)

    sid = findSellerIdByName(result["seller"])
    print(sid)
    if sid != None:
        result["seller"] = sid[0]
    else:
        insertOneIntoSellerTable(result["seller"])
        result["seller"] = findSellerIdByName(result["seller"])[0]

    bid = findBrandIdByName(result["brand"])
    print(bid)
    if bid != None:
        result["brand"] = bid[0]
    else:
        insertOneIntoBrandTable(result["brand"])
        result["brand"] = findBrandIdByName(result["brand"])[0]


    print(result["price"])
    
    sql = "INSERT INTO results(price, url, name, image_link, bid, sid, qid) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    val = (result["price"], result["url"], result["item_name"], result["image_link"], result["brand"], result["seller"], "7",)
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

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
    print(mycursor.rowcount, "record inserted.")

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
    print(mycursor.rowcount, "record inserted.")

def findBrandIdByName(name):
    mycursor = mydb.cursor(buffered=True)
    
    sql = "SELECT id FROM brands WHERE name = %s;"
    val = (name, )

    mycursor.execute(sql, val)
    mydb.commit()

    return mycursor.fetchone()
