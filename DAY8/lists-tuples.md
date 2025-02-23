### **Lists and Tuples in Python** 🐍

Both **lists** and **tuples** are used to store multiple values in Python, but they have some key differences.

---

## **🔹 Lists in Python**
A **list** is an **ordered, mutable** (changeable) collection that can store different data types.

### ✅ **Key Features of Lists:**
- **Ordered**: Elements maintain the order they were added.
- **Mutable**: You can change, add, or remove items.
- **Allows duplicates**: Can contain duplicate values.

### **📌 Creating a List**
```python
# Creating a list
fruits = ["apple", "banana", "cherry", "banana"]

print(fruits)  # Output: ['apple', 'banana', 'cherry', 'banana']
```

### **📌 Accessing Elements**
```python
print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: banana (last item)
```

### **📌 Modifying Lists**
```python
fruits[1] = "mango"  
print(fruits)  # Output: ['apple', 'mango', 'cherry', 'banana']
```

### **📌 Adding & Removing Elements**
```python
fruits.append("orange")  # Adds to the end
fruits.insert(1, "grape")  # Inserts at index 1
print(fruits)  # Output: ['apple', 'grape', 'mango', 'cherry', 'banana', 'orange']

fruits.remove("banana")  # Removes the first occurrence
del fruits[2]  # Removes item at index 2
print(fruits)  
```

### **📌 Looping through a List**
```python
for fruit in fruits:
    print(fruit)
```

---

## **🔹 Tuples in Python**
A **tuple** is an **ordered, immutable** (unchangeable) collection.

### ✅ **Key Features of Tuples:**
- **Ordered**: Elements maintain their order.
- **Immutable**: Cannot be modified after creation.
- **Faster than lists**: Useful when data should not change.

### **📌 Creating a Tuple**
```python
numbers = (1, 2, 3, 4, 5)
print(numbers)  # Output: (1, 2, 3, 4, 5)
```

### **📌 Accessing Elements**
```python
print(numbers[0])  # Output: 1
print(numbers[-1]) # Output: 5
```

### **📌 Looping through a Tuple**
```python
for num in numbers:
    print(num)
```

### **📌 Tuple Packing & Unpacking**
```python
person = ("John", 30, "Engineer")  # Packing

name, age, profession = person  # Unpacking
print(name)      # Output: John
print(age)       # Output: 30
print(profession)  # Output: Engineer
```

---

## **🔹 List vs Tuple (Differences)**

| Feature      | List (`[]`)        | Tuple (`()`)  |
|-------------|------------------|--------------|
| **Mutable**  | ✅ Yes (can change) | ❌ No (cannot change) |
| **Ordered**  | ✅ Yes  | ✅ Yes  |
| **Performance** | Slower | Faster (due to immutability) |
| **Methods Available** | More (append, remove, etc.) | Fewer |
| **Use Case** | When data needs modification | When data should remain constant |

---

## **🔹 When to Use What?**
✔ **Use a List when** you need to modify data (e.g., user lists, tasks, logs).  
✔ **Use a Tuple when** you need fixed data (e.g., coordinates, months of the year).
