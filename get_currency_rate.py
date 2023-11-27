
import requests
import pymysql
import datetime


def get_data_from_cb(site):
    result = requests.get(site)
    valites = result.json()
    valutes_raw_dict = valites['Valute']
    clean_valute_dict = {}
    for val in valutes_raw_dict:
        real_rate = valutes_raw_dict[val]['Value'] / valutes_raw_dict[val]['Nominal']
        clean_valute_dict[val] = round(real_rate, 3)
    return clean_valute_dict


def put_data_to_db(connection, cursor, data):
    today = datetime.datetime.today().strftime("%Y%m%d")
    # data
    # {"USD":"92","EUR":"101"}
    #
    for valute in data:
        rate = data[valute]
        insert_string = f'INSERT into currency_exchange_rate values("{valute}","{rate}","{today}")'
        # print(insert_string)
        cursor.execute(insert_string)
    connection.commit()
    connection.close()
    return "commit - OK"


def connect_to_db(host, user, password, database, port):
    connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
    cursor = connection.cursor()
    return connection, cursor


if __name__ == '__main__':
    db_host = 'nadejnei.net'
    db_user = 'student'
    db_password = '1q2w#E$R'
    db_name = 'test'
    db_port = 33306
    cb_site = 'https://www.cbr-xml-daily.ru/daily_json.js'

    data = get_data_from_cb(cb_site)  # получил данные с сайта ЦБ в словарь

    connection, cursor = connect_to_db(db_host, db_user, db_password, db_name,
                                       db_port)  ## получили подключение и курсор к базе данных
    put_result = put_data_to_db(connection, cursor, data) # положили данные в базу
    print(put_result)