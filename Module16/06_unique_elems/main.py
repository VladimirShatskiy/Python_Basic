def in_list(count, name):
    list = []
    for i in range(count):
        print(f"Введите {i + 1}-е число для {name} списка ", end="")
        list.append(input(""))
    return list


list1, list2 = [], []

list1.extend(in_list(3, "первого"))
list2.extend(in_list(7, "второго"))

print(f"Первый список: {list1} \n"
      f"Второй списк: {list2}")

list1.extend(list2)
list1 = list(set(list1))

print(f"\nНовый первый список: {list1}")
