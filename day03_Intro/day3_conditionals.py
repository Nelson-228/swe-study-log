# Day 3 – Python Conditionals
# Purpose: Grade evaluator using if/elif/else and user input
# Author: Nelson Rueda
# Date: 2025-06-01

# Ask user for their name and test score
name = input("What is your first name: ")
score = float(input(f"Hello {name}! What is your test score for your assignment? (0–100): "))

# === Determine letter grade based on score ===
if score >= 90:
    print(f"Congrats {name}! You got an A! Keep up the good work!")
elif score >= 80:
    print(f"Congrats {name}! You got a B! Great job!")
elif score >= 70:
    print(f"You got a C. Not bad, {name}, but there is room for improvement.")
elif score >= 60:
    print(f"You got a D. You should review more of the material to improve your grade for the next exam, {name}. You got this!")
else:
    print(f"You got an F. Consider getting help from your professor but don't be too hard on yourself. Failure is when you give up!")

# End message
print("Done evaluating your grade!")
