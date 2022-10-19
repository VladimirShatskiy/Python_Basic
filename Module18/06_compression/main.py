string = input("Введите строку: ")
count, new_string = 1, ""

for item in range(len(string) - 1):
  if string[item] == string[item + 1]:
    count += 1
  else:
    new_string += string[item] + str(count)
    count = 1

new_string += string[-1] + str(count)
print(new_string)

