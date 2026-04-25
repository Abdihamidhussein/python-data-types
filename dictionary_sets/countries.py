counrtries={
  "country":"somalia",
  "capital": "mogadishu",
  "papulation": 20000000,
  "continent": "africa",
  "religion": "islam",
  "indepident": 1960,
}
#  access all keys and values
print(counrtries)
# access values
print(counrtries.values())
# access keys only
print(counrtries.keys())
# access all keys and values by for loop
for x,y in counrtries.items():
  print(x,y)
  # changing a dictionary
counrtries["papulation"]=22000000
print(counrtries)
# change a distionary using update method
counrtries.update( {"papulatin": 20000000})
print(counrtries)
# adding new key and values
counrtries["president"]="Hassan sheikh mohamud"
print(counrtries)
# you can use update ( ) to add a new item
# counrtries.update({"president":"Hassan sheikh mohamud"})
# removiin item in dictionary
counrtries.pop("president")
print(counrtries)
#  also you can use pop item while pop item removes last item
# counrtries.get("religion")
# search item using get method
print(counrtries.get("president"))

