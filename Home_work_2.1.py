users = ('ilya: Plankin: m: 89996660544', 'Oleg: Galkin: m: 89996660544', 'Tamara: Karpova: f: 89996660554',
              'Sveta: Bereskina: f: 89552896407')

f = open('users2.txt', 'w')
for user in users:
    print(user)
    f.write(user+'\n')