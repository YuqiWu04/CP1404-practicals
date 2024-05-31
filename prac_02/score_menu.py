
def main():
    """choose the option to select different function
    including input the score, print the category of score, and print the times of '*'"""
    menu = "MENU:\n(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars (this should print as many stars as the score)\n(Q)uit"
    print(menu)
    score = ""
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score == "":
                print("Error message!")
            else:
                result = determine_score(score)
                print(result)
        elif choice == "S":
            if score == "":
                print("Error message!")
            else:
                print_stars(score)
        else:
            print("Error message")
        print(menu)

        choice = input("Enter your choice: ").upper()
    print("Finished!")

def get_valid_score():
    """get valid score number and use the error checking"""
    value = float(input("Enter the number(0-100): "))
    while value < 0 or value > 100:
        print("Invalid score!")
        value = float(input("Enter the number(0-100): "))
    return value


def determine_score(score):
    """determine the category of score"""
    if score < 50:
        message = "Bad"
    elif score < 90:
        message = "Passable"
    else:
        message = "Excellent"
    return message


def print_stars(score):
    """print the times of *"""
    for i in range(int(score)):
        print("*", end=" ")
main()