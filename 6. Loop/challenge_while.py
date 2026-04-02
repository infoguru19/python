"""
1. Create a variable i with the value 0
2. Write a while loop that runs as long as i is less than 6
3. Inside the loop: increment i by 1
4. If i equals 3, use continue to skip that iteration
5. Print i 
""""

# Create the i variable
i = 0
# While loop: print 1-5, skip 3 with continue
while i < 6:
  i += 1
  print(i)
  if i == 3:
    continue
