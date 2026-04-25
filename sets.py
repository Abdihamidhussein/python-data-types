set_a={1,2,3,4,5,6}
set_b={5,6,7,8}
# cheking a number is in the set or not
print(7 in set_a)
if 6 in set_b:
  print(6 ,'is in the set')
else:
  print('not found')
#  adding and removing sets
set_a.add(9)
set_a.discard(9)

print(type(set_a))
print("seta union set b", set_a | set_b)
