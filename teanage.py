teaneger_ages=[13,15,14,17,18,19,16,13,15]
print(teaneger_ages)
print("slicing a list ",teaneger_ages[:6])
# changge a list 
teaneger_ages[3]=26
print('updated list',teaneger_ages)
print(len(teaneger_ages))

# adding new items in list
teaneger_ages.append(11)
# append adds new item at the end
print(teaneger_ages)
teaneger_ages.insert(5,17)
# insert( ) is used to add new item in specific index
print(teaneger_ages)
print(len(teaneger_ages))
# removin a list  using remove()
teaneger_ages.remove(13)
# the romove method removes a specified item
print('removed  13',teaneger_ages)
teaneger_ages.pop(8)
# The pop() method removes the specified index.
print('remove index 8',teaneger_ages)
teaneger_ages.pop()
print('removes the last item',teaneger_ages)
teaneger_ages.sort()
print(teaneger_ages)
for age in teaneger_ages:
  if age>=18:
   print('you are adult',age)
  # print(age)

