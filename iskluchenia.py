try:
    print(10/0)
except ZeroDivisionError:
    print("на 0 делить нельзя!")
except NameError:
    print("переменная не задана!")
except ValueError:
    print("невозможно привести к целому число!")
except TypeError:
    print("Ошибка типа данных!")
except:
    print("произошла ошибка!!!!")
