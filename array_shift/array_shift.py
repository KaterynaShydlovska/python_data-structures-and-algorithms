l=[4,8,15,23,42]
b = 16

l_two=[2,4,6,8] 
c = 5

def middle_l(l,b):
  middle = len(l) // 2
  if len(l) % 2 == 0:

    return l[:middle] + [b] + l[middle:]
  else:
    return l[:middle + 1] + [b] + l[middle +1:]

print(middle_l(l, b))
print(middle_l(l_two, c))