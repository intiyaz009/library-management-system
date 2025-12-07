from connection import connection
def add_books(title,author,category):
    with connection() as con:
        cur = con.cursor()
        cur.execute("Insert into books (title,author,category) values(:title,:author,:category)",{':title':title,':author':author,':category':category})
        con.commit()
        print("Inserted")



def list_books(all_books):
    with connection() as con:
        cur = con.cursor()
        if all_books=='Yes':
            cur.execute("select * from books")
        else:
            cur.execute("select * from books where available='Yes' order by book_id")
        rows = cur.fetchall()
        cur.close()
        return rows


def get_book(book_id):
    con = connection()
    cur = con.cursor()
    cur.execute("select * from books where book_id=:id",{':id':book_id})
    row = cur.fetchone()
    print(row)

