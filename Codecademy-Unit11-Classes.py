# This file contains code written for Unit 11 an Introduction to Classes

# Instantiating My First Object

class Animal(object):
    def __init__(self,name):
        self
        self.name = name

zebra = Animal("Jeffrey")

print zebra.name

# Shopping cart example

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Brad")

my_cart.add_item("Hotdog",50)

# Inheritance example with employee

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")

print milton.full_time_wage(10)

# Triangle project example

class Triangle(object):
    number_of_sides = 3
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

my_triangle = Triangle(90,30,60)

print my_triangle.number_of_sides
print my_triangle.check_angles()
