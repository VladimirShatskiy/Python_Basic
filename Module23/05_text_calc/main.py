count = 0

with open("calc.txt", "r", encoding='utf-8') as file_open:
  date_file = file_open.read().split('\n')

for item in range(len(date_file)):
  try:
    if len(date_file[item].split()) != 3:
      raise IndexError
    else:
      try:
        count += eval(date_file[item])
      except:
        print(f'Обнаружена ошибка в строке {date_file[item]}, хотите исправить? ', end ="")
        if input().lower() == 'y':
          count += eval(input('Введите исправленную строку '))
          
  except IndexError:
    print('В формуле недосаточно элементов ')

print(f'\nСумма результатов: {count}')
