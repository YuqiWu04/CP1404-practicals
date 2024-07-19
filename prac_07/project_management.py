from prac_07.project import Project
import datetime

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit ")
def main():
    print(MENU)
    file_name = FILENAME
    projects_data = read_file(file_name)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            load_file()
        elif choice == "S":
            user_input_filename = get_new_filename()
            save_project(projects_data, user_input_filename)
        elif choice == "D":
            display_projects(projects_data)
        elif choice == "F":
            filer_projects(projects_data)
        elif choice == "A":
            projects_data = add_project(projects_data)
        elif choice == "U":
            update_project(projects_data)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>>").upper()
    select_option_to_save(projects_data, FILENAME)
    print("Thank you for using custom-built project management software.")



def read_file(file_name):
    """open csv file and read this file"""
    projects_data = []
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
       in_file.readline()
       for i in in_file:
           parts = i.strip().split("\t")
           name = parts[0]
           start_date = parts[1]
           priority = parts[2]
           cost_estimate = parts[3]
           completion_percentage = parts[-1]
           projects_data.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects_data


def load_file():
    """load the file"""
    file_name = input("File Name:\n>>>")
    try:
        return read_file(file_name)
    except FileNotFoundError:
        print(f"file not found, using the default file: {FILENAME}")
        file_name = FILENAME
        return read_file(file_name)

def get_new_filename():
    """get the valid filename"""
    user_input_filename = input("You want to save in: ")
    if not user_input_filename.endswith(".txt"):
        user_input_filename += ".txt"
    return user_input_filename


def save_project(projects_data, user_input_filename):
    """save the project data into a new file"""
    with open(user_input_filename, "w") as new_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=new_file)
        for i in projects_data:
            print(f"{i.name}\t{i.start_date}\t{i.priority}\t{i.cost_estimate}\t{i.completion_percentage}", file=new_file)


def display_projects(projects_data):
    """display the project data """
    completed_projects = []
    uncompleted_projects = []
    for project in projects_data:
        if project.completion_percentage == 100:
            completed_projects.append(project)
        else:
            uncompleted_projects.append(project)
    completed_projects.sort()
    uncompleted_projects.sort()
    print("Incomplete projects:")
    for project in uncompleted_projects:
        print(project)

    print("Completed projects:")
    for project in completed_projects:
        print(project)


def add_project(projects_data):
    """add a new project"""
    print("Let's add a new project")
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = get_valid_data("Priority:")
    priority = int(priority)
    cost = get_valid_data("Cost estimate:$ ")
    completion_percentage = int(input("Percent complete: "))
    projects_data.append(Project(name, date, priority, cost, completion_percentage))
    return projects_data


def update_project(projects_data):
    """update the project"""
    index_number = 0
    for project in projects_data:
        index_number += 1
        print(f"{index_number-1} {project}")
    number = get_valid_number(projects_data)
    print(projects_data[number])
    new_percentage = int(input("New percentage: "))
    projects_data[number].completion_percentage = new_percentage
    new_priority = int(input("New Priority: "))
    projects_data[number].priority = new_priority
    print(projects_data[number])



def get_valid_number(projects_data):
    """get a valid number for priority """
    number = 0
    initial = False
    while not initial:
        try:
            number = int(input("Project choice: "))
            if number < 0 or number >= len(projects_data):
                print("Error")
            else:
                initial = True
        except ValueError:
            print("Please put correct number")
    return number


def filer_projects(projects_data):
    """filter projects by date"""
    new_projects = projects_data
    date_string = input("Date (d/m/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    new_projects.sort()
    for line in projects_data:
        start_date = datetime.datetime.strptime(line.start_date, "%d/%m/%Y").date()
        if start_date >= date:
            print(line)

def get_valid_data(prompt):
    """get a valid data for cost and priority"""
    data = 0
    initial = False
    while not initial:
        try:
            data = float(input(prompt))
            if data < 0:
                print("Error!")
            else:
                initial = True

        except ValueError:
            print("Please enter valid data")
    return data


def select_option_to_save(projects_data, file_name):
    """ask for user to save the data into defalt file"""
    user_input_filename = file_name
    option = input("Would you like to save to projects.txt? ").title()
    if option == "Y" or option == "Yes":
        save_project(projects_data, user_input_filename)


main()

