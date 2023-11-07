import pymysql
f = open("users.txt", "r")

for line in f:
    line = line.strip()
    split_line = line.split(":")
    name = split_line[0]
    surname = split_line[1]
    sex = split_line[2]
    phone = split_line[3]
f.close()

connection = pymysql.connect(host='10.10.101.161', user='pyuser', password='123456', database='test')

cursor = connection.cursor()

cursor.execute(f'insert into telsprav values("{name}","{surname}","{sex}","{phone}")')
connection.commit()
