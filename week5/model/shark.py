import random
from agent import Agent


class Shark(Agent):
    """
    A Shark is an Agent that can move (swim) to a random adjacent free location
    in the Ocean environment.
    """

    def __swim(self, ocean):
        """
        Attempt to move the shark to a random free adjacent location.

        Args:
            ocean (Ocean): The environment (grid) in which the shark moves.
        """

        # Get a list of all free adjacent cells around the shark's current position
        free_locations = ocean.find_free_adjacent_locations(self.get_location())

        # If there are any available (empty) locations nearby
        if len(free_locations) > 0:
            # Randomly select one of those free locations
            target = random.choice(free_locations)

            # Store the shark's current location before moving
            current = self.get_location()

            # Move the shark in the ocean grid:
            # 1. Place the shark at the target position
            ocean.set_agent(self, target)
            # 2. Remove the shark from its old position
            ocean.set_agent(None, current)
            # 3. Update the shark’s internal location reference
            self.set_location(target)

    def act(self, environment):
        """
        Perform the shark's behavior for one simulation step.
        The shark will 'swim' (move) within the given environment.

        Args:
            environment (Ocean): The environment where the shark acts.
        """
        self.__swim(environment)
