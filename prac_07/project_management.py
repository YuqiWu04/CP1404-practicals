from prac_07.project import Project


FILENAME = "projects.txt"
MENU: str = """(L)oad projects 
(S)ave Projects
(D)isplay projects
(F)ilter projects by date
(A)dd new project
(U)pdate project
(Q)uit"""
def main():
    print(MENU)
    file_name = FILENAME
    projects_data = read_file(file_name)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            load_file()
        elif choice == "S":
            save_project(projects_data)
        elif choice == "D":
            display_projects(projects_data)
        # elif choice == "F":
        #     filer_projects()
        elif choice == "A":
            projects_data = add_project(projects_data)
        elif choice == "U":
            update_project(projects_data)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>>").upper()
    print("Thank you for using custom-built project management software.")



def read_file(file_name):
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
    file_name = input("File Name:\n>>>")
    try:
        return read_file(file_name)
    except FileNotFoundError:
        print(f"file not found, using the default file: {FILENAME}")
        file_name = FILENAME
        return read_file(file_name)

def get_new_filename():
    user_input_filename = input("You want to save in: ")
    if not user_input_filename.endswith(".txt"):
        user_input_filename += ".txt"
    return user_input_filename


def save_project(projects_data):
    user_input_filename = get_new_filename()
    with open(user_input_filename, "w") as new_file:
        for i in projects_data:
            print(f"{i.name}\t{i.start_date}\t{i.priority}\t{i.cost_estimate}\t{i.completion_percentage}", file=new_file)


def display_projects(projects_data):
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
    print("Let's add a new project")
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority:"))
    cost = float(input("Cost estimate:$ "))
    completion_percentage = int(input("Percent complete: "))
    projects_data.append(Project(name, date, priority, cost, completion_percentage))
    return projects_data


def update_project(projects_data):
    index_number = 0
    for project in projects_data:
        index_number += 1
        print(f"{index_number-1} {project}")
    number = int(input("Project choice: "))


    new_percentage = int(input("New percentage: "))
    projects_data[number].completion_percentage = new_percentage
    new_priority = int(input("New Priority: "))
    projects_data[number].priority = new_priority
    print(projects_data[number])

main()