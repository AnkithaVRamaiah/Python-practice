# 📦 **Understanding Packages in Python**  

A **package** in Python is a **collection of modules** organized in directories. It helps structure your code, making it more readable and reusable. Think of a package as a **folder** that contains multiple related Python files (modules), just like a folder on your computer that holds documents.

---

## 🔹 **What is a Package?**
A **package** is simply a **directory (folder)** that contains an `__init__.py` file and multiple **modules**.

📂 **Example Package Structure:**
```
my_package/          # This is a package (a folder)
│-- __init__.py      # This makes it a package
│-- module1.py       # A module inside the package
│-- module2.py       # Another module inside the package
```

### **Why Use Packages?**
✅ **Code Organization** – Keeps related modules together  
✅ **Reusability** – Allows easy import and reuse of code  
✅ **Avoids Name Conflicts** – Helps prevent module name clashes  
✅ **Scalability** – Makes large projects easier to manage  

---

## 🔹 **How to Create a Package in Python**
Follow these steps to create and use a package:

### **Step 1: Create a Package (Folder)**
Create a folder **`my_package`** that will act as a package.

### **Step 2: Add an `__init__.py` File**
Inside `my_package`, create an empty file named `__init__.py`.  
This file tells Python that this folder should be treated as a package.

### **Step 3: Create Modules Inside the Package**
Now, add two module files inside `my_package`:  
📜 **`module1.py`**
```python
# module1.py
def greet(name):
    return f"Hello, {name}!"
```

📜 **`module2.py`**
```python
# module2.py
def add(a, b):
    return a + b
```

---

## 🔹 **How to Import and Use a Package**
Now, let's use the **package and its modules** in another script.

📜 **`main.py`**
```python
# Import specific functions from modules inside the package
from my_package.module1 import greet
from my_package.module2 import add

# Using the functions
print(greet("Alice"))    # Output: Hello, Alice!
print(add(5, 3))         # Output: 8
```

### **Alternative: Import the Whole Module**
Instead of importing specific functions, you can import the entire module:
```python
import my_package.module1
import my_package.module2

print(my_package.module1.greet("Bob"))  # Output: Hello, Bob!
print(my_package.module2.add(10, 2))    # Output: 12
```

---

## 🔹 **Using `__init__.py` for Package-Level Imports**
You can define what gets imported when using `from my_package import *` by modifying `__init__.py`.

📜 **`__init__.py`**
```python
from .module1 import greet
from .module2 import add
```

Now, you can simply write:
```python
from my_package import greet, add

print(greet("Charlie"))  # Output: Hello, Charlie!
print(add(7, 4))         # Output: 11
```

---

## 🔹 **Installing and Using Third-Party Packages**
Python allows installing external packages using **pip**.

### **Example: Installing the `requests` Package**
```sh
pip install requests
```
Then, use it in Python:
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200
```

---

## **✅ Summary**
| Feature | Description | Example |
|---------|-------------|---------|
| **Package** | A folder containing multiple modules | `my_package/` |
| **Module** | A single `.py` file with functions & classes | `module1.py` |
| **`__init__.py`** | Marks a directory as a package | `__init__.py` (empty or with imports) |
| **Import a Module** | Import a specific module from a package | `from my_package import module1` |
| **Import a Function** | Import only a function from a module | `from my_package.module1 import greet` |
| **Third-Party Packages** | Install external packages using pip | `pip install requests` |

---

## **🎯 Practice Task**

## **Step 1: Create a Package Named `math_operations`**
1. Create a folder called **`math_operations/`**.
2. Inside this folder, create an empty file named **`__init__.py`** (this makes it a package).

📂 **Folder Structure**
```
math_operations/       # Package folder
│-- __init__.py        # Makes it a package
│-- calculator.py      # Module with math functions
main.py                # Main script to use the package
```

---

## **Step 2: Create `calculator.py` with Functions**
Inside **`math_operations/`**, create a file **`calculator.py`** and define the following functions:

📜 **`calculator.py`**
```python
# calculator.py - Module inside math_operations package

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b
```

---

## **Step 3: Import and Use These Functions in `main.py`**
Now, create a new file **`main.py`** (outside the `math_operations` folder) and import the functions:

📜 **`main.py`**
```python
# main.py - Importing functions from the math_operations package

from math_operations.calculator import add, subtract, multiply, divide

# Testing the functions
num1 = 10
num2 = 5

print("Addition:", add(num1, num2))        # Output: 15
print("Subtraction:", subtract(num1, num2)) # Output: 5
print("Multiplication:", multiply(num1, num2)) # Output: 50
print("Division:", divide(num1, num2))     # Output: 2.0
```

---

## **Step 4: Run `main.py`**
Now, run the script:
```sh
python main.py
```
✅ **Expected Output:**
```
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

---

### **🎯 Bonus Challenge**
✔ Modify `__init__.py` to automatically import the functions:
📜 **`__init__.py`**
```python
from .calculator import add, subtract, multiply, divide
```
Now, in `main.py`, you can simply write:
```python
from math_operations import add, subtract, multiply, divide
```
This keeps your import clean and makes your package more user-friendly! 🚀

