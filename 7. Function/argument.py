def name(fname, lname):
  print(fname + " "+lname)
name("ravi", "ranjan")

# Defult Argument
def name(fname = "ravi", lname = "raj"):
  print(fname + " "+lname)
name()
name("John", "Rocky")
