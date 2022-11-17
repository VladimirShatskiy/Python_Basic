class Stack:

    def __init__(self):
        self.__base = []

    def add_element(self, *item):
        """Добавление элемента в стек
        """
        self.__base.append(item)

    def del_element(self):
        """
        Удаляет последний элемент стека
        """
        self.__base.remove(self.__base[len(self.__base) - 1])

    def __str__(self):
        return str(self.__base)

    def get_slement(self):
        """
        :return: возвращает последний элемент стека
        """
        return self.__base[len(self.__base) - 1]

    def get_elements(self):
        """
        :return: возвращает все элементы списка
        """
        return self.__base


def manager_task(tasks_temp):
    task_dict = {}
    for i in tasks_temp.get_elements():
        if i[1] in task_dict.keys():
            task_dict[i[1]] = task_dict[i[1]] + ' ; ' + i[0]
        else:
            task_dict[i[1]] = i[0]
    print('Результат:')
    for i in sorted(task_dict.items()):
        print(i[0], i[1])


tasks = Stack()
tasks.add_element("сделать уборку", 4)
tasks.add_element("помыть посуду", 4)
tasks.add_element("отдохнуть", 1)
tasks.add_element("поесть", 2)
tasks.add_element("сдать дз", 2)
manager_task(tasks)

print('Удаляем последнее выданое задание')
tasks.del_element()
manager_task(tasks)
