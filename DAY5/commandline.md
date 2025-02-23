### **📌 Understanding Command Line Arguments in Python**
Command-line arguments allow you to pass inputs to a Python script **when running it from the terminal**. Python provides the `sys` and `argparse` modules to handle these arguments.

---

## **✅ Method 1: Using `sys.argv` (Basic)**
The `sys.argv` list stores command-line arguments passed to the script.

### **Example 1️⃣: Print Command Line Arguments**
```python
import sys

# Print all command-line arguments
print("Arguments passed:", sys.argv)

# Print the first argument (excluding script name)
if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])
```

### **🔹 Running the Script**
```sh
python script.py Hello
```
🔹 **Output**:
```
Arguments passed: ['script.py', 'Hello']
First argument: Hello
```

📌 **Key Notes:**
- `sys.argv[0]` → Always the script name.
- `sys.argv[1]` → First argument.
- Arguments are treated as **strings**.

---

## **✅ Method 2: Using `argparse` (Recommended)**
For better argument parsing, use `argparse`.

### **Example 2️⃣: Parse Arguments with `argparse`**
```python
import argparse

# Create parser
parser = argparse.ArgumentParser(description="Process some numbers.")

# Add arguments
parser.add_argument("num1", type=int, help="First number")
parser.add_argument("num2", type=int, help="Second number")
parser.add_argument("--operation", choices=["add", "sub"], default="add", help="Operation to perform")

# Parse arguments
args = parser.parse_args()

# Perform operation
if args.operation == "add":
    result = args.num1 + args.num2
else:
    result = args.num1 - args.num2

print(f"Result: {result}")
```

### **🔹 Running the Script**
```sh
python script.py 10 5 --operation add
```
🔹 **Output**:
```
Result: 15
```

📌 **Key Features of `argparse`**:
- Allows **positional arguments** (`num1`, `num2`).
- Supports **optional arguments** (`--operation`).
- Provides **help messages** when running `python script.py --help`.

---

### **✅ Summary of Key Commands**
| **Command** | **Purpose** |
|------------|------------|
| `sys.argv` | Basic method to access arguments as a list. |
| `argparse.ArgumentParser()` | Recommended method for structured argument handling. |
| `parser.add_argument()` | Defines the expected command-line arguments. |
| `parser.parse_args()` | Parses arguments from the command line. |

---

### **🎯 Next Steps**
1️⃣ Modify the `argparse` script to support multiplication and division.  
2️⃣ Try adding **default values** and **error handling** for missing arguments.  

