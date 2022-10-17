import random

list = ["I" for _ in range(10)]
attempt = int(input("Введи количество бросков: "))

for att in range(attempt):
    left = random.randint(0, 9)
    right = random.randint(left, 9)
    print(f"Бросок {att + 1}. Сбиты палки с номера {left + 1}\n"
          f"по номер {right + 1}\n")

    for i in range(left, right + 1):
        list[i] = "."

print("Результат: ", end="")
for i in range(len(list)):
    print(list[i], end="")

