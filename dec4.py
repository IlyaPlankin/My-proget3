

def upper_decorator(func):
    def wrapper(*args, **kwargs):
        data =func(*args, **kwargs).upper()
        return data
    return wrapper

def split_decorator(func):
    def wrapper():
        data = list (func())
        return data
    return wrapper

@split_decorator
def my_name_func():
    return 'кирилл'

@upper_decorator
def hello(name):
    return (f"Hello, {name}!")


if __name__=='__main__':
    name = my_name_func()
    print(name)
    line=hello('kirill')
    print(line)