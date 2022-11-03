import os

file_in = open('zen.txt', 'r')
text = file_in.read().split('\n')
file_in.close()

for i_text in range(len(text) - 1, -1, -1):
    print(text[i_text])