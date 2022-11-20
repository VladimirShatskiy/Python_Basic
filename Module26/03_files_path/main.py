# TODO здесь писать код
import os

find_branch = 'People Playground'

def get_files_path(way, st_word):
        for item in os.listdir(way):
                path = os.path.join(way, item)
                if not st_word:
                    if item == find_branch:
                        st_word = True
                    if os.path.isdir(path):
                        yield from get_files_path(path, st_word)
                    else:
                        yield path


str = get_files_path('F:\\Games', False)
for i in str:
    print(i)
