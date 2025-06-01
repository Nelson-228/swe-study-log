# Day 4 – For Loop Practice
# Purpose: Calculate total time for homework tasks using a for loop
# Author: Nelson Rueda
# Date: 2025-06-01

# === Get input from user ===
homework = int(input("How much homework do you have: "))
duration = int(input("How much is the estimated amount of time you will spend on each: "))

# === Initialize total time ===
total_time = 0

# === Use for loop to calculate total time ===
for i in range(homework):
    print(f"Currently on task {i + 1}...")
    total_time += duration

# === Final output ===
print(f"Total estimated time for every assignment: {total_time} minutes")
