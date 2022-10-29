def check_arg(element, i):
    if isinstance(element, dict):
        return list(element.keys())[i]
    else:
        return element[i]

def elem(args, i):
    temp = tuple(check_arg(element, i) for element in args)
    return temp

def my_zip(*args):
    list_str = []
    min_len = int(min(len(item) for item in args))
    list_str = [(elem(args, i)) for i in range(min_len)]

#     print(list_str)
#
#
# a = [1, 2, 3, 4, 5]
# b = {1: "s", 2: "q", 3: 4}
# x = (1, 2, 3, 4, 5)
#
# my_zip(a, x, b)
