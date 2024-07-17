import PySimpleGUI as sg
import requests


def get_ovcount_from_api(iv, ov, count):
    apiurl = f'http://192.168.218.233:8080/obmen?val1={iv}&val2={ov}&count={count}'
    result = requests.get(apiurl)
    result_sring = result.text
    result_elem = window['result']
    result_elem.update(result_sring)


def clear():
    window['result'].update("")
    window['ov'].update("")
    window['iv'].update("")
    window['cv'].update("")


sg.theme('DarkBlue13')

layout = [[sg.Text("Первая валюта:", font='Helvetica 16'), sg.InputText(font='Helvetica 16', key='iv')],
          [sg.Text("Вторая валюта: ", font='Helvetica 16'), sg.InputText(font='Helvetica 16', key='ov')],
          [sg.Text("Количество:    ", font='Helvetica 16'), sg.InputText(font='Helvetica 16', key='cv')],
          [sg.Text("0.0", font='Helvetica 16', key='result')],
          [sg.Button("Вычислить", enable_events=True, key='-CALC-', font='Helvetica 16'),
           sg.Button("Очистить", enable_events=True, key='-CLEAR-', font='Helvetica 16')]]

window = sg.Window("Обменник валют.", layout)

while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
    if event == '-CALC-':
        print(values)
        print(type(values))
        get_ovcount_from_api(values['iv'], values['ov'], values['cv'])
    if event == '-CLEAR-':
        clear()
# закрываем окно и освобождаем используемые ресурсы
window.close()