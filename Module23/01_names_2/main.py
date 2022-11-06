import datetime

def count_sym_str(string):
    count = 0
    for sym in string:
        if sym != '\n':
            count += 1
    return count


count_total = 0
with open('peple.txt', 'r', encoding='utf-8') as file_source:
    date_source = file_source.read().split()
    for i_str in range(len(date_source)):
        try:
            len_str = count_sym_str(date_source[i_str])
            if len_str < 3:
                raise BaseException()
            count_total += len_str

        except BaseException:
            print(f'Ошибка: Длина имени менее 3 символов, в строке {i_str}')

            with open('errors.log', 'a', encoding='utf-8') as file_error:
                file_error.write(str(datetime.datetime.now()))
                file_error.write(f'\tДлина имени менее 3 символов, в строке {i_str}\n')

print(f'Общее количество символов с файле {count_total}')

