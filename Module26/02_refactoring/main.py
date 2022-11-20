list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break

# TODO провести рефакторинг кода


def fan(list1, list2):
    for i in list1:
        for x in list2:
            yield i * x


if to_find in fan(list_1, list_2):
    print('Found!!!')


