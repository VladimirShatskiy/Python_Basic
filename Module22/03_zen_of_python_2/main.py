import os

file_in = open('zen.txt')

str_date = file_in.read().split('\n')
count_str = len(str_date)
count_word, count_sym = 0, 0
date_sym = {}

file_in.close()

for i_str in str_date:
    count_word += len(i_str.split())
    for i_sym in i_str.lower():
        if i_sym.isalpha():
            count_sym += 1
            if i_sym in date_sym.keys():
                date_sym[i_sym] += 1
            else:
                date_sym[i_sym] = 1

low_used_sym = list(date_sym.keys())[list(date_sym.values()).index(min(date_sym.values()))]

print('Количество букв в файле: {}\n'
      'Количество слов в файле: {}\n'
      'Количество строк в файле: {}\n'
      'Наиболее редкая буква: {}'.format(
    count_sym,
    count_word,
    count_str,
    low_used_sym
))

