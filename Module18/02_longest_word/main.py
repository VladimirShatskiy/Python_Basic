long, word = 0, ""

string = input("Введ строку: ")

str_word = string.split()

for wr in str_word:
  if len(wr) > long:
    long = len(wr)
    word = wr

print(f"Самое длинное слово в строке: {word}\n"
f"Длина этого слова: {long}")

