"""
Project management program
90 minutes, 11:35 a.m.
"""
import csv
from prac_07.project import Project

MENU = f"- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n- (F)ilter projects by date\n" \
       f"- (A)dd new project  \n- (U)pdate project\n- (Q)uit\n>>> "


def main():
    choice = input(MENU).upper()
    projects = load_file('projects.txt')
    while choice != "Q":
        # if choice == "L":
        # in_file = input("Please enter the name of the file you wish to load: ")
        # projects = load_file(in_file)
        if choice == "S":
            save_name = input("Please enter the name of the file you wish to save to: ")
            save_projects_file(projects, save_name)
        elif choice == "D":
            sorted_projects = sorted(projects)
            print("Incomplete Projects:")
            print_projects_of_completion(sorted_projects, False)
            print("Completed Projects:")
            print_projects_of_completion(sorted_projects, True)
        # elif choice == "F":
        #
        elif choice == "A":
            get_new_project(projects)
        elif choice == "U":
            updated_project = ""
            updated_percentage = ""
            updated_priority = ""
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            updated_project = determine_integer_validity(updated_project, "Project Choice: ")
            updated_percentage = determine_integer_validity(updated_percentage, "New Percentage: ")
            updated_priority = determine_integer_validity(updated_priority, "New Priority: ")
            projects[updated_project].update(updated_priority, updated_percentage)
        else:
            print("Invalid menu choice")
        choice = str(input(MENU)).upper()


def get_new_project(projects):
    name = str(input("Name: "))
    start_date = input("Start date: ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Estimated cost: "))
    completion_percentage = int(input("Completion percentage: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def print_projects_of_completion(projects, complete):
    for project in projects:
        if project.is_complete() is complete:
            print(project)


def save_projects_file(projects, save_name):
    out_file = open({save_name}, 'w')
    for project in projects:
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t"
              f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)
    out_file.close()


def load_file(in_file):
    projects = []
    file = open(f'{in_file}', 'r', newline="")
    file.readline()
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        project = Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4]))
        projects.append(project)
    file.close()
    return projects


def determine_integer_validity(potential_integer, input_prompt):
    """Checks if an integer is valid by making sure it is the correct type (int), then returns the integer"""
    valid = False
    while not valid:
        try:
            potential_integer = int(input(f"{input_prompt}"))
            valid = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return potential_integer


main()
