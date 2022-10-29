nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
new_list = []
def line(list):
    for item in list:
        if isinstance(item, int):
            new_list.append(item)
        else:
            line(item)


line(nice_list)
print(new_list)