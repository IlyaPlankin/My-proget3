import read_from_file.py

connection = pymysql.connect(host='10.10.101.161', user='pyuser', password='123456', database='test')

cursor = connection.cursor()

cursor.execute(f'insert into telsprav values("{name}","{surname}","{sex}","{phone}")')
connection.commit()
