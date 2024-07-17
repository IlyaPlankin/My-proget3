import requests

if __name__ == '__main__':
    in_valute = input("Какую вылюту вы хотите обменять? ")
    out_valute = input("Какую вылюту вы хотите получить? ")
    in_valute_count = int(input("Сколько валюты вы хотите обменять! "))

    result=requests.get(f'f'http://192.168.218.233:8080/obmen/?val1={in_valute}&val2={out_valute}&count={in_valute_count}')


print(result.text)