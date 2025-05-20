# Asks user for two numbers
a = float(input("Enter your first number here: "))
b = float(input("Enter your second numnber here: "))

# Basic math is done here such as addition, subtraction, multiplication and division
equation = input("What would you like to do with these two numbers: +, -, *, / ")
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

print("Have a great day, User! :)")
