many = int(input("Кол-во человек "))
count = int(input("Какое количество людей в считалке "))
print(f"\nЗначит выюывает каждый {count}-й человек")
count_stream = 1
people = [i for i in range(1,many +1 )]

while len(people) > 1:
    print(f"Текущий круг людей {people}\n"
          f"Начало счета с номера {people[count_stream - 1]}")
    for _ in range(1, count + 1):
        if count_stream >= len(people):
            count_stream = 0
        count_stream += 1
    print(f"Выбывает человек под номером {people[count_stream - 2]}\n")
    people.remove(people[count_stream - 2])
    if count_stream == 1:
        count_stream = 1
    else:
        count_stream -= 1

print(f"Остался человек по номером {people}")





