orig_list = [i for i in range(10)]

new_list =[(orig_list[i], orig_list[i + 1]) for i in range(len(orig_list)) if i % 2 == 0]

print("Оригинальный список: {}".format(
    orig_list))
print("Новый список: {}".format(
    new_list))

