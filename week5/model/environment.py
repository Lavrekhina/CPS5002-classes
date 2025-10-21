from abc import ABC, abstractmethod

class Environment(ABC):
    """
    Abstract base class for environments where agents live and interact.
    Subclasses (like Ocean) must implement these methods.
    """

    @abstractmethod
    def clear(self):
        """
        Remove all agents from the environment, resetting it to an empty state.
        """
        pass

    @abstractmethod
    def get_agent(self, location):
        """
        Retrieve the agent at a given location.

        Args:
            location: A Location object specifying the position in the environment.

        Returns:
            The agent at the given location, or None if empty.
        """
        pass

    @abstractmethod
    def set_agent(self, agent, location):
        """
        Place an agent at a specific location, or remove it (if agent is None).

        Args:
            agent: An instance of an Agent or None to clear the cell.
            location: The Location where to place the agent.
        """
        pass

    @abstractmethod
    def get_height(self):
        """
        Return the number of rows (height) of the environment grid.
        """
        pass

    @abstractmethod
    def get_width(self):
        """
        Return the number of columns (width) of the environment grid.
        """
        pass
