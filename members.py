from connection import connection
def add_members(name,phone):
    with connection() as con:
        cur = con.cursor()
        cur.execute("Insert into members (name,phone) values(:name,:phone)",{':name':name,':phone':phone})
        con.commit()
        print('inserted')


def memberdetail(member_id):
    with connection() as con:
        cur = con.cursor()
        cur.execute("select * from members where member_id=:id",{':id':member_id})
        row = cur.fetchone()
        print(row)
