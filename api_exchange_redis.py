from fastapi import FastAPI
import pymysql
import logging
import datetime
import configparser
import redis
#http://192.168.20.46:8080/plot?val=USD&start_date=20240610&end_date=20240715
logging.basicConfig(filename='exchange.log', level=logging.DEBUG)
def get_valute_rate(connection, cursor, valute):
    if valute == "RUB" or valute == "RUR":
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


def connect_to_redis(redis_host, redis_port, redis_password):
    redis_connection = redis.StrictRedis(host=redis_host, port=redis_port)
    return redis_connection


def get_from_redis(redis_connection, valute):
    valute_rate = (redis_connection.get(valute))
    if valute_rate:
        valute_rate = float(valute_rate.decode())
        return valute_rate
    else:
        return False

def set_to_redis(redis_connection, valute, valute_rate, redis_cache_time):
    redis_connection.set(valute, str(valute_rate), ex=redis_cache_time)
    return True


def get_data_from_config():
    config = configparser.ConfigParser()
    config.read('exchange_redis.conf')
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
    redis_port = int(config['redis']['redis_port'])
    redis_pass = config['redis']['redis_password']
    redis_host = config['redis']['redis_host']
    redis_cache_time = int(config['redis']['redis_cache_time'])
    return db_host, db_user, db_password, db_name, db_port, redis_port, redis_pass, redis_host, redis_cache_time

app = FastAPI()

@app.get("/plot")
def plot(val, start_date, end_date, token):
    if token == "123456":
        db_host, db_user, db_password, db_name, db_port, _, _, _, _ = get_data_from_config()
        connection, cursor = connect_to_db(db_host, db_user, db_password, db_name, db_port)
        select_str = f'SELECT date,rate from currency_exchange_rate WHERE valute = "{val}" and `date` BETWEEN "{start_date}" AND "{end_date}"'
        cursor.execute(select_str)
        points = cursor.fetchall()
        return points
    else:
        return "unauthorized"
@app.get("/obmen/")
def obmen(val1, val2, count, token):
    if token == "123456":
        in_valute = val1
        out_valute = val2
        in_valute_count = int(count)
        db_host, db_user, db_password, db_name, db_port, redis_port, redis_pass, redis_host, redis_cache_time = get_data_from_config()
        redis_connection = connect_to_redis(redis_host, redis_port, redis_pass)
        in_valute_rate = get_from_redis(redis_connection, in_valute)
        out_valute_rate = get_from_redis(redis_connection, out_valute)
        if in_valute_rate and out_valute_rate:
            out_valute_count = exchange_valute(in_valute_rate, out_valute_rate, in_valute_count)
        else:
            connection, cursor = connect_to_db(db_host, db_user, db_password, db_name, db_port)
            in_valute_rate = get_valute_rate(connection, cursor, in_valute)
            out_valute_rate = get_valute_rate(connection, cursor, out_valute)
            connection.close()
            set_to_redis(redis_connection, in_valute, in_valute_rate, 3600)
            set_to_redis(redis_connection, out_valute, out_valute_rate, 3600)
            out_valute_count = exchange_valute(in_valute_rate, out_valute_rate, in_valute_count)
        return f'Вы получите {out_valute_count} {out_valute}. '
    else:
        return "unauthorized"