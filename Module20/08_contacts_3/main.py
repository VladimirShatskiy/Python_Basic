def new_number():
    name, surname = (input("Введите имя и фамилию нового контакта (через пробел): ")).split()
    # проверка по книге
    for piople in adress_book:
        if name in piople and surname in piople:
            print(f"\nТакой абонент есть, добавление невозможно \n")
            return
    adress_book[name, surname] = input("Введите номер телефона: ")

def searth_number():
    name = input("Введите фамилию для поиска: ").title()
    for piople in adress_book:
        if name == piople[1]:
            print(piople[0], piople[1], adress_book[piople])


adress_book = {('Иван', 'Сидоров'): '123', ('Иван', 'Петров'): '345', ('Ира', 'Сама'): '567'}
while True:
    choice = int(input(f" 1. Добавить контакт \n 2. Найти человека \n ? "))
    if (choice) == 1:
        new_number()
    elif choice == 2:
        searth_number()
    else:
        print("Ошибка ввода")

    print("\n", adress_book)

