def find_item(element, string, str_rep):
    if string in element.keys():
        element[string] = str_rep
        return element[string]

    for level1 in element.values():
        if isinstance(level1, dict):
            str_for_change = find_item(level1, string, str_rep)
            if str_for_change:
                break
    else:
        return

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


for i_site in range(int(input("Сколько сайтов "))):
    print("Введите название продукта для нового сайта: ", end = "")
    brend = input()
    title_str = "Куплю/продам {tel} недорого ".format(tel=brend)
    h2_str = "У нас самая низкая цена на {tel}".format(tel=brend)
    find_item(site, 'title', title_str)
    find_item(site, 'h2', h2_str)
    print(f"\nсайт для {brend} \n {site}")