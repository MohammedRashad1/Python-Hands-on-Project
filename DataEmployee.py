class Employee:
    count = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count += 1

    def displayCount(self):
        print("There are %d employees" % Employee.count)

    def displayDetails(self):
        print("Name:", self.name, ", position:", self.position, ", salary:", self.salary)


emp1 = Employee("Employee1", "HR", 30000)
emp2 = Employee("Employee2", "Manger", 70000)
emp3 = Employee("Employee3", "Programmer", 50000)
emp4 = Employee("Employee4", "Engineer", 60000)
emp5 = Employee("Employee5", "Security", 12000)
emp6 = Employee("Employee6", "Accountant", 15000)
emp2.displayCount()

print("**Information about Employee**")
emp1.displayDetails()
emp2.displayDetails()
emp3.displayDetails()
emp4.displayDetails()
emp5.displayDetails()
emp6.displayDetails()
        