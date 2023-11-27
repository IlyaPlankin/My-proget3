def get_and_norm_user_data():
    a = input('Введите a: ')
    b  = input('Введите b: ')
    try:
        a = int(a)
        b = int(b)
        return a,b
    except:
        a = None
        b = None
        return a, b

if __name__ == '__main__':
    oper = input('Введите операцию:')
    a,b = get_and_norm_user_data()
    if oper == 'plus' and a !=None and b!=None:
        c = a + b
        print(c)
    elif oper == 'minus' and a != None and b != None:
        c = a - b
        print(c)
    elif oper == 'umnoj' and a != None and b != None:
        c = a * b
        print(c)
    elif oper == 'deli' and a != None and b != None:
        c = a / b
        print(c)