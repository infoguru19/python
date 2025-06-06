class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = myNumbers()
myiter = iter(myclass)
print(next(myiter))  # Output: 1
print(next(myiter))  # Output: 2
print(next(myiter))  # Output: 3
print(next(myiter))  # Output: 4