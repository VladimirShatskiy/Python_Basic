from Fio import generate_age, generate_surname, generate_name
import random

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Employer(Person):
    def __init__(self, name, surname, age, salary=0):
        super().__init__(name, surname, age)
        self.salary = salary

    def get_salary(self):
        return self.salary


class Agent(Employer):
    def __init__(self, name, surname, age, sales_value, salary=0):
        super().__init__(name, surname, age, salary)
        self.sales_value = sales_value
        self.salary = 5000 + self.sales_value * 0.05

    def __str__(self):
        return f'У агента {self.name} по фамилии {self.surname} Возрастом ' \
               f'{self.age} Заработная плата {self.salary}'


class Manager(Employer):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__salary = 13000

    def __str__(self):
        return f'У менеджера {self.name} по фамилии {self.surname} Возрастом ' \
               f'{self.age} Заработная плата {self.__salary}'


class Worker(Employer):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours
        self.__salary = 100 * self.hours

    def __str__(self):
        return f'У рабочего {self.name} по фамилии {self.surname} Возрастом ' \
               f'{self.age} Заработная плата {self.__salary}'


people_list = []
count = 0
for i in range(3):
    people_list.append(Agent(name=generate_name(), surname=generate_surname(), age=generate_age(), sales_value=random.randint(100000, 200000)))
    people_list.append(Manager(name=generate_name(), surname=generate_surname(), age=generate_age()))
    people_list.append(Worker(name=generate_name(), surname=generate_surname(), age=generate_age(), hours=random.randint(30, 80)))

with open('emp.txt', 'w') as file_out:
    for item in people_list:
        file_out.write(str(f'{item}\n'))
        print(item)
        count += item.get_salary()
    file_out.write(str(f'Общая заработная плата сотрудников {count}\n'))
    print(f'Общая заработная плата сотрудников {count}\n')


