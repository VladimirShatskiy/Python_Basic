def fact(num):
    if num == 1:
        return num
    else:
        num *= fact(num - 1)
    return num


def calculating_math_func(data):
    # result = 1
    result = fact(data)
    # for index in range(1, data + 1):
    #     result *= index
    result /= data ** 3
    result = result ** 10
    return result

print(calculating_math_func(5))
