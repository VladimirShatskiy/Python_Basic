str1 = input("Первая строка: ")
str2 = input("Вторя строка: ")

rev = False

for i in range(len(str1)):
    str2 = str2[1:] + str2[0]
    if str2 == str1:
        print(f"Первая строка получается из второй со сдвигом {i + 1}")
        rev = True
        break
if not rev:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")

