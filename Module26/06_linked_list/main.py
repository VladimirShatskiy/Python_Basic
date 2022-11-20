from typing import Any, Optional
class Node:
    """
    Элемент списка
    """
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        """
        head - Начальный элемент списка
        count - счетчик количества элементов в списке
        """
        self.head = None
        self.count_element = 0

    def __str__(self):
        """
        Печать списка
        :return: str - вывод списка при его наличии
        """
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return f'{values}'
        return 'Список пуст'

    def append(self, item: Optional[Any]) -> None:
        """
        Добавление элемента в список

        :param item: Any
        :return: None
        """
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.count_element += 1

    def get(self, index: int):
        """
        :param index: номер элемента в списке с 0
        :return: None
        """

        if self.count_element >= index >= 0:
            count = 0
            elem = self.head
            for _ in range(index):
                elem = elem.next
                count += 1
            return f'{elem.value}'
        else:
            raise IndexError

    def remove(self, index) -> None:
        """
        Удаляет элемент из списка
        :param index: int позиция элемента для удаления из списка
        :return:
        """
        cur_node = self.head
        if self.count_element >= index >= 0:
            if index == 0:
                self.head = cur_node.next
                self.count_element -= 1
            else:
                for _ in range(index):
                    temp_node = cur_node
                    cur_node = cur_node.next
                temp_node.next = cur_node.next
                self.count_element -= 1
        else:
            raise IndexError


new_list = LinkedList()
new_list.append(10)
new_list.append(20)
new_list.append(30)
new_list.append(40)
new_list.append(50)
new_list.append(60)
print(new_list)
print(new_list.get(3))
new_list.remove(5)
print(new_list)
new_list.remove(4)
print(new_list)
