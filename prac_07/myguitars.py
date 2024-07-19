import csv
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






main()

