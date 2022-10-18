err = False

ip = input("Введи IP: ")

ip_conf =ip.split(".")

if len(ip_conf) != 4:
    print("Адрес — это четыре числа, разделённые точками.")
else:
    for item in ip_conf:
        if not item.isdigit():
            print(f"{item} - это не целое число")
            err = True
        elif not 0 < int(item) < 255:
            print(f"{int(item)} превышает 255")
            err = True
    if not err:
            print("IP-адрес корректен.")