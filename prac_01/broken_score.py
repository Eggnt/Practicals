"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = int(input("Enter score: "))
if score < 0 or score > 100:
    category = "invalid"
elif score > 90:
    category = "excellent"
elif score > 50:
    category = "passable"
else:
    category = "bad"
print(f"Your score is {category}.")
