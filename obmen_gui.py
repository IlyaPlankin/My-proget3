import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [[sg.Text("Первая валюта:", font='Helvetica 16'), sg.InputText(font='Helvetica 16')],
          [sg.Text("Вторая валюта: ", font='Helvetica 16'), sg.InputText(font='Helvetica 16')],
          [sg.Text("Количество:    ", font='Helvetica 16'), sg.InputText(font='Helvetica 16')],
          [sg.Text("0.0", font='Helvetica 16')],
          [sg.Button("Вычислить", enable_events=True, key='-CALC-', font='Helvetica 16')
           ]]

window = sg.Window("Обменник валют.", layout)

while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
    if event == '-FUNCTION-':
        update()
# закрываем окно и освобождаем используемые ресурсы
window.close()
