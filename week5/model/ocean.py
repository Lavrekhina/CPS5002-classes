import random
from environment import Environment
from simulation_constants import GRID_COLS, GRID_ROWS
from week5.model.location import Location


class Ocean(Environment):
    """
    The Ocean class represents the environment (grid) where agents live and move.
    Each cell in the grid can contain either an Agent (like a Shark) or None (empty water).
    """

    def __init__(self, cols, rows):
        """
        Initialize the Ocean with a specified number of columns and rows.

        Args:
            cols (int): The number of columns in the grid.
            rows (int): The number of rows in the grid.
        """
        self.__cols = cols
        self.__rows = rows

        # Create a 2D grid (list of lists) initialized with None (empty spaces)
        self.__grid = [[None for _ in range(cols)] for _ in range(rows)]

    def clear(self):
        """
        Remove all agents from the grid, resetting the ocean to an empty state.
        """
        self.__grid = [[None for _ in range(self.__cols)] for _ in range(self.__rows)]

    def get_agent(self, location):
        """
        Retrieve the agent at a specific location in the grid.

        Args:
            location (Location): The grid position to check.

        Returns:
            Agent or None: The agent at that location, or None if empty.
        """
        return self.__grid[location.get_y()][location.get_x()]

    def set_agent(self, agent, location):
        """
        Place an agent at a specific grid location.

        Args:
            agent (Agent or None): The agent to place (or None to clear the cell).
            location (Location): The grid position where to place the agent.
        """
        self.__grid[location.get_y()][location.get_x()] = agent

    def get_height(self):
        """
        Get the total number of rows (height) of the ocean grid.
        """
        return self.__rows

    def get_width(self):
        """
        Get the total number of columns (width) of the ocean grid.
        """
        return self.__cols

    def find_free_adjacent_locations(self, location):
        """
        Find all free (empty) adjacent cells surrounding a given location.

        Args:
            location (Location): The current position of the agent.

        Returns:
            list[Location]: A list of adjacent free locations.
        """
        # Possible movements (8 directions: N, NE, E, SE, S, SW, W, NW)
        offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        free_locations = []

        # Check each possible offset around the current location
        for dx, dy in offsets:
            new_x = location.get_x() + dx
            new_y = location.get_y() + dy

            # Verify that the new position is within grid boundaries
            if 0 <= new_x < self.__cols and 0 <= new_y < self.__rows:
                # Check if the position is empty (no agent there)
                if self.__grid[new_y][new_x] is None:
                    free_locations.append(Location(new_x, new_y))

        return free_locations

    def __str__(self):
        """
        Return a string representation of the ocean grid.
        Useful for visualizing the environment in the console.
        """
        output = ""
        for row in self.__grid:
            line = ""
            for cell in row:
                # Represent occupied cells (with an agent) as 'S', empty cells as '.'
                line += "S " if cell is not None else ". "
            output += line + "\n"
        return output
