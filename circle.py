
#Creation of Class
import math
class Circle:
    def __init__(self,radius):
        a = radius
        self.radius = radius
# creation of Area and Circumference#
    def area_of_circle(self):
        area_of_circle = self.radius**2*math.pi
        return area_of_circle
    def circumference_of_circle(self):
        circumference_of_circle = 2*math.pi*self.radius
        return circumference_of_circle
#creation of while loop#
while True:
    usr_input=(float(input("Please input radius\n")))
    radius = usr_input 
    radius = Circle(radius)
    a = radius.area_of_circle()
    b = radius.circumference_of_circle()
    print(f'the area is {a}and the circumference is {b}')



