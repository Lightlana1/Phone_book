# Интерфейс для ввода данных в телефонный справочник
import File_writing as file

def get_info ():
    info = []
    family = input('Введите фамилию: ')
    info.append(family)
    name = input('Введите имя: ')
    info.append(name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) > 11:
                print('В номере телефона не должно быть больше 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)

    file.writing_csv(family, name, phone_number, description)
    file.writing_txt(family, name, phone_number, description)


