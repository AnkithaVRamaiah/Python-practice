import sys
import os

# Custom environment variable
name = os.environ.get("MY_NAME")

if name:
    print(f"Hello, {name}")
else:
    print("Environment variable MY_NAME is not set!")

# before running the script set environment variable: export MY_NAME="YourName"
# runscript: python cal.py 8 add 7
# output: Hello, Ankitha
# output: 15.0

def add(num1, num2):
    return num1 + num2
    
num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    result = add(num1, num2)
    print("Addition of two numbers is:", result)