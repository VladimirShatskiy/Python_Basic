def write_file(name_file, base):
    with open(name_file, 'w') as file_out:
        for item in base:
            file_out.write(item + '\n')

def test_name(name):
    return str.isalpha(name)

def test_email(email):
    if '@' in email and '.' in email:
        return True
    return False

def test_age(age):
    if 10 <= int(age) <= 99:
        return True
    return False


registrations_good, registrations_bad = [], []
err_str = ''

with open('registrations.txt', 'r', encoding='utf-8') as file_source:
    email_books = file_source.read().split('\n')

for entry in email_books:
    err_str = ''
    try:
        if len(entry.split()) != 3:
            raise IndexError
        else:
            try:
                if not test_name(entry.split()[0]):
                    raise NameError
            except NameError:
                err_str += '"Поле «Имя» содержит НЕ только буквы" '
            try:
                if not test_email(entry.split()[1]):
                    raise SyntaxError
            except SyntaxError:
                err_str += '"Поле «Имейл» НЕ содержит @ и . (точку)" '
            try:
                if not test_age(entry.split()[2]):
                    raise ValueError
            except ValueError:
                err_str += '"Поле «Возраст» НЕ является числом от 10 до 99" '
    except IndexError:
        err_str += '"НЕ присутствуют все три поля" '
        # format_bad_str(entry, err_str)

    if err_str == '':
        registrations_good.append(entry)
    else:
        registrations_bad.append(entry + ' ' * (40 - len(entry)) + err_str)

write_file('registrations_good.log', registrations_good)
write_file('registrations_bad.log', registrations_bad)
