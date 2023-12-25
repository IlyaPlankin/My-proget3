import requests
import pymysql
import datetime
import configparser
import logging
logging.basicConfig(filename = 'get_currency_rate.log', level = logging.DEBUG)


def get_data_from_config():
    config = configparser.ConfigParser()
    config.read('get_currency_rate.conf')
    db_host = config['database']['db_host']
    logging.debug(f'{datetime.datetime.now()} - Получил db_host - {db_host}')
    db_user = config['database']['db_user']
    logging.debug(f'{datetime.datetime.now()} - Получил db_user - {db_user}')
    db_password = config['database']['db_password']
    logging.debug(f'{datetime.datetime.now()} - Получил db_password - {db_password}')
    db_name = config['database']['db_name']
    logging.debug(f'{datetime.datetime.now()} - Получил db_name - {db_name}')
    db_port = int(config['database']['db_port'])
    logging.debug(f'{datetime.datetime.now()} - Получил db_port - {db_port}')
    cb_site = config['cb_site']['cb_site']
    logging.debug(f'{datetime.datetime.now()} - Получил cb_site - {cb_site}')
    return db_host, db_user, db_password, db_name, db_port, cb_site


def get_data_from_cb(site):
    proxies = {'https': 'http://192.168.39.46:3128', 'http': 'http://192.168.39.46:3128'}
    result = requests.get(site,proxies=proxies)

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
    try:
        logging.info(f'{datetime.datetime.now()} Начинаю читать данные из конфига')
        db_host, db_user, db_password, db_name, db_port, cb_site = get_data_from_config()
        logging.info(f'{datetime.datetime.now()} Данные из конфига прочитаны')

        logging.info(f'{datetime.datetime.now()} Начинаю получать данные из ЦБ')
        data = get_data_from_cb(cb_site)  # получил данные с сайта ЦБ в словарь
        logging.info(f'{datetime.datetime.now()} Данные из ЦБ получены')

        logging.info(f'{datetime.datetime.now()} Начинаю подключение к ДБ')
        connection, cursor = connect_to_db(db_host, db_user, db_password, db_name,
                                           db_port)  ## получили подключение и курсор к базе данных
        logging.info(f'{datetime.datetime.now()} Подключился к ДБ')

        logging.info(f'{datetime.datetime.now()} Начинаю вносить данные в ДБ')
        put_result = put_data_to_db(connection, cursor, data)  # положили данные в базу
        logging.info(f'{datetime.datetime.now()} Данные в ДБ внесены')
        print(put_result)
    except ConnectionRefusedError as cre:
        logging.critical(f'{datetime.datetime.now()} Не удалось подключиться: {cre}')
    except pymysql.err.OperationalError as poe:
        logging.critical(f'{datetime.datetime.now()} Ошибка sql: {poe}')
    except requests.exceptions.ConnectionError as rce:
        logging.critical(f'{datetime.datetime.now()} Не удалось подключиться к сайту ЦБ: {rce}')
    except KeyError as ke:
        logging.critical(f'{datetime.datetime.now()} Ошибка ключа: {ke}')