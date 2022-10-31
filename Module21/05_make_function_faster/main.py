def fact(num):
    if num == 1:
        return num
    else:
        num *= fact(num - 1)
    return num


def calculating_math_func(data):
  if data in list_fact.keys():
    return list_fact[data]
  else:
    result = fact(data)
    result /= data ** 3
    result = result ** 10
    list_fact[data] = result
    return result


list_fact = {}
for i in range(int(input("сколько цыфр проверяем "))):
  print(calculating_math_func(int(input("Введи число "))))
