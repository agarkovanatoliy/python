from interfaces import *
from file_handling import *

while True:
    interface()
    command = int(input('Введите команду: '))
    if command == 1:
        person = input("Введите данные пользователя ")
        add_person(person)
    elif command == 2:
        show_all()
    elif command == 3:
        name = input("Введите элемент для поиска: ")
        search_element(name)
    elif command == 4:
        while True:
            interface_changes()
            command = int(input('Введите команду: '))
            if command == 1:
                person = input("Введите данные пользователя ")
                contact_deletion(person)
            elif command == 2:
                while True:
                    data_changes()
                    command = int(input('Введите команду: '))
                    if command == 1:
                        person = input("Введите данные пользователя ")
                        index = 0
                        new_name = input('Введите новую фамилию ')
                        contact_replacement(person, index, new_name)
                    elif command == 2:
                        person = input("Введите данные пользователя ")
                        index = 1
                        new_name = input('Введите новое имя ')
                        contact_replacement(person, index, new_name)
                    elif command == 3:
                        person = input("Введите данные пользователя ")
                        index = 2
                        new_name = input('Введите новое отчество ')
                        contact_replacement(person, index, new_name)
                    elif command == 3:
                        person = input("Введите данные пользователя ")
                        index = 0
                        new_name = input('Введите новый номер телефона ')
                        contact_replacement(person, index, new_name)
                    elif command == 5:
                        person = input("Введите данные пользователя ")
                        for i in range(4):
                            if i == 0:
                                index = 0
                                new_name = input('Введите новую фамилию ')
                                contact_replacement(person, index, new_name)
                                person = new_name
                            if i == 1:
                                index = 1
                                new_name = input('Введите новое имя ')
                                contact_replacement(person, index, new_name)
                            if i == 2:
                                index = 2
                                new_name = input('Введите новое отчество ')
                                contact_replacement(person, index, new_name)
                            if i == 3:
                                index = 3
                                new_name = input('Введите новый номер телефона ')
                                contact_replacement(person, index, new_name)
                    elif command == 6:
                        break
                    else:
                        print("Ввод некорректен")
            elif command == 3:
                break
            else:
                print("Ввод некорректен")
    elif command == 5:
        break
    else:
        print("Ввод некорректен")