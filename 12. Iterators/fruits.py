fruittuple = ("apple", "banana", "cherry")
myit = iter(fruittuple)

print(next(myit))  # Output: apple
print(next(myit))  # Output: banana
print(next(myit))  # Output: cherry

# Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))