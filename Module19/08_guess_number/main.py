
max_num = int(input("Введите максимальное число: "))
help_w = {"помогите"}
num = set(range(max_num + 1))

while True:
    test = str(input("Нужное число есть среди вот этих чисел: ")).split()
    test = set(test)
    if test == help_w:
        print(f"Артём мог загадать следующие числа: {num}")
        break
    else:
        answ = input("Ответ Артёма: ")
        if answ == "нет":
            num -= test
        else:
            num = test
