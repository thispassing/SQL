import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows
    # rows is returned as a python list

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

# def update(quantity,price,item):
#     conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
#     cur=conn.cursor()
#     cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
#     conn.commit()
#     conn.close()

def update(item,price,quantity):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5433'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET item=%s, price=%s WHERE quantity=%s",(item,price,quantity))
    conn.commit()
    conn.close()

create_table()
#insert("Bananas",8,42.00)
#delete("Apple")
#update('Oranges',35,16)
print(view())

# insert("Coffee Cup",10,5)
# update(10,5.99,"Water Pipe")
# delete("Coffee Cup")
# print(view())