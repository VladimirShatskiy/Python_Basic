quantity = int(input("Количество друзей: "))
receipt = int(input("Долговых расписок: "))
balance = [0 for _ in range(quantity)]

for i in range(receipt):
    print(f"\n{i + 1}-я расписка ")
    kredit = int(input("Кому: "))
    debit = int(input("От кого: "))
    money = int(input("Сколько: "))
    balance[kredit -1] += money
    balance[debit - 1] -= money

print("\nБаланс другей:")
for i in range(len(balance)):
    print(f"{i + 1}: {balance[i]}")
