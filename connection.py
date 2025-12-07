import oracledb as orc
def connection():
    con = orc.connect("Username/Password@DNS")
    print("connected")
    return con

connection()
