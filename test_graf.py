import matplotlib.pyplot as plt
import requests

val = input("Введите валюту:")
start_date = input("Введите начало периода:")
end_date = input("Введите конец периода:")

result = requests.get(f'http://192.168.20.46:8080/plot?val={val}&start_date={start_date}&end_date={end_date}')
raw_points = result.json()

# print(raw_points)

dates = []
rates = []

for pl in raw_points:
    dates.append(pl[0])
    rates.append(float(pl[1]))

print(dates)
print(rates)
plt.xlabel("Даты")
plt.ylabel('Курс в рублях')
plt.title(f'Курс валюты {val} от {start_date} до {end_date}')
# plt.legend("123432523523")
plt.plot(dates, rates)
plt.bar(dates, rates)
plt.show()