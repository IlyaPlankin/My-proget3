def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end=time.time()
        print(f'Время выполнения {end - start}')
        return wrapper

def printestrata():
    print('test')

if __name__ == '__main__':
    printestrata()