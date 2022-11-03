import os

alfa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_count = 1
def cipher_text(string, num):
    cipher_string = ""
    for i_sym in string:
        cipher_string += alfa[alfa.index(i_sym) % 50 + num]
    return cipher_string


file_open = open('text.txt')
file_wr = open('cipher_text.txt', 'w')
str_from_file = file_open.read()

for i_str in str_from_file.split('\n'):
    str = cipher_text(i_str, str_count)
    str_count += 1
    file_wr.write(str + '\n')

file_wr.close()
file_open.close()