

#ySimpleGUI_License = 'epytJ2MIavWhNylbbBnJN3lCVsH7lYwDZvSQIu6FIlkERVl7d8mMVEsQbE3UBqlLc1inItsPIHkjxXp1Y12BVsuGcT2pVwJlRiCYIN6WMXTzcVyzMOD9c1xzMSzhEWyzNjilwpiFT0GAlJjYZdWt5TzcZPUpRBlRcVG4xEvyeOWw1elsblnkRwWIZRXKJpz7adWu9pudI3jQo1xVL2CEJdOCYoWz1Ul8RAmPlVyfcD39QZieONilJLr2atXEJfpibHG5wFifL3CrJUOEYmWp1vloTwGeFFzZdrCiIe6wIdmr1CvCckmz986RbC3rYGiLLoCOJUDPb62e1IwYYOWv5x52ILjboAiRIdiTwOi7QT3KVnzsd6Gs9AtWZwXRJoJTRFCEIA6aIujHIx5pO6D2c1zpINicwyipRsGnFy0aZ8UelFzjcT3hVJlOZRCnIP6WI6jwA33NL5zBEExlLjz0IQwTMLjsQHiwL1CQJiEFYyXjRklvRxX1hnw5ajXVJVlzcdytIl6CICj7Aa3FLMzREUxVLWzEIHweMjjfU1i9LACvJDFkb0WUFZpIb2EhF6kWZYHxJylBcA3nMHiBOdilJkrfbEWk16vrcTmJ9w60b23RZwAEZ12D18h3aSWPwduMY92498t9IciWwMi1SfV8BvBvZgG6RYy6Z2XwNGzlIGjkosioOFTbEju5MpTNIWyQLdjOYHwGLljDE85lMCS7JW9783e3b03e8555d5ebea3233d30c4df0a283fbf0753fc4383239a9e57b039979f9216f42e89bf39170fb83c0057394f45eb3571480ad6f2f99c3209677db906c4eaa148b97b7ce7d98fd1e942c5a578c9a7400c563a2ddfbe27b6ce4ee62dae317a17cadc0a7f749fd44eb5bbb231adaf3a784ab1f2b2a508fe707bb7c64905bbf28f19638829b3500ad9f48be91803adf5e8f616a9f6ec73d18c9ce7b5d56bdd344f53985d08ef6e7ec7b3d227be1d3c3a69a40f3d41608ef4dd298b159cd2f42f3dc53c4eaae02b5e778d429490cbd6811c3eab725524684e1d3dd6ddffdd837c2e8d2698e157da0a0a5c847abb03968c2401d576312ffd8d1bd5b54f359862062beffacba690c91f3d21e58af4914a67beb52139be376c47bc8c4825e016efe8638ca62cc5b46cf1bfa88b2b3b3dc3d9dac143acfc4ccf277c134d3dca5ea6813090e249e192d28f90397cfdace55136078aa82097645120591b9e82f64f4222f4b0b624812d94c60d0122d513234d91387775138c8d11083268a02fcf7b5fe3940574017f8b9991cf2b70aa4a89be8b687f84330dbddaba3aec8d34a55ce3c58f50db885e21b782e0601170f1cd9faa92c2680874b73bfe91a0a15ccd6ea4207296775230c944f96e6e10b3acab82cdbac7a660760e977b8abb955d26d5072ed857ab4cb72b2edb34baa591fecb24b81eceecae0b729090201592cd0487226

import PySimpleGUI as sg
import random


def update():
    # получаем новое случайное число
    r = random.randint(1, 100)
    # получаем доступ к текстовому элементу
    text_elem = window['-text-']
    # выводим в него текст с новым числом
    text_elem.update("Результат: {}".format(r))


# что будет внутри окна
# первым описываем кнопку и сразу указываем размер шрифта
layout = [[sg.Button('Новое число', enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
          # затем делаем текст
          [sg.Text('Результат:', size=(25, 1), key='-text-', font='Helvetica 16')]]
# рисуем окно
window = sg.Window('Генератор случайных чисел', layout, size=(500, 200))
# запускаем основной бесконечный цикл
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
