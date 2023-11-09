vegetables = ('kapusta', 'morkov', 'pomidor', 'kartofel')

f = open('vegetables.txt', 'w')

for vegetable in vegetables:
    print(vegetable)
    f.write(vegetable+'\n')

f.close()
