# Day 4 – While Loop Practice
# Purpose: Count from 1 to a user-defined limit using a while loop
# Author: Nelson Rueda
# Date: 2025-06-01

# === Get user-defined limit ===
limit = int(input("Give me a number that I will count up to: "))

# === Initialize starting number ===
starting_number = 1

# === Count using while loop ===
while starting_number <= limit:
    print("Number:", starting_number)
    starting_number += 1

# === End message ===
print(f"I successfully counted up to {limit}. Have a great day!")
