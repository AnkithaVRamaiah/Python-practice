# Global Scope Variable
print("Global Scope Varible")
a = 6
b = 4
def addition():
   r = a + b
   print("the value of addition is ", str(r))

def substraction():
    r = a - b
    print("the value of substraction is ", str(r))

addition()
substraction()

# Local Scope Variable
print(" Local Scope Varible")
def addition():
   a = 9
   b = 4
   r = a + b
   print("the value of addition is ", str(r))

def substraction():
   a = 1
   b = 9
   r = a - b
   print("the value of substraction is ", str(r))

addition()
substraction()