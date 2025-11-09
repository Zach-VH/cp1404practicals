"""
Project Class
"""

class Project:
    def __init__(self, name="",date="",priority=0,cost=0.0,completion=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __repr__(self):
        return (f"{self.name}, start:{self.date}, priority {self.priority}, estimated: ${self.cost:.2f}, "
                f"completion: {self.completion}%")

    def is_complete(self):
        if self.completion == 100:
            return True
        else:
            return False

def run_tests():
    projects = []
    with open("project.txt", 'r') as in_file:
        header = in_file.readline().strip()
        for line in in_file:
            parts = line.strip().split(',')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)
    print(projects)
    print(f"Completed:{[project for project in projects if project.is_complete()]}")

run_tests()