def reverce_number(number):
    new_number = 0
    while number != 0:
        new_number = number % 10 + new_number * 10
        number //= 10
    return new_number
def number_dev(number):
    int_number = int(number)
    fract_number = round(number - int_number, 2)
    new_number = reverce_number(int_number) + reverce_number(fract_number * 100) / 100
    return new_number


N = float(input("Введи первое число N "))
K = float(input("Введи первое число K "))
N = number_dev(N)
K = number_dev(K)
summ = N + K
print("Первое число наоборот :", N)
print("Второе число наоборот :", K)
print("Сумма :", summ)