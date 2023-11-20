import pymysql

phone_cache = {}

while True:

    username = input('Введите имя абонента ').capitalize()
    phone = phone_cache.get(username, None)                  #работа со словарем
    if phone != None:
        print(f'телефон абонента {username} - {phone}')
        print('из словаря')

    else:
        connection = pymysql.connect(host='nadejnei.net', user='student', password='1q2w#E$R', database='test',
                                     port=33306)
        cursor = connection.cursor()
        cursor.execute(f'SELECT name , phone from telsprav WHERE name = "{username}"')
        connection.close()
        data = cursor.fetchall()
        #print(data)
        #print(len(data))                                      #работа с базой данных
        if len(data) > 0:
            name = data[0][0]
            phone = data[0][1]
            print(f'телефон абонента {username} - {phone}')
            print('из базы данных')
            phone_cache[username] = phone
        else:
            print(f'телефон абонента {username} - не найден')
