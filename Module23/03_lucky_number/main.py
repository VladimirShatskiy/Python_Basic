import random


count, stop_count, stop_item = 0, 777, 5

try:
    with open('out_file.txt', 'w') as file_open:
        while count < stop_count:
            number = int(input('Введи число: '))
            if stop_item == random.randint(0, 13):
                raise BaseException
            file_open.write(str(number) + '\n')
            count += number
    print('Вы успешно выполнили условие для выхода из порочного цикла!')

except BaseException:
    print('Вас постигла неудача')



