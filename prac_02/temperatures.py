MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
def main():
    """ convert the celsius to fahrenheit or conver fahrenheit to celsius"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_c_to_f(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_f_to_c(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_c_to_f(celsius):
    """calculate the fahrenheit depend on celsius"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_f_to_c(fahrenheit):
    """calculate the celsius depend on the value of fahrenheit"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()
