file_source = open('text.txt', 'r')
data_source = file_source.read()
file_source.close()
alfa = {}
count = 0

for item in data_source.lower():
    if item.isalpha():
        if item in alfa.keys():
            alfa[item] += 1
            count += 1
        else:
            alfa[item] = 1
            count += 1

alfa_sort = dict(sorted(alfa.items(), key=lambda items: items[0], reverse=False))
alfa_sort1 = dict(sorted(alfa_sort.items(), key=lambda items: items[1], reverse=True))

file_out = open('analysis.txt', 'w')
for i_key, i_value in alfa_sort1.items():
    file_out.write(f'{i_key} {i_value / count :5.3f} \n')

file_out.close()
