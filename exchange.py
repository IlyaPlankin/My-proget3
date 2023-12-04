import pymysql
import logging
import datetime
import configparser

logging.basicConfig(filename='exchange.log', level=logging.DEBUG)


def get_valute_rate(connection, cursor, valute):
    if valute == "RUB" or valute =="RUR":
        return 1
    else:
        today = datetime.datetime.today().strftime("%Y%m%d")
        select_str = f'select rate from currency_exchange_rate where valute = "{valute}" and date = "{today}"'
        cursor.execute(select_str)
        data = cursor.fetchall()
        valute_rate = float(data[0][0])
        return valute_rate


def exchange_valute(in_valute_rate, out_valute_rate, in_valute_count):
    in_rubles = in_valute_rate * in_valute_count
    out_valute_count = in_rubles / out_valute_rate
    out_valute_count
    return round(out_valute_count, 3)


def connect_to_db(host, user, password, database, port):
    connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
    cursor = connection.cursor()
    return connection, cursor


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
    return db_host, db_user, db_password, db_name, db_port


if __name__ == '__main__':
    in_valute = input("Какую вылюту вы хотите обменять? ")
    out_valute = input("Какую вылюту вы хотите получить? ")
    in_valute_count = int(input("Сколько валюты вы хотите обменять! "))
    start_time = datetime.datetime.now()
    db_host, db_user, db_password, db_name, db_port = get_data_from_config()

    connection, cursor = connect_to_db(db_host, db_user, db_password, db_name, db_port)

    in_valute_rate = get_valute_rate(connection, cursor, in_valute)
    out_valute_rate = get_valute_rate(connection, cursor, out_valute)

    connection.close()
    out_valute_count = exchange_valute(in_valute_rate, out_valute_rate, in_valute_count)
    end_time = datetime.datetime.now()
    work_time = end_time - start_time
    print(f'Вы получите {out_valute_count} {out_valute}. ')
    print(work_time)