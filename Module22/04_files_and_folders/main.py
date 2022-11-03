import os

def file_list(way):
    for i_way in os.listdir(way):
        path = os.path.join(way, i_way)

        if os.path.isdir(path):
            list_branch['count_branch'] += 1
            file_list(path)
        else:
            list_branch['count_file'] += 1
            list_branch['size_branch'] += os.path.getsize(path)


list_branch = {'count_file': 0,
               'count_branch': 0,
               'size_branch': 0
               }

way = os.path.join('F:\\', 'Скачал')
file_list(way)
print(f"\n{way}\n"
      f"Размер каталога (в Мб): {list_branch['size_branch'] / 1024**2 :10,.2f}\n"
      f"Количество подкаталогов: {list_branch['count_branch']}\n"
      f"Количество фалов: {list_branch['count_file'] }")