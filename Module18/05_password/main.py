num_count, up_count = 0, 0

while True:
  passw=input("Придумайте пароль: ")

  for simbol in passw:
    if simbol.isdigit():
      num_count += 1
    if simbol.isupper():
      up_count += 1

  if len(passw) >= 8 and up_count >= 1 and num_count >= 3:
    break

print("Это надежный пароль")

