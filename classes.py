class Employee:
    # class variables
    company_name = 'ABC Company'

    # constructor to initialize the object
    def __init__(self, name, salary):
        # instance variables
        self.name = name
        self.__salary = salary
        

    # instance method
    def show(self):
        print('Employee:', self.name, self.__salary, self.company_name)

# create first object
emp1 = Employee("Harry", 12000)
emp1.show()

# create second object
emp2 = Employee("Emma", 10000)
emp2.show()
print(emp2._Employee__salary)

# class Circle(Employee):
class Circle():
    
    pi = 3.14

    def __init__(self, redius):
        self.radius = redius

    def calculate_area(self):
        print("Area of circle :", self.pi * self.radius * self.radius)


a=Circle(100)

a.calculate_area

def area(shape):
    # call action
    shape.calculate_area()

# create object
cir = Circle(5)

# call common function
area(cir)

