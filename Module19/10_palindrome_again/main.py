string = input("Введи строку: ")
count = 0

for i in set(string):
    count += int(string.count(i)) % 2

if (len(string) % 2 == 0 and count == 0) or (len(string) % 2 == 1 and count == 1):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")
