import oracledb as orc
def connection():
    con = orc.connect("System/Dhone_518@localhost/orcl")
    print("connected")
    return con
connection()