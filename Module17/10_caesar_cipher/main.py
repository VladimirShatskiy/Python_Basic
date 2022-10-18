alfa = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя    "

word = input("Введи слово для шифрования:")
str = []

str = [alfa[alfa.index(word[i]) + 3] if word[i] != "" else "" for i in range(len(word))]

for i in str:
  print(i , end ="" )
