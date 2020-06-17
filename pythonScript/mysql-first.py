import pymysql

# 链接数据库,并执行语句.
conn = pymysql.connect(host='47.107.177.108',user = "root", passwd="root", db="hchat", port=8806, charset="utf8")
cur = conn.cursor()
cur.execute("select * from tb_user")
users = cur.fetchall()
for i in range(len(users)):
    print(users[i])


