import os

def write_file(user_name):
  with open(os.path.join('C:\\temp', 'dialog.txt'), 'a', encoding='utf-8') as file_open:
    file_open.write(f'\n\n{user_name}:\n')
    file_open.write(input("Введи текст в чат: "))


def read_file():
  try:
    with open(os.path.join('C:\\temp', 'dialog.txt'), 'r', encoding='utf-8') as file_open:
      text = file_open.read()
      print(text)
  except FileNotFoundError:
    print('\nНа данный момент файл пуст или отсутвует, внесите первую запись\n')

user_name: str = input('\nИмя пользователя?: ')

while True:
  print(f'\nВыбери действие:  \n'
        f'1 - Прочитать чат\n'
        f'2 - Внести текст в чат  ', end = '')
  try:
    ans = int(input())
  except:
    print('\nВеден неверный символ действия повторяем, с ввода пользователя\n')
    ans = 0
  if ans == 1:
    read_file()
  elif ans == 2:
    write_file(user_name)
  else:
    print('Неободимо выбрать 1 или 2')

