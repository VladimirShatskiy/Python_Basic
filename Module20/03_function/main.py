def slicer(string, num):
    start = string.index(num) + 1
    end = string[start:].index(num)
    new_string = (simbol for simbol in string[start:end + start])

    print(new_string)
    return new_string


# slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2)




