from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
def main():
    """the whole option which is about choosing taxi and drive how far to drive"""
    total_cost = 0.0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            current_taxi = choice_taxi(taxis)
        elif choice =="D":
            if current_taxi==None:
                print("You need to choose a taxi before you can drive")
            else:
                current_cost = drive_taxi(current_taxi)
                total_cost += current_cost
                print(f"Your {current_taxi.name} cost you ${current_cost:.2f}")
        else:
            print("Invalid choice!")
        print(f"Bill to date:{total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finish")


def choice_taxi(taxis):
    """choose a taxi from some a list by select index number"""
    print("Taxi available:")
    for index_number, taxi in enumerate(taxis):
        print(f"{index_number} - {taxi}")
    option_number = int(input("Choose taxi: "))
    if option_number >= 0 and option_number < len(taxis):
        return taxis[option_number]
    else:
        print("Invalid taxi choice")
        return None
def drive_taxi(current_taxi):
    """drive some distance and finally get some cost"""
    distance = int(input("Drive how far? "))
    current_taxi.drive(distance)
    current_taxi.get_fare()
    return current_taxi.get_fare()



main()