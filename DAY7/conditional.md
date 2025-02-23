## **Conditional Handling in Python (if-else statements)**
Conditional handling allows Python to make **decisions** based on conditions. It helps control the flow of execution by running different code blocks depending on whether a condition is **True or False**.

---

## **1️⃣ if Statement**
The `if` statement **executes a block of code only if a condition is True**.

### **Syntax:**
```python
if condition:
    # Code to execute if the condition is True
```

### **Example:**
```python
age = 18

if age >= 18:
    print("You are eligible to vote.")  # This runs because 18 >= 18
```

**🔹 Output:**  
```
You are eligible to vote.
```

---

## **2️⃣ if-else Statement**
The `else` block **executes if the condition in the if statement is False**.

### **Syntax:**
```python
if condition:
    # Code if condition is True
else:
    # Code if condition is False
```

### **Example:**
```python
temperature = 25

if temperature > 30:
    print("It's a hot day.")
else:
    print("The weather is cool.")
```

**🔹 Output:**  
```
The weather is cool.
```

---

## **3️⃣ if-elif-else (Multiple Conditions)**
Use `elif` to check **multiple conditions**.

### **Syntax:**
```python
if condition1:
    # Code if condition1 is True
elif condition2:
    # Code if condition2 is True
else:
    # Code if none of the above conditions are True
```

### **Example:**
```python
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")
```

**🔹 Output:**  
```
Grade: B
```

---

## **4️⃣ Nested if Statements**
An `if` statement inside another `if` statement is called **nested if**.

### **Example:**
```python
num = 10

if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
```

**🔹 Output:**  
```
Positive number
Even number
```

---

## **5️⃣ Short-hand if and if-else (Ternary Operator)**
Python allows short-hand notation for simple conditions.

### **Short-hand if**
```python
x = 5
if x > 0: print("Positive number")
```

**🔹 Output:**  
```
Positive number
```

### **Short-hand if-else (Ternary Operator)**
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

**🔹 Output:**  
```
Adult
```

Here are the Python programs for your three tasks:

---

### **1️⃣ Check if a number is Positive, Negative, or Zero**
```python
# Take input from the user
num = float(input("Enter a number: "))

# Check conditions
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")
```
**🔹 Example Output:**
```
Enter a number: -5
The number is Negative.
```

---

### **2️⃣ Check Age Category (Child, Teenager, or Adult)**
```python
# Take user age as input
age = int(input("Enter your age: "))

# Check age category
if 0 <= age <= 12:
    print("You are a Child.")
elif 13 <= age <= 19:
    print("You are a Teenager.")
elif age >= 20:
    print("You are an Adult.")
else:
    print("Invalid age entered!")
```
**🔹 Example Output:**
```
Enter your age: 15
You are a Teenager.
```

---

### **3️⃣ Check if a Year is a Leap Year**
A leap year is:
- Divisible by 4 **AND** (not divisible by 100 **OR** divisible by 400).

```python
# Take user input for the year
year = int(input("Enter a year: "))

# Check if it is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")
```
**🔹 Example Output:**
```
Enter a year: 2024
2024 is a Leap Year.
```