def number_in_row(number, position):
    for i in range(1, position + 1):
       return_number = number % 10
       number //= 10
    return return_number


start_year = int(input('Введите первый год '))
stop_year = int(input("Введите второй год "))

print(f"За годы от {stop_year} до {stop_year} с тремя одинаковыми цифрами:" )

for number in range(start_year, stop_year + 1):
    for pos in range(1, 5):
        coincidence = 0
        searth_number = number_in_row(number, pos)
        for i in range(1, 5):

            if searth_number == number_in_row(number, i):
                coincidence += 1
        if coincidence >= 3:
            print(number)
            break
