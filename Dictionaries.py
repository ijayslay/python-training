thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(thisdict["brand"])

#Accessing Dict
x = thisdict["model"]

#change Dict
thisdict["year"] = 2018

#add dict element
thisdict["color"] = "red"
print(thisdict)

#second dict
thisdict2 = {
  "brand": "Audi",
  "model": "xtron",
  "year": 2002
}

print(thisdict2)

# Merge two Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Nested Dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])