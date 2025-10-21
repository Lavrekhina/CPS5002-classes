from abc import ABC, abstractmethod

class Agent(ABC):
    """
    Abstract base class representing an agent in an environment.
    Each agent has a location and can perform actions (act) within the environment.
    """

    def __init__(self, location):
        """
        Initialize the agent with a specific location.

        Args:
            location (Location): The initial position of the agent in the environment.
        """
        self.__location = location

    def get_location(self):
        """
        Get the current location of the agent.

        Returns:
            Location: The agent's current position.
        """
        return self.__location

    def set_location(self, location):
        """
        Set or update the agent's location.

        Args:
            location (Location): The new position for the agent.
        """
        self.__location = location

    @abstractmethod
    def act(self, environment):
        """
        Define the agent's behavior for a single simulation step.
        Must be implemented by all subclasses.

        Args:
            environment (Environment): The environment in which the agent acts.
        """
        pass
