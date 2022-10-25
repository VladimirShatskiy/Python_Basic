def tpl_sort(*list):
    if sum(list) - int(sum(list)) != 0:
        return list
    return sorted(list)


# print("Ответ в консоли:", tpl_sort(6, 3, -1, 8, 4, 10, -5))

