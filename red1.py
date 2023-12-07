import redis

r = redis.StrictRedis(host='nadejnei.net', port = 16379, password='123456')
r.set('kirill', '89110271345',ex=20)
result = r.get('kirill')

print(result.decode())
