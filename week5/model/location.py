class Location:

    def __init__(self, x, y):
        """
        Initialize a Location object with specified x and y coordinates.

        Args:
            x (int): The x-coordinate of the location.
            y (int): The y-coordinate of the location.
        """
        self.__x = x
        self.__y = y

    def get_x(self):
        """
        Get the x-coordinate of the location.
        """
        return self.__x

    def get_y(self):
        """
        Get the y-coordinate of the location.
        """
        return self.__y

    def set_x(self, new_x: int):
        """
        Set the x-coordinate to a new value.
        """
        self.__x = new_x

    def set_y(self, new_y: int):
        """
        Set the y-coordinate to a new value.
        """
        self.__y = new_y

    def equals(self, other_location: "Location"):
        """
        Compare this location with another location.
        """
        if self.__x == other_location.get_x() and\
                self.__y == other_location.get_y():
            return True
        return False

    def __str__(self):
        """
        Return a string representation of the location.
        """
        return f"Location ({self.__x}, {self.__y})"