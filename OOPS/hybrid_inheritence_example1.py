# ------------------ INHERITANCE STRUCTURE ------------------
#
#        Person
#           |
#        Employee
#           |
#        TeamLead
#           |
#        Project
#
# TeamLead inherits from Employee and Project
# Employee already inherits from Person
# This combination is called HYBRID INHERITANCE
# -----------------------------------------------------------


# Base class
class Person:
    # Constructor to store the person's name
    def __init__(self, name):
        self.name = name



# Employee class inherits from Person
class Employee(Person):
    # Method to show role
    def role(self):
        print(self.name, "is an employee")


# Another independent class
class Project:
    # Method to store project name
    def project_details(self, project_name):
        self.project_name = project_name


# TeamLead inherits from Employee and Project
class TeamLead(Employee, Project):  # Hybrid Inheritance
    # Method to display project leadership details
    def details(self):
        print(self.name, "leads project:", self.project_name)


# ------------------ PROGRAM FLOW ------------------
#
# lead = TeamLead("Konda")
#       |
#       |-- Person.__init__() runs
#       |      self.name = "Konda"
#       |
# lead.role()
#       |
#       |-- prints employee role
#
# lead.project_details("MNC project")
#       |
#       |-- stores project name
#
# lead.details()
#       |
#       |-- prints project leadership details
# --------------------------------------------------


# Create object of TeamLead
lead = TeamLead("Konda")

# Call method from Employee class
lead.role()

# Call method from Project class
lead.project_details("MNC project")

# Call method from TeamLead class
lead.details()