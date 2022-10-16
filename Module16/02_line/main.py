


short_class = list(range(160, 176 + 1, 2))
higt_class = list(range(162, 180 + 1, 3))
short_class.extend(higt_class)
short_class.sort()

print(f"Отсортированный список учеников: {short_class}")