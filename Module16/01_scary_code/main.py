# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
count_5 = a.count(5)

for _ in range(count_5):
    a.remove(5)

a.extend(c)
count_3 = a.count(3)

print(f"Результат работы программы\n"
      f"Количество цифр 5 при первом объединении : {count_5}\n"
      f"Количество цифр 3 при втором объединеии : {count_3}\n"
      f"Итоговый список: {a}")

