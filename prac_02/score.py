import random
def main():
    """the whole process to determine the score category depend on user's input and random number"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid message")
        score = float(input("Enter score: "))
    category = determine_score(score)
    print(category)
    random_score = random.randint(0, 100)
    print(f"Random number: {random_score}")
    category = determine_score(random_score)
    print(category)


def determine_score(score):
    """determined the score category"""
    if score < 50:
        message = "Bad"
    elif score < 90:
        message = "Passable"
    else:
        message = "Excellent"
    return message

main()
