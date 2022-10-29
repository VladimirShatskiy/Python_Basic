site = {
	'html': {'head': {'title': 'Мой сайт'},'body': {'h2': 'Здесь будет мой заголовок','div': 'Тут, наверное, какой-то блок','p': 'А вот здесь новый абзац'}}}


def search_key(date, srth_key, deep):
	if deep <= 0:
		return None

	if srth_key in date.keys():
		return date[srth_key]

	for item in date.values():
		if isinstance(item, dict):
			result = search_key(item, srth_key, deep - 1)
			if result:
				break
	else:
		result = None
	return result


srth_key = input("введи ключ: ")

if input("Хотите ввести максимальную глубину? Y/N: ").lower() == "y":
	deep = int(input("Введите максимальную глубину: "))
else:
	deep = 1000000000

print(search_key(site, srth_key, deep))