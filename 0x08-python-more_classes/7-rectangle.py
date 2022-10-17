#!/usr/bin/python3
class Rectangle:
    """Represents a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the data."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Delete a rectangle."""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """Print the rectangle."""
        string = ''
        if self.__width == 0 or self.__height == 0:
            return string
        string += ((str(self.print_symbol) * self.__width + '\n') *
                   self.__height)
        return string[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return ('Rectangle(' + str(self.__width) + ', ' +
                str(self.__height) + ')')

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
