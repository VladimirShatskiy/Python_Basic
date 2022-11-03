def short_name(name):
    return (name[0] + '.')


date_out = []
file_source = open('first_tour.txt', 'r')
data_source = file_source.read()
file_source.close()

k = data_source.split()[0]

for i_str in data_source.split('\n'):
    if i_str.split()[0].isalpha() and i_str.split()[2] > k:
        date_out.append([short_name(i_str.split()[1]), i_str.split()[0], i_str.split()[2]])

data_sort = sorted(date_out, key=lambda x: x[2], reverse=True)

file_out = open('second_tour.txt', 'w')
file_out.write(str(len(data_sort)) + '\n')

for i_str in range(len(data_sort)):
    str_temp = (item for item in data_sort[i_str])
    file_out.write(f"{i_str + 1})")
    for item in data_sort[i_str]:
        file_out.write(f'\t {item}')
    file_out.write('\n')

file_out.close()