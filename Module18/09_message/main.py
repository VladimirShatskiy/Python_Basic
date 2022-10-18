txt = input("Сообщение: ")
temp = ""
new_txt = ""

for sim in txt:
    if sim.isalpha():
        temp += sim
    else:
        new_txt += temp[:: -1] + sim
        temp = ""

print(f"новое собщение {new_txt}")

