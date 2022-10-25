femaly = {
    ("Сидоров Иван"): 35,
    ("Сидоров Петр"): 23,
    ("Сидоров Владимир"): 12,
    ("Иванов Владимир"): 12,
    ("Иванова Света"): 34,
}

surname = (input("Введите фамилию: ")).lower()

if surname[-1] == "а":
  surname = surname[: -1]

for sur in femaly:
  if surname in sur.lower():
    print(sur, femaly[sur])

