import pymysql

connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test', port=33306)
cursor = connection.cursor()

data = cursor.execute('select name, phone from telsprav')

data = cursor.fetchall()

connection.close()

telsprav = {}

for element in data:
    print(element)
    # telsprav []
    name = element[0]
    phone = element[1]
    telsprav[name] = phone

print(telsprav)

while True:
    username = input('Введите имя абонента').capitalize()    #.capitalize() писать можно имя и с маленькой и с большой буквы
    phone = telsprav.get(username, 'не найден')
    print(f'телефон абонента {username} - {phone}')