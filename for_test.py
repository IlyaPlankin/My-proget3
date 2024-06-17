def printall(a=None,b=None,c=None):
    print(a,'первый вывод')
    print(b,'второй вывод')
    print(c,'третий вывод')

if __name__=='__main__':
    printall('kirill')
    l1 = [1,2,3]
    l2 = [*l1,4,5,6]
    print(l2)
    print("------------------------")
    print(l1)
    print(*l1)