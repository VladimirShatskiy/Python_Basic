new_list = []
def summ(*qwer):
    fun_sum(list(qwer)[0])
    print(sum(new_list))

def fun_sum(list_num):
    for i_num in list_num:
        if isinstance(i_num, int):
            new_list.append(i_num)
        elif isinstance(i_num, list):
            fun_sum(i_num)
    return




summ([[1, 2, [3]], [1], 3])





