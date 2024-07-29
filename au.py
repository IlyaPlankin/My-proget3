import sys
import hashlib


login = input("Введтье логин:")
passwd = input("Введите пароль: ")

h_passwd = hashlib.sha256(passwd.encode()).hexdigest()
print(h_passwd)

if login == "kirill" and h_passwd == '8888':
    print('work')
else:
    print("Ошибка ввода пароля")
    sys.exit(0)