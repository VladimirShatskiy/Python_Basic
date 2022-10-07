def sum_number(number):
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    print("Сумма чисел :", sum)
    return sum
def count_number(number):
    count = 0
    while number >= 1:
        count += 1
        number //= 10
    print("Количество цифр в числе :" , count)
    return count

number = int(input("Введи число "))
print("Разность суммы и количества цифр ", sum_number(number) - count_number(number))

