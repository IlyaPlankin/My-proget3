import pymysql

connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test', port=33306)
cursor = connection.cursor()

cursor.execute('select * from telsprav')

data = cursor.fetchall()

f = open('users2.txt', 'w')

for elem in data:
    name = elem[0]
    surname = elem[1]
    sex = elem[2]
    phone = elem[3]
    user = f'{phone};{sex};{surname};{name}'
    f.write(user + '\n')

data_1 = True

while data_1 == True:
    try:
        name = input("Введите имя: ")
        print(f'Телефон абонента {elem[3]}')
        data_1 = False
    except KeyError:
        print(f'Телефон абонента {name} - не найден')
