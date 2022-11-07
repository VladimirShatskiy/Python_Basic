def write_file(user):
  with open('dialog.txt', 'a', encoding='utf-8') as file_open:
    file_open.write(f'\n\n{user}:\n')
    file_open.write(input("Введи текст в чат: "))
  

def read_file():
  with open('dialog.txt', 'r', encoding='utf-8') as file_open:
    text = file_open.read()
    print(text)


user = ''
while user != 'stop':
  user = input('\nИмя пользователя?:')
  print(f'\nВыбери действие:  \n'
        f'1 - Прочитать чат\n'
        f'2 - Внести текст в чат  ', end = '')
  try:
    ans = int(input())
  except:
    print('\nВеден неверный символ действия повторяем с ввода пользователя\n')
    ans = 0
  if ans == 1:
    read_file()
  elif ans == 2:
    write_file(user)
  else:
    print('Неободимо выбрать 1 или 2')
