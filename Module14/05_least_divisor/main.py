
number = int(input("Введи число :"))
min_div = 2
while number % min_div != 0:
    min_div += 1
print("Наименьший делитель больше 1 = ", min_div)
