"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_details = load_data(FILENAME)
    display_subject_details(subject_details)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    data=[]
    for line in input_file:
        parts = line.strip().split(',')  # Remove the \n & Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data

def display_subject_details(subject_details):
    """Print the subject details in a proper sentence form"""
    subject_width = max(len(parts[0]) for parts in subject_details)
    lecturer_width = max(len(parts[1]) for parts in subject_details)
    student_count_width = max(len(str(parts[2])) for parts in subject_details)

    for subject, lecturer, student_count in subject_details:
        print(f"{subject:{subject_width}} is taught by {lecturer:{lecturer_width}} and has {student_count:{student_count_width}} students")

main()