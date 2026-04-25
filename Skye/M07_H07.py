class Rectangle:
       ## Initializer method - set up the attributes for Car class
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        '''Instance method that returns the area'''
        self.area = self.height * self.width
        return f"The area is: {self.area}"
        
    def perimeter(self):
        '''Instance method that returns the perimeter'''
        self.perimeter = 2 * (self.height + self.width)
        return f"The perimeter is: {self.perimeter}" 
    
       

## Use case: Create an instance of the Rectangular class and call the area and perimeter methods to verify that they work correctly.
my_rectangle = Rectangle(4, 6)
print(my_rectangle.area())
print(my_rectangle.perimeter())

### Problem 2: Define a subclass called Square that 
# inherits from parent class Rectangle
# Using super(), will set .height and .width attributes from inherited superclass Rectangle.__init__()
class Square(Rectangle):
    def __init__(self, height, width):
        super().__init__(height, width)
        if self.height != self.width:
            raise ValueError ("Height and Width must match")

my_square = Square(4, 4)    
print(my_square.area())
print(my_square.perimeter())    

#my_square_err = Square(4, 6)

### Problem 3: Create a new class Cube that inherits from parent class Square
# Use super() to set .height and .width attributes from inherited superclass Square.__init__()
# Define new methods surface_area() and volume() that calculate the surface area and volume of the cube using the inherited attribute 

class Cube(Square):
    def __init__(self, height, width, length):
        super().__init__(height, width)
        self.length = length


    def surface_area(self):
        '''Instance method that returns the surface area'''
        self.surface_area = (2 * (self.height + self.width)) * 6
        return f"The surface area is: {self.surface_area}"

    def volume(self):
        '''Instance method that returns the volume'''
        self.volume = self.height * self.width * self.length
        return f"The volume is: {self.volume}"
    


my_cube = Cube(4, 4, 4)
print(my_cube.surface_area())
print(my_cube.volume())

# Do the Raise Errors also carry over from the parent class?
my_cube_err = Cube(4, 6, 4)

#test
print("This isn't working")