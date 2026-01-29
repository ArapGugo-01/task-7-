class Employee:
    # Parameterized constructor
    def __init__(self, name, age, service_year, salary):
        self.name = name
        self.age = age
        self.service_year = service_year
        self.salary = salary

    # Destructor
    def __del__(self):
        # Destructor (called when object is destroyed)
        pass

    # Accessor (Getter) methods
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getServiceYear(self):
        return self.service_year

    def getSalary(self):
        return self.salary


# Example usage
emp = Employee("John Doe", 35, 10, 75000.0)

print("Name:", emp.getName())
print("Age:", emp.getAge())
print("Service Years:", emp.getServiceYear())
print("Salary:", emp.getSalary())
