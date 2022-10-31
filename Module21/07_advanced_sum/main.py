def fun_sum(list_num):
  summ = 0
  for i_num in (list_num):
    if isinstance(i_num, int):
      summ += i_num
    elif isinstance(i_num, list):
      summ += fun_sum(i_num)
  return summ


print(fun_sum([[1, 2, [3]], [1], 3]))





