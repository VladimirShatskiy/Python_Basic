string = input("Введи строку: ")
dictionary = dict()

print("Оригинальный словарь частот:")
for simbol in set(string):
    count_sim = string.count(simbol)
    print(f"{simbol} : {count_sim}")
    dictionary[count_sim] = dictionary.get(count_sim, []) + [simbol]

print("\nИнвертированный словарь частот:")
for item in dictionary.keys():
    print(f"{item} : {dictionary[item]}")

