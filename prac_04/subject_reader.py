"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
subjects = []


def main():
    get_data(subjects)
    display_subject_details()


def get_data(subject):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject += [parts]
    input_file.close()
    print(subject)


def display_subject_details():
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students.")



main()
