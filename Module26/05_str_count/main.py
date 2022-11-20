
import os

way = 'C:\\Users\\Ирина\\PycharmProjects\\Python_Basic\\Python_Basic\\Python_Basic\\module20'

def str_count_file(way: str, file_name: str):
    """
    :return: int Общее количество строк без бустых и строк с комментариями
    """
    count = 0
    with open(os.path.join(way, file_name), 'r', encoding='utf-8') as file_open:
        str = file_open.read()
    for i in str.split('\n'):
        if len(i) != 0 and not '#' in i:
            count += 1
    return count


def file_search(way):
    for item in os.listdir(way):
        path = os.path.join(way, item)
        if not os.path.isdir(path):
            if '.py' in item:
                n_str = str_count_file(way, item)
                yield n_str

        else:
            yield from file_search(path)


count = file_search(way)

print(f'Количество строк в файлах: {sum(list(count))}\n')






