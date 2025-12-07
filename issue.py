from connection import connection
import datetime

def issue_book(book_id,member_id):
    with connection() as con:
        cur = con.cursor()
        cur.execute("select available from books where book_id=:id",{':id':book_id})
        row = cur.fetchone()
        print(row)
        if not row:
            print("Book not available")
            cur.close()
            return
        if row[0]!='Yes':
            print("Book not Found")
            cur.close()
            return
        cur.execute("insert into issue (book_id,member_id,issue_date) values (:book_id,:member_id,SYSDATE)",{':book_id':book_id,':member_id':member_id})
        cur.execute("update books set available='No' where book_id=:id", {':id': book_id})
        con.commit()
        print("Issue Inserted")
        cur.close()
#issue_book(int(input("enter the book id: ")),int(input("enter the member id:")))


def return_book(issue_id):
    with connection() as con:
        cur = con.cursor()
        cur.execute("select book_id,return_date from issue where issue_id=:id",{':id':issue_id})
        row = cur.fetchone()
        if not row:
            print("Issue not returned")
            cur.close()
            return
        if row[1] is None:
            print("Book not returned")
        else:
            print(row)
            cur.close()
            return
        cur.execute("update issue set return_date=SYSDATE where issue_id=:id",{':id':issue_id})
        book_id=int(input("enter the book id: "))
        cur.execute("update books set available='Yes' where book_id=:id",{':id':book_id})
        con.commit()
        print('Book returned')
        cur.close()


def list_issues(not_returned):
    with connection() as con:
        cur = con.cursor()
        if not_returned=='yes':
            cur.execute("""select i.issue_id,i.book_id,b.title,i.member_id,m.name,i.issue_date from issue i
                         join books b on i.book_id=b.book_id 
                         join members m on m.member_id=i.member_id 
                         where i.return_date is null 
                         order by i.issue_date""")
            row = cur.fetchall()
            return row
            cur.close()
        else:
            cur.execute("""select i.issue_id,i.book_id,b.title,i.member_id,m.name,i.issue_date,i.return_date from issue i
                           join books b on i.book_id=b.book_id 
                           join members m on m.member_id=i.member_id 
                           order by i.issue_date""")
            rows = cur.fetchall()
            return rows
            cur.close()

