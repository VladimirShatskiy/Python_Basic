def is_prime(number):
    if number > 1:
        count = 0
    else:
        count = 1
    for i in range(2, number):
        if number % i == 0:
            count += 1
    return (False if count != 0 else True)


def crypto(string):
    new_string = []
    for i in enumerate(string):
        if is_prime(i[0]):
            new_string += i[1]
    return new_string


