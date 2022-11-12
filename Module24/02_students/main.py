import random
def sort_key(a):
    return a.mid_grade
class Student:
    def __init__(self, name, n_group, performance):
        self.name = name
        self.group = n_group
        self.performance = performance
        self.mid_grade = sum(performance)/len(performance)

    def prn_stud(self):
        print('Студент {name} учится в группе {group} список оценок {grade} средний балл {mid_grade}'
        .format(
            name=self.name,
            group=self.group,
            grade=self.performance,
            mid_grade=self.mid_grade
        ))

group_stud = []

name =['Иван','Саша','Петя','Гоша','Гоча','Вадим','Руслан']
surname= ['Иванов','Петров','Сидоров','Васечкин','Михайлов','Лопатин','Субботин']

for _ in range(10):
    fio = name[random.randint(0, len(name) - 1)] + ' ' + surname[random.randint(0, len(surname) - 1)]
    group_stud.append(Student(fio, random.randint(0, 1000), [random.randint(1, 5) for _ in range(5)]))

temp = sorted(group_stud, key=sort_key)

for item in range(len(temp)):
   temp[item].prn_stud()