guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    quantity = len(guests)
    print(f"Сейчас на вечеринке {quantity} человек: {guests}")
    choice = input("Гость пришел или ушел? ")
    name = input("Имя гостя: ")

    if name == "Пора спать" or choice == "Пора спать":
        break

    if choice == "пришел":
        if quantity <= 5:
            guests.append(name)
            print(f"Привет: {name}")
        else:
            print(f"Прости, {name}, но мест нет ")
    elif choice == "ушел":
        guests.remove(name)
    else:
        print(f"Не понятно, что с {name}")