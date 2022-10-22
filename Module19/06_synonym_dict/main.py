num_sim = {
    1: "первая",
    2: "вторая",
    3: "третья",
    4: "четвертая",
    5: "пятая"
        }

synonym = dict()
count_synonym = int(input("Введи количесво пар слов (формат Слово - Слово): "))

for i_count in range(count_synonym):
    str = input(f"{num_sim[i_count + 1]} пара: ").lower()
    pos_tab = str.index(" ")
    synonym[str[:pos_tab]] = str[pos_tab + 3:]

for _ in range(2):
    word = input("Введи слово: ").lower()
    syn = synonym.get(word)
    if syn == None:
        print("Такого слова в словаре нет")
    else:
        print(f'Синоним {syn}')