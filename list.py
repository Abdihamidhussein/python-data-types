africa_capitals=[  "Nairobi",
    "Accra",
    "Cairo",
    "Addis Ababa",
    "Dakar",
    "Algiers",
    "Kampala",
    "Rabat",
    "Luanda",
    "Pretoria"
]
# totall lengh of list
print(len(africa_capitals))
# accessing list items by using index starting 0
print(africa_capitals[ -1 ])
print(africa_capitals[2 : 6])
for city in africa_capitals:
  print(city)
  # changing list items
africa_capitals[1:2]=["mogadishu", "DJbouti"]
print(africa_capitals)
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
africa_capitals.insert(1, 'acra')
print(africa_capitals)

print(africa_capitals)