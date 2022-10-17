def is_vowers(letter):
  ret_letter = ""
  for sim in vowels:
    if letter == sim:
      return sim
      break
  return ret_letter


vowels =["а", "о", "у", "э", "ы", "я", "ё", "ю", "у", "и"]

string = input("Введи строку: ")

list = [letter for letter in string if is_vowers(letter) != ""]

print(f"Список гласных букв: {list}\nКоличество букв: {len(list)}")
