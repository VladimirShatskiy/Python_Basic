def fibonachi(number):
    if number < 2:
        return number
    else:
        return fibonachi(number - 1) + fibonachi(number - 2)


number = int(input("ВВеди позицию числа Фибоначи: "))
print(fibonachi(number))