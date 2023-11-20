import pymysql

while True:
    connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test', port=33306)
    cursor = connection.cursor()
    username = input('Введите имя абонента ')
    cursor.execute(f'SELECT name , phone from telsprav WHERE name = "{username}"')
    connection.close()
    data = cursor.fetchall()
    #print (data)
    #print(len(data))  #len длина данных. без нее будет ошибка   print(data[0].....

    #if  len(data) > 0:
        #print(data[0][0],data[0][1])

    if  len(data) > 0:
        name = data[0][0]
        phone = data[0][1]
        print(f'телефон абонента {username} - {phone}')
    else:
        print(f'телефон абонента {username} - не найден')
