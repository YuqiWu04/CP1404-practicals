from prac_06.guitar import Guitar
guitars = []
TITLE = "My guitars!"
print(TITLE)
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost:$ "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar.name} ({guitar.year}): ${guitar.cost:,.2f} added")
    name = input("Name: ")
max_name_length = max([len(guitar.name) for guitar in guitars])
max_year_length = max([len(str(guitar.year)) for guitar in guitars])
max_cost_length = max([len(str(f"{guitar.cost:,.2f}")) for guitar in guitars])
# Iterate through the list of guitars and include the index number
for i, guitar in enumerate(guitars, 1):
    # Return a string if the value of is_vintage() is True otherwise empty
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year:>{max_year_length}}), worth ${guitar.cost:>{max_cost_length},.2f} {vintage_string} ")