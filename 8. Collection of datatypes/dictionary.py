# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(type(thisdict))

print(thisdict.get("model"))

x = thisdict["year"]
print(x)

for x in thisdict:
    print(x)            # print Key
    print(thisdict[x])  # Print value

for x in thisdict.keys():
    print(x)

for x in thisdict.values():
    print(x)

