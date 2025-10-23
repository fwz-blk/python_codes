# Question 2: Class with Constructor

# Create a Circle class with:
# Attribute: radius
# Method: area() that returns area of the circle (π*r*r
# Method: perimeter() that returns perimeter (2*π*r)

# Task:
# Create a circle object with radius 5
# Print its area and perimeter

class Circle:
    
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        r=self.radius
        return 3.14*r*r
    
    def perimeter(self):
        r=self.radius
        return 2*3.14*r
    

c=Circle(5)   

print(c.area())
print(c.perimeter())



