import random

num = int(input("Количество чисел в списке: "))

list = [1 if number % 2 == 0 else number % 5 for number in range(num)]
print(list)

