class IterClass:
    def __init__(self, limit):
        self.count = -1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        return self.count ** 2

def prn_str(str):
    for i in str:
        print(i, ' ', end='')


def sq(number):
    count = 0
    for i in range(number):
        yield i ** 2
        count += 1

n_number = 10  # int(input("Число в последовательности "))

print('Генераторное выражение')
prn_str(i ** 2 for i in range(n_number))

print('\nКласс итератор')
str = []
date = IterClass(10).__iter__()
for i in range(10):
    str.append(next(date))
prn_str(str)

print('\nКлас генератор')
str = sq(10)
prn_str(str)






