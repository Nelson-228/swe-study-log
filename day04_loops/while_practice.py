# Creating a variable that receives the user's input that will limit the loop to a specific number
limit = int(input("Give me a number that I will count up to: "))

# Variable that declares the start of the number
starting_number = 1

# While this loop is going, it will count down starting from the "starting_number", while adding +1 until it reaches the limit number, then breaks.
while starting_number <= limit:
    print("Number", starting_number)
    starting_number += 1

# Displays output to user that the system successfully did a countdown to its requested number
print(f"I successfully counting up to {limit}. Have a great day!")
