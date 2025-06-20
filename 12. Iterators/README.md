# Iterators
An iterator is an object that contains a countable number of values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods `__iter__()` and `__next__()`.

## Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
```
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
```

## Create an Iterator
To create an object/class as an iterator you have to implement the methods `__iter__()` and `__next__()` to your object.
The `__iter__()` method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The `__next__()` method also allows you to do operations, and must return the next item in the sequence.