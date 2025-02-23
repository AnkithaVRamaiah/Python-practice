### **🌍 Understanding Environment Variables in Python (Easy Explanation)**
Think of **environment variables** as a **hidden storage area** in your computer where you can save important settings like **passwords, API keys, or configuration values**. Instead of writing sensitive information **directly in your code**, you store it in the environment and access it when needed.

---

### **🔹 Why Use Environment Variables?**
✔️ **Security** – Keeps passwords and API keys out of your code.  
✔️ **Flexibility** – You can change configurations without modifying the code.  
✔️ **Portability** – Works across different machines (Dev, Testing, Production).

---

## **1️⃣ Using Environment Variables in Python**
Python provides the `os` module to work with environment variables.

### **👉 Example: Reading an Environment Variable**
```python
import os

# Get the value of an existing environment variable
home_directory = os.environ.get("HOME")  # Works on Linux/macOS
print(f"Your home directory is: {home_directory}")
```
🔹 This prints your home directory (`/home/username` on Linux, `C:\Users\username` on Windows).  

---

### **2️⃣ Creating and Using a Custom Environment Variable**
You can create your own environment variable and use it in Python.

#### **🔹 Step 1: Set an Environment Variable (Temporary)**
Run this command in your terminal (**before running your Python script**):

#### **On macOS/Linux:**
```sh
export MY_NAME="Alice"
```
#### **On Windows (Command Prompt):**
```sh
set MY_NAME=Alice
```
---

#### **🔹 Step 2: Read the Variable in Python**
```python
import os

# Read the environment variable
name = os.environ.get("MY_NAME")

print(f"Hello, {name}!")  # Output: Hello, Alice!
```
---

### **3️⃣ Using a `.env` File (Better Way)**
Instead of setting variables **manually every time**, we can store them in a `.env` file and load them using the `dotenv` library.

#### **🔹 Step 1: Install `python-dotenv`**
```sh
pip install python-dotenv
```

#### **🔹 Step 2: Create a `.env` File**
Create a file called **`.env`** in your project folder and add:
```
MY_SECRET_KEY=SuperSecret123
DATABASE_URL=mysql://user:password@localhost/dbname
```

#### **🔹 Step 3: Load and Use `.env` Variables in Python**
```python
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Read the variables
secret_key = os.getenv("MY_SECRET_KEY")
database_url = os.getenv("DATABASE_URL")

print(f"Secret Key: {secret_key}")
print(f"Database URL: {database_url}")
```
---

### **📌 Summary**
| **Method**          | **Description** |
|---------------------|---------------|
| `os.environ.get("VAR")` | Read environment variable |
| `os.environ["VAR"] = "value"` | Set environment variable temporarily |
| `.env + dotenv` | Store and load variables from a file |

---

### **🛠 Practice Task**
✅ Create a `.env` file with:  
```
API_KEY=12345abcde
```
✅ Write a Python script that prints `API_KEY` using `dotenv`.  
