def polindrone(list):
    test_list = []
    for i in range(len(list) - 1, -1, -1):
        test_list.append(list[i])
    if test_list == list:
        return True
    else:
        return False


list_number = []
test = []
add_list = []

for i_count in range(int(input("Колчество чисел: "))):
    list_number.append(int(input("Число: ")))

for i in range(len(list_number)):
    for x in range(i, len(list_number)):
        test.append(list_number[x])
    if polindrone(test):
        break
    else:
        test = []

for x in range(0, i):
    add_list.append(list_number[x])
add_list.reverse()

print(f"Последовательность: {list_number}\n"
      f"Нужно пиписать чисел {i}\n"
      f"Сами числа: {add_list}")

