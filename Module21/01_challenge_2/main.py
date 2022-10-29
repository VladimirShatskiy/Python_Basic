def prn(number, end_number):
    print(number)
    if number == end_number:
        return
    prn(number + 1, end_number)

prn(1 , int(input("Введите количество: ")))