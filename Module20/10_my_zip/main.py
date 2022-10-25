def min_value(num1, num2):
    return min(len(num1), len(num2))


def my_zip(letter, number):
    new = ((letter[item], number[item]) for item in range(min_value(letter, number)))
    return new


number = (10, 20, 30, 40, 50, 60, 70)
letter = "abcd"

new = my_zip(letter, number)
print(new)
for item in new:
    print(item)

