
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
def main():
    guitars = read_file()
    # original guitar
    guitar = [guitar for guitar in guitars]
    for c in guitar:
        print(c)
    print()
    # sort the guitar
    guitars.sort()
    guitar = [guitar for guitar in guitars]
    for a in guitar:
        print(a)
    get_valid_guitar_data(guitars)
    upload_file(guitars)


def read_file():
    guitars = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for i in in_file:
            parts = i.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[-1])
            guitars.append(Guitar(name, year, cost))
    return guitars


# Complete first part of More Guitars exercise
def get_valid_guitar_data(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost:$ "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")
    return guitars

def upload_file(guitars):
    with open(FILENAME, "w") as new_infile:
        for d in guitars:
            print(f"{d.name}, {d.year}, {d.cost}", file=new_infile)


main()

