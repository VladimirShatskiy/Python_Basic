students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def fun():
    long, s_interest = 0, []

    for i, i_value in students.items():
        s_interest += i_value["interests"]
        long += len(i_value["surname"])

    return set(s_interest), long


num_age = [(i, i_value["age"]) for i, i_value in students.items()]
ans = fun()

print('Список пар "ID студента — возраст":', num_age)
print("Полный список интересов всех студентов: {}\n Общая длина всех фамилий студентов: {}".format(
    ans[0],
    ans[1]))
