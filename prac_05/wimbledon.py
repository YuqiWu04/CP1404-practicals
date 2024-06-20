import csv
filename = "wimbledon.csv"
year_to_data = {}
datas = []
def main():
    """display the winner name and the times of country"""
    year_to_data = read_file()
    winner_detail, names = display_name(year_to_data)
    name_time = count_name_times(names)
    display_data(name_time)
    country = count_winner_country(winner_detail)
    number = count_country_number(country)
    display_winner_country(number, country)


def read_file():
    """read the file from a csv and put the detail into the dictionary"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for data in reader:
            datas.append(data)
            year_to_data[data[0]] = data[1:-1]
    return year_to_data



def display_name(year_to_data):
    """show the no.1 name and winner details"""
    winner_detail = list(year_to_data.values())
    names = []
    for i in winner_detail:
        names.append(i[1])
    return winner_detail, names

def count_name_times(names):
    """calculate the name times"""
    name_to_count = {}
    for name in names:
        if name in name_to_count:
            name_to_count[name] += 1
        else:
            name_to_count[name] = 1
    return name_to_count



def display_data(name_to_count):
    """display the name and count"""
    for name, count in name_to_count.items():
        print(f"{name} {count}")


#
def count_winner_country(winner_detail):
    """display the No.1 winner for the country"""
    country = set()
    for i in winner_detail:
        country.add(i[0])
    country = sorted(country)
    return country

def count_country_number(country):
    """calculate the country number """
    number = len(country)
    return number


def display_winner_country(number, country):
    """display the winner country"""
    print(f"These {number} countries have won Wimbledon: ")
    country = ", ".join(country)
    print(f"{country}")


main()
