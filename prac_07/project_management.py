"""
Project management program
90 minutes, 11:35 a.m.
"""
import csv
import datetime
from prac_07.project import Project

MENU = f"- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n- (F)ilter projects by date\n" \
       f"- (A)dd new project  \n- (U)pdate project\n- (Q)uit\n>>> "


def main():
    projects = []
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            in_file = input("Please enter the name of the file you wish to load: ")
            projects = load_file(in_file)
        elif choice == "S":
            save_name = input("Please enter the name of the file you wish to save to: ")
            save_projects_file(projects, save_name)
        elif choice == "D":
            if len(projects) > 0:
                sorted_projects = sorted(projects)
                print("Incomplete Projects:")
                print_projects_of_completion(sorted_projects, False)
                print("Completed Projects:")
                print_projects_of_completion(sorted_projects, True)
            else:
                print("No projects to display. Choose 'A' to add more projects or 'L' to load an existing file.")
        elif choice == "F":
            given_date = input("Show projects that start after date (dd/mm/yy): ")
            for project in projects:
                if given_date <= project.start_date:
                    print(project)
        elif choice == "A":
            get_new_project(projects)
        elif choice == "U":
            if len(projects) > 0:
                updated_project = ""
                updated_percentage = ""
                updated_priority = ""
                for i, project in enumerate(projects):
                    print(f"{i} {project}")
                updated_project = determine_range_validity(updated_project, 0, (len(projects) - 1), "Project Choice: ")
                updated_percentage = determine_range_validity(updated_percentage, 0, 100, "New Percentage: ")
                updated_priority = determine_integer_validity(updated_priority, "New Priority: ")
                projects[updated_project].update(updated_priority, updated_percentage)
            else:
                print("No projects to update.")
        else:
            print("Invalid menu choice")
        choice = str(input(MENU)).upper()
    print("Thank you for using custom-built project management software.")


def get_new_project(projects):
    name = ""
    start_date = ""
    priority = ""
    cost_estimate = ""
    completion_percentage = ""
    name = determine_name_validity(name, "Name: ")
    start_date = input("Start date: ")
    priority = determine_integer_validity(priority, "Priority: ")
    cost_estimate = determine_float_validity(cost_estimate, "Estimated cost: ")
    completion_percentage = determine_integer_validity(completion_percentage, "Completion percentage: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def print_projects_of_completion(projects, complete):
    for project in projects:
        if project.is_complete() is complete:
            print(project)


def save_projects_file(projects, save_name):
    out_file = open(save_name, 'w')
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
        row[1] = datetime.datetime.strptime(row[1], "%d/%m/%Y").date()
        row[1] = row[1].strftime("%d/%m/%Y")
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


def determine_float_validity(potential_float, input_prompt):
    """Checks if an integer is valid by making sure it is the correct type (int), then returns the integer"""
    valid = False
    while not valid:
        try:
            potential_float = float(input(f"{input_prompt}"))
            valid = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return potential_float


def determine_range_validity(potential_integer, minimum, maximum, input_prompt):
    """Checks if an integer is within a certain range"""
    valid = False
    while valid is False:
        potential_integer = determine_integer_validity(potential_integer, input_prompt)
        if minimum <= potential_integer <= maximum:
            valid = True
        else:
            print(f"The number must be between {minimum} and {maximum}")
    return potential_integer


def determine_name_validity(potential_name, input_prompt):
    """Checks if a name is valid by making sure it is not blank then returns the name"""
    valid = False
    while not valid:
        for letter in potential_name:
            if not letter.isspace():
                valid = True
        if not valid:
            print("Input can not be blank")
            potential_name = str(input(f"{input_prompt}"))
    return potential_name


main()
