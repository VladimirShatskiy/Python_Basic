import os
count = 0

file_in = open('numbers.txt', 'r', encoding='utf-8')
date = file_in.read().split()

for i in date:
    count += int(i)
file_in.close()

file_out = open('answer.txt', 'w')
file_out.write(f'Sum numbers {count}')
file_out.close()


