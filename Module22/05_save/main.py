import os

def op_file(ful_way, text):
    open_file = open(ful_way, 'w')
    open_file.write(text)
    open_file.close()


text = input("Введите строку для записи в файл:")
print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
way_list = input()

file_name = str(input("Введите имя файла: ") + ".txt")
ful_way = os.path.abspath(os.path.join(*way_list.split(), file_name))

if not os.path.isfile(ful_way):
    op_file(ful_way, text)
    print("Файл успешно сохранён!")
else:
    if input('Перезаписать файл y/n; ').lower() == 'y':
        op_file(ful_way, text)
        print('Файл успешно перезаписан!')
