"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid message")
    score = float(input("Enter score: "))
if score < 50:
    message = "Bad"
elif score < 90:
    message = "Passable"
else:
    message = "Excellent"
print(message)
