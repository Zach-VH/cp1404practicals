"""

Estimate: 80 minutes

Code:
Documentation:
Actual:
"""
from project import Project

DEFAULT_FILENAME = "project.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

def main():
    projects, header = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    #display_projects(projects)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = f"{input("Filename: ")}.txt"
            load_projects(filename)
        elif choice == "S":
            save_projects(projects,header)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            print("Filter selected")
        elif choice == "A":
            print("Add selected")
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid Input")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as in_file:
            header = in_file.readline().strip()
            for line in in_file:
                parts = line.strip().split(',')
                project = Project(parts[0],parts[1],int(parts[2]),float(parts[3]),float(parts[4]))
                projects.append(project)
        return projects, header
    except FileNotFoundError:
        print(f"{filename} does not exist")

def save_projects(projects,header):
    filename = input("Enter file name: ")
    if filename == "":
        filename = DEFAULT_FILENAME
    with open(f"{filename}.txt", 'w') as out_file:
        print(header, file=out_file)
        for project in projects:
            print(f"{project.name},{project.date},{project.priority},{project.cost},{project.completion}",file=out_file)
    print(f"Projects have been saved to {filename}.txt")

def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(f"  {project}")
    print("Complete projects:")
    for project in projects:
        if project.is_complete():
            print(f"  {project}")

def update_project(projects):
    for i, project in enumerate(projects,0):
        print(f"{i} {project}")
    try:
        project_index = int(input("Project choice: "))
        project = projects[project_index]
        print(project)
        updated_percentage = int(input("New percentage: "))
        project.completion = updated_percentage
    except ValueError:
        print("Input must be a integer")
    except IndexError:
        print("Choice is out of range of list")

main()