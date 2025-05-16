#Object-Oriented Programming (OOP)

#class is a blueprint for creating objects 
class Calculator:
    #many functions (methods) as placed inside class. There is no strict limit on the number of methods a class can contain.
    def __init__(self, a, b): #constructor -- to initialize the instance attiribute -- there we can give parameters
        
        #self is essential for accessing instance-specific data and methods within a class.
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

calc = Calculator(10, 20)
print("The output for OOPS programming \n The sum of two digits will be , ", calc.add())