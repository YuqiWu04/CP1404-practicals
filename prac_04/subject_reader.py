"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """print several lines including name, year, number"""
    data = load_data()
    print(data)
    display_subject_detail(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    lines = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        lines.append(parts)
        # print(parts)  # See if that worked
    print(lines)
    print("----------")
    input_file.close()

    return lines

def display_subject_detail(data):
    """print several lines for subject details"""
    for pair in data:
        year, name, number = pair
        print(f"{year} is taught by {name:<12} and has {number:>6} students.")




main()