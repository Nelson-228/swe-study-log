# Day 2 – Python Variables & Arithmetic
# Purpose: Perform arithmetic operations based on user input and selected operator
# Author: Nelson Rueda
# Date: 2025-06-01

# === Get numbers from user ===
a = float(input("Enter your first number here: "))
b = float(input("Enter your second number here: "))

# === Choose operation ===
equation = input("What would you like to do with these two numbers: +, -, *, / ")

# === Perform operation ===
if equation == "+":
    print(a + b)
elif equation == "-":
    print(a - b)
elif equation == "*":
    print(a * b)
elif equation == "/":
    print(a / b)
else:
    print("Please input the correct math sign! Thank you.")

# === Exit message ===
print("Have a great day, User! :)")
