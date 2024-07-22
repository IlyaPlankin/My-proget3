import sys
import hashlib

login = input("Введтье логин:")
passwd = input("Введите пароль: ")

h_passwd = hashlib.sha256(passwd.encode()).hexdigest()
print(h_passwd)

if login == "kirill" and h_passwd == '5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5':
    print('work')
else:
    sys.exit(0)
