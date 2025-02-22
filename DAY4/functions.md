## **Understanding Functions in Python** 🚀

A **function** in Python is like a **machine** that takes some input, processes it, and gives back an output. It helps you **avoid repetition** and makes your code **organized and reusable**.

---

## **1️⃣ What is a Function?**
A function is a **block of code** that runs only when you call it.

### **Example**
Imagine a function as a **coffee machine**:
- You **give it input** (coffee beans, water, milk).
- It **processes** them.
- It **returns** coffee as output.

```python
def make_coffee():  # Defining a function
    print("☕ Here is your coffee!")

make_coffee()  # Calling the function
```
**Output:**
```
☕ Here is your coffee!
```

---

## **2️⃣ How to Create a Function?**
Use the `def` keyword, followed by the function name and parentheses `()`.

### **Syntax**
```python
def function_name():
    # Code inside the function
    print("Hello!")
```

### **Example**
```python
def greet():
    print("Hello, welcome to Python!")

greet()  # Calling the function
```
**Output:**
```
Hello, welcome to Python!
```

---

## **3️⃣ Function with Parameters (Inputs)**
A function can **take inputs (parameters)** to perform operations.

### **Example**
```python
def greet(name):  # name is a parameter
    print(f"Hello, {name}!")

greet("Alice")  # Passing "Alice" as an argument
greet("Bob")    # Passing "Bob" as an argument
```
**Output:**
```
Hello, Alice!
Hello, Bob!
```

---

## **4️⃣ Function with Return Value (Output)**
A function can return a **result** using the `return` keyword.

### **Example**
```python
def add(a, b):
    return a + b  # Returns the sum of a and b

result = add(5, 3)  # Storing the returned value in a variable
print(result)  # Output: 8
```
**Output:**
```
8
```

---

## **5️⃣ Default Parameter Values**
If you don’t pass a value, Python uses the **default value**.

### **Example**
```python
def greet(name="Guest"):  # Default value is "Guest"
    print(f"Hello, {name}!")

greet()       # No argument passed, uses default
greet("Eve")  # Argument passed, overrides default
```
**Output:**
```
Hello, Guest!
Hello, Eve!
```

---

## **6️⃣ Multiple Parameters**
You can pass multiple parameters **separated by commas**.

### **Example**
```python
def multiply(a, b, c):
    return a * b * c

result = multiply(2, 3, 4)
print(result)  # Output: 24
```
**Output:**
```
24
```

---

## **7️⃣ Function with Unlimited Arguments (`*args`)**
If you don’t know how many arguments will be passed, use `*args`.

### **Example**
```python
def sum_all(*numbers):  # Accepts multiple arguments
    return sum(numbers)

print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(10, 20, 30, 40))  # Output: 100
```
**Output:**
```
6
100
```

---

## **8️⃣ Function with Keyword Arguments (`**kwargs`)**
If you want to pass **named arguments**, use `**kwargs`.

### **Example**
```python
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="New York")
```
**Output:**
```
name: Alice
age: 25
city: New York
```

---

## **9️⃣ Lambda (Anonymous) Functions**
A **lambda function** is a small, one-line function.

### **Example**
```python
square = lambda x: x * x  # Function to square a number
print(square(5))  # Output: 25
```
**Output:**
```
25
```

---

## **🔟 Nested Functions (Function Inside Another Function)**
A function can be defined **inside another function**.

### **Example**
```python
def outer():
    print("This is the outer function.")

    def inner():
        print("This is the inner function.")

    inner()  # Calling inner function inside outer

outer()
```
**Output:**
```
This is the outer function.
This is the inner function.
```

---

## **✅ Summary**
| Feature | Description | Example |
|---------|-------------|---------|
| **Basic Function** | Code block that runs when called | `def greet(): print("Hi!")` |
| **Function with Parameter** | Takes input values | `def add(a, b): return a + b` |
| **Return Value** | Sends output back | `return result` |
| **Default Value** | Uses a default if no argument is given | `def greet(name="Guest")` |
| **Multiple Arguments** | Accepts multiple inputs | `def multiply(a, b, c): return a*b*c` |
| **`*args`** | Unlimited positional arguments | `def total(*nums): return sum(nums)` |
| **`**kwargs`** | Unlimited keyword arguments | `def display(**info): print(info)` |
| **Lambda Function** | Short function | `lambda x: x*x` |
| **Nested Function** | Function inside another function | `def outer(): def inner(): pass` |

---
### **🎯 Why Use Functions?**
✅ **Reusability** – Write once, use multiple times  
✅ **Organized Code** – Break code into smaller parts  
✅ **Reduces Errors** – Debug and fix easily  
✅ **Improves Readability** – Code is more structured  

---

## **💡 Practice Time!**

### **1️⃣ Function to Calculate the Square of a Number**
```python
def square(num):
    return num * num  # or num ** 2

print(square(5))  # Output: 25
print(square(10)) # Output: 100
```

---

### **2️⃣ Function to Return the Largest of Three Numbers**
```python
def largest(a, b, c):
    return max(a, b, c)  # Using the built-in max() function

print(largest(10, 25, 15))  # Output: 25
print(largest(5, 3, 8))     # Output: 8
```
**Alternative without `max()`**
```python
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(largest(10, 25, 15))  # Output: 25
print(largest(5, 3, 8))     # Output: 8
```

---

### **3️⃣ Function to Check if a Number is Even or Odd**
```python
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(4))  # Output: Even
print(even_or_odd(7))  # Output: Odd
```

---
