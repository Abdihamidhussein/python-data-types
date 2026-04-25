num=(1,2,3,4,5,5,6)
print(type(num))
# accessing tuble by index
print(num[1:4])
print(num[-1])
# count is used to count 
print(num.count(5))

print(num.index(5))
# unpacking a tuple
x,y ,*z=num
# * means normaly w
print('x',x,'y',y ,'z',z)
print(z)

print(num)