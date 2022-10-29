def tower(n, disk_from, mid, disk_targ):
    if n == 1:
        return print(f"Переложить диск {n} со стержня номер {disk_from} на стержень с номером {disk_targ}")
    else:
        tower(n - 1, disk_from, disk_targ, mid)
        print(f"Переложить диск {n} со стержня номер {disk_from} на стержень с номером {disk_targ}")
        tower(n - 1, mid, disk_from, disk_targ)


tower(int(input("Введите количество дисков ")), "1", "2", "3")
