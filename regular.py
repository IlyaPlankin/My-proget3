import re   # регулярные выражения. Выбирать откуда-то по шаблону нужную информацию из строки.
            # Пример result=re.match(r'pri',stroka)

stroka = 'Privet, menya zovut kirill, mne 38 let, moi telefon 89967860524, a pocta kmmorozov@gmail.com,rabochiy telefon 89969860524'
result = re.match(r'Privet, menya zovut kirill', stroka)    # вывод: <re.Match object; span=(0, 3), match='Pri'>
                                                            # где (0, 3) - это счет с начало строчки до конца!
                                                            # И да re.match ищет только с начало строки!!! Например menya или zovut не найдет!
#print(result)

#print(result.group(0))  # print(result.group(0))   вывести строку
#print(result.start())  # print(result.start())   вывести начало
#print(result.end())  # print(result.end()) вывести конец

#################################################

#result = re.search(r'telefon', stroka)      # Ищет прямо по строке! <re.Match object; span=(44, 51), match='telefon'>
#print(result)

#################################################
#result = re.split(r'moi', stroka)           # Разбить строку по слову moi - разделитель его не показывают!
#print(result)

#################################################
#result = re.findall(r'telefon',stroka)      # re.findall(r'telefon',stroka) ищет все вхождения в строке данного слова -telefon!
#print(result)

#phones = re.findall(r'\d{7,11}', stroka)   # используем справочник по регулярным выражениям python!
                                            # https://uproger.com/shpargalka-po-regulyarnym-vyrazheniyam-python-2023/?ysclid=lpbe6u8vmk139525510
                                            # \d {7,11} - ищет цифры 7 от 11
#print(phones)

phones = re.findall(r'\b\d\d\d\d\d\d\d\b\b|\d\d\d\d\d\d\d\d\d\d\d\b',stroka)  # ищет 2 телефона!
print(phones)
#emails = re.findall(r'\w+@\w+\.\w+', text)
#print(emails)

                                            #[]- список (огурчик, банан, помидор и тд...)
                                            #{} -Словарь - это тип данных, аналогичный массивам, но работающий с ключами и значениями вместо индексов.
                                            #{"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}