import math

print("программа для решений квадратных уровнений")
bad_data = True
while bad_data == True:
    try:
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        c = int(input("Введите число c: "))
        bad_data = False
    except ValueError:
        print("данные не привести к числу")

D = (b * b) - (4 * a * c)
print(D)

if D > 0:
    d = math.sqrt(D)
    x1 = ((-b) + d) / (2 * a)
    x2 = ((-b) - d) / (2 * a)
    print(f"Уравнение имеет 2 корня. x1={x1},x2={x2}")
elif D == 0:
    x1 = (-b) / (2 * a)
    print("Уравнение имеет 1 корнь. x1={}".format (x1))
else:
    print("Уравнение не имеет корней!")
