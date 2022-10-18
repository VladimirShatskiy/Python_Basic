bad_start = "@№$%^&\*()"

n_file = input("Введи название файла: ")

if not n_file.endswith(".txt") and not n_file.endswith(".docx"):
  print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
elif bad_start.count(n_file[0]) > 0:
  print("Ошибка: название начинается на один из специальных символов.")
else:
  print("Файл назван верно.")

