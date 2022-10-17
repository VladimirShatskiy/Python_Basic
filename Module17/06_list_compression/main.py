import random

number = int(input("количество цыфр последовательности: "))

list =[random.randint(0, 2) for _ in range(number)]
print(f"Список до сжатия: {list}")
list1 =[x for x in list if x > 0]
print(f"Список после сжатия: {list1}")

