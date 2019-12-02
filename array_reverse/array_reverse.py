new_list = []
def list_rev():
  i = len(list) - 1
  while i >= 0:
    new_list.append(list[i])
    i -= 1
  print(new_list)