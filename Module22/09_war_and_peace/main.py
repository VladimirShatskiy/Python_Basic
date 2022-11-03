import zipfile
import os

alfa = {}
alfa_sort = {}
file_in_zip = []

z_file = zipfile.ZipFile('voyna-i-mir.zip', 'r')
for name in z_file.namelist():
    file_in_zip.append(name)
    print(f'Извлекаем файл {name} из архива voyna-i-mir.zip')

file_ext = z_file.extract(file_in_zip[0])
z_file.close()

file_source = open(file_ext, 'r', encoding='utf-8')
date_file = file_source.read()
file_source.close()
os.remove(file_source.name)

for item in date_file:
    if item.isalpha():
        if item in alfa.keys():
            alfa[item] += 1
        else:
            alfa[item] = 1

alfa_sort = sorted(alfa.items(), key=lambda item: item[1], reverse=True)

for i_key, i_value in alfa_sort:
    print(f'{i_key} {i_value :8d}')