def qHofm(list_in, depth: int) -> None:
    if list_in != [1, 1]: return None
    yield list_in[0]
    yield list_in[1]
    temp_list = list_in
    for i in range(2, depth):
        temp_item = (temp_list[i - temp_list[i-1]] + temp_list[i - temp_list[i-2]])
        yield temp_item
        temp_list.append(temp_item)


start_list = [1, 1]
sequence = qHofm(start_list, 30)
print(list(sequence))