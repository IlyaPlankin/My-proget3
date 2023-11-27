oper = input('Введите операцию:')

if oper == 'plus':
    a = input('Введите a:')
    b = input('Введите b:')
    try:
        a = int(a)
        b = int(b)
        c = a + b
        print(c)
    except:
        print('ошибка')
elif oper == 'minus':
    a = input('Введите a:')
    b = input('Введите b:')
    try:
        a = int(a)
        b = int(b)
        c = a - b
        print(c)
    except:
        print('ошибка')
elif oper == 'umnoj':
    a = input('Введите a:')
    b = input('Введите b:')
    try:
        a = int(a)
        b = int(b)
        c = a * b
        print(c)
    except:
        print('ошибка')
elif oper == 'deli':
    a = input('Введите a:')
    b = input('Введите b:')
    try:
        a = int(a)
        b = int(b)
        c = a - b
        print(c)
    except:
        print('ошибка')