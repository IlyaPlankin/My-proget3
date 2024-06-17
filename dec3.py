def upper_decorator(func):
    def wrapper():
        data =func().upper()
        return data
    return wrapper
@upper_decorator
def my_name_func():
    return 'кирилл'

if __name__=='__main__':
    name = my_name_func()
    print(name)
