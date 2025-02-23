### **Operators in Python (Simplified Explanation)**  
Operators in Python are symbols that perform operations on variables and values.  

---

## **1️⃣ Arithmetic Operators**
Used for basic math operations.  

| Operator | Description | Example |
|----------|------------|---------|
| `+` | Addition | `5 + 3 → 8` |
| `-` | Subtraction | `5 - 3 → 2` |
| `*` | Multiplication | `5 * 3 → 15` |
| `/` | Division | `5 / 2 → 2.5` |
| `//` | Floor Division (removes decimal) | `5 // 2 → 2` |
| `%` | Modulus (remainder) | `5 % 2 → 1` |
| `**` | Exponentiation (power) | `2 ** 3 → 8` |

### **Example:**
```python
a = 10
b = 3
print(a + b)  # 13
print(a // b) # 3 (removes decimal)
print(a ** b) # 1000 (10³)
```

---

## **2️⃣ Comparison Operators**  
Used to compare values and return `True` or `False`.

| Operator | Description | Example |
|----------|------------|---------|
| `==` | Equal to | `5 == 5 → True` |
| `!=` | Not equal to | `5 != 3 → True` |
| `>` | Greater than | `5 > 3 → True` |
| `<` | Less than | `5 < 3 → False` |
| `>=` | Greater than or equal to | `5 >= 5 → True` |
| `<=` | Less than or equal to | `3 <= 5 → True` |

### **Example:**
```python
x = 10
y = 5
print(x > y)  # True
print(x == y) # False
```

---

## **3️⃣ Logical Operators**  
Used to combine conditions.

| Operator | Description | Example |
|----------|------------|---------|
| `and` | Returns `True` if **both** conditions are true | `(5 > 3 and 10 > 5) → True` |
| `or` | Returns `True` if **at least one** condition is true | `(5 > 3 or 10 < 5) → True` |
| `not` | Reverses the result | `not(5 > 3) → False` |

### **Example:**
```python
a = True
b = False
print(a and b) # False
print(a or b)  # True
print(not a)   # False
```

---

## **4️⃣ Assignment Operators**  
Used to assign values to variables.

| Operator | Example | Equivalent to |
|----------|---------|--------------|
| `=`  | `x = 5` | Assigns 5 to x |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |

### **Example:**
```python
x = 10
x += 5  # x = x + 5 → 15
x *= 2  # x = x * 2 → 30
print(x)  # 30
```

---

### **Bitwise Operators in Python (Explained in Detail)**
Bitwise operators are used to perform operations on individual **bits** (binary digits) of numbers. These operations are useful in **low-level programming**, **cryptography**, **compression**, and **networking**.

Each number in a computer is represented in binary (0s and 1s). **Bitwise operators manipulate these bits directly**.

---

## **1️⃣ Bitwise AND (`&`)**
- Performs a **bitwise AND** operation between two numbers.
- The result is **1** only if both bits are **1**, otherwise, it’s **0**.

### **Example:**
```python
a = 5  # Binary:  101
b = 3  # Binary:  011

print(a & b)  # Output: 1 (Binary: 001)
```
**Explanation:**
```
   101   (5 in binary)
&  011   (3 in binary)
------------
   001   (1 in binary)
```
Only the last bit is **1**, so the result is `1` (decimal).

---

## **2️⃣ Bitwise OR (`|`)**
- Performs a **bitwise OR** operation between two numbers.
- The result is **1** if at least one of the bits is **1**.

### **Example:**
```python
a = 5  # Binary:  101
b = 3  # Binary:  011

print(a | b)  # Output: 7 (Binary: 111)
```
**Explanation:**
```
   101   (5 in binary)
|  011   (3 in binary)
------------
   111   (7 in binary)
```
Since at least one bit is **1** in each position, the result is `7` (decimal).

---

## **3️⃣ Bitwise XOR (`^`)**
- Performs a **bitwise XOR (exclusive OR)** operation.
- The result is **1** if the bits are different, otherwise **0**.

### **Example:**
```python
a = 5  # Binary:  101
b = 3  # Binary:  011

print(a ^ b)  # Output: 6 (Binary: 110)
```
**Explanation:**
```
   101   (5 in binary)
^  011   (3 in binary)
------------
   110   (6 in binary)
```
Only the **different** bits become `1`, so the result is `6` (decimal).

---

## **4️⃣ Bitwise NOT (`~`)**
- Flips all the bits of a number.
- Inverts `1` to `0` and `0` to `1`.
- The result is **negative** due to **two’s complement representation**.

### **Example:**
```python
a = 5  # Binary:  101

print(~a)  # Output: -6
```
**Explanation (in an 8-bit system for better visualization):**
```
   00000101   (5 in binary)
~  11111010   (-6 in two's complement)
```
The `~` operator flips the bits and represents the negative value.

💡 **Note:** The actual output is `-(n+1)`. So `~5` becomes `-(5+1) = -6`.

---

## **5️⃣ Left Shift (`<<`)**
- Moves all bits **left by a given number of places**.
- **Multiplies** the number by `2^n`.

### **Example:**
```python
a = 5  # Binary:  101

print(a << 1)  # Output: 10 (Binary: 1010)
print(a << 2)  # Output: 20 (Binary: 10100)
```
**Explanation:**
```
   101   (5 in binary)
<< 1 (Shift left by 1 place)
------------
  1010   (10 in binary)
```
Each shift **doubles** the number:
- `5 << 1` → `5 * 2^1 = 10`
- `5 << 2` → `5 * 2^2 = 20`

---

## **6️⃣ Right Shift (`>>`)**
- Moves all bits **right by a given number of places**.
- **Divides** the number by `2^n`.

### **Example:**
```python
a = 5  # Binary:  101

print(a >> 1)  # Output: 2 (Binary: 10)
print(a >> 2)  # Output: 1 (Binary: 1)
```
**Explanation:**
```
   101   (5 in binary)
>> 1 (Shift right by 1 place)
------------
   10    (2 in binary)
```
Each shift **halves** the number:
- `5 >> 1` → `5 / 2^1 = 2`
- `5 >> 2` → `5 / 2^2 = 1`

---

## **6️⃣ Membership Operators**  
Check if a value is in a sequence.

| Operator | Description | Example |
|----------|------------|---------|
| `in` | Checks if a value exists in a sequence | `'a' in 'apple' → True` |
| `not in` | Checks if a value **does not** exist in a sequence | `'z' not in 'apple' → True` |

### **Example:**
```python
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
print("grape" not in fruits)  # True
```

---

## **7️⃣ Identity Operators**  
Check if two objects are **same in memory**.

| Operator | Description | Example |
|----------|------------|---------|
| `is` | Returns `True` if two variables refer to **same object** | `a is b` |
| `is not` | Returns `True` if two variables refer to **different objects** | `a is not b` |

### **Example:**
```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # True (same memory)
print(x is z)  # False (different memory)
```

---

## **🎯 Summary**
- **Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical**: `and`, `or`, `not`
- **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`
- **Bitwise**: `&`, `|`, `^`, `~`, `<<`, `>>`
- **Membership**: `in`, `not in`
- **Identity**: `is`, `is not`
### **Relational Operators in Python (Comparison Operators)**  
Relational operators **compare two values** and return a **Boolean result** (`True` or `False`). These operators are used in **conditional statements, loops, and logical operations**.

---

## **1️⃣ Equal to (`==`)**  
- Checks if two values are **equal**.
- Returns **True** if they are the same, otherwise **False**.

### **Example:**
```python
a = 10
b = 10
c = 5

print(a == b)  # True (because 10 is equal to 10)
print(a == c)  # False (because 10 is not equal to 5)
```

---

## **2️⃣ Not Equal to (`!=`)**  
- Checks if two values are **not equal**.
- Returns **True** if they are different, otherwise **False**.

### **Example:**
```python
x = 7
y = 5

print(x != y)  # True (because 7 is not equal to 5)
print(x != 7)  # False (because 7 is equal to 7)
```

---

## **3️⃣ Greater than (`>`)**  
- Checks if the left value is **greater than** the right value.
- Returns **True** if the left value is larger, otherwise **False**.

### **Example:**
```python
x = 15
y = 10

print(x > y)   # True (because 15 is greater than 10)
print(y > x)   # False (because 10 is not greater than 15)
```

---

## **4️⃣ Less than (`<`)**  
- Checks if the left value is **smaller than** the right value.
- Returns **True** if the left value is smaller, otherwise **False**.

### **Example:**
```python
a = 3
b = 8

print(a < b)   # True (because 3 is less than 8)
print(b < a)   # False (because 8 is not less than 3)
```

---

## **5️⃣ Greater than or Equal to (`>=`)**  
- Checks if the left value is **greater than or equal to** the right value.
- Returns **True** if the left value is either greater than **or** equal to the right value.

### **Example:**
```python
x = 10
y = 10
z = 5

print(x >= y)  # True (10 is equal to 10)
print(x >= z)  # True (10 is greater than 5)
print(z >= x)  # False (5 is not greater than or equal to 10)
```

---

## **6️⃣ Less than or Equal to (`<=`)**  
- Checks if the left value is **less than or equal to** the right value.
- Returns **True** if the left value is either less than **or** equal to the right value.

### **Example:**
```python
a = 4
b = 4
c = 9

print(a <= b)  # True (4 is equal to 4)
print(a <= c)  # True (4 is less than 9)
print(c <= a)  # False (9 is not less than or equal to 4)
```

---

## **🔥 Quick Summary**
| Operator | Description | Example | Output |
|----------|------------|---------|--------|
| `==` | Equal to | `10 == 10` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `7 > 3` | `True` |
| `<` | Less than | `2 < 5` | `True` |
| `>=` | Greater than or equal to | `8 >= 8` | `True` |
| `<=` | Less than or equal to | `4 <= 9` | `True` |
