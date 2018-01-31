import pymysql

database = pymysql.connect("127.0.0.1", "root", "ivanl48265", "test")

cursor = database.cursor()

# 1， 查询数据库版本
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database version : %s " % data)

# 2，查询数据, 一条或者多条
cursor.execute("select * from py_student")
# data = cursor.fetchmany(2)
data = cursor.fetchall()
print(data)

# 3, 插入一条数据
# try:
#     rows = cursor.execute('insert into py_student (name, age, num, words) values ("ivanl004", "80", "22222222", "Never say never")')
#     database.commit()
# except:
#     database.rollback()
# print(rows)

# 4, 更新数据
sqlStr = "UPDATE py_student SET num = '%s' where age < 60" % ('10120945')
try:
   # 执行SQL语句
   rows = cursor.execute(sqlStr)
   # 提交到数据库执行
   database.commit()
except:
   # 发生错误时回滚
   database.rollback()
print(rows)


database.close()