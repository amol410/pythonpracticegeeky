class Rectangle:
    def __init__(self, width, height):
        self._width = width    # Private attribute
        self._height = height  # Private attribute

    # Accessor methods (getter methods)
    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    # Method to calculate area
    def calculate_area(self):
        return self._width * self._height


# Creating an instance of the Rectangle class
rectangle = Rectangle(5, 3)

# Accessing attributes using accessor methods
print("Width:", rectangle.get_width())    # Output: Width: 5
print("Height:", rectangle.get_height())  # Output: Height: 3

# Calculating area
print("Area:", rectangle.calculate_area())  # Output: Area: 15
