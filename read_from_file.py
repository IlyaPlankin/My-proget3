f = open("users.txt", "r")

for line in f:
    line = line.strip()  # strip - Удаление пробельных символов
    split_line = line.split(":")  # split - Разбиение строки по разделителю
    # print(split_line)
    name = split_line[0]
    surname = split_line[1]
    sex = split_line[2]
    phone = split_line[3]
    # print(f"Привет,меня зовут {name},моя фамилия {surname},пол {sex},телефон {phone}") = insert_string - тоже самое!
    insert_string = f'insert into telsprav values ("{name}","{surname}","{sex}","{phone}")'
    print(insert_string)

f.close()
