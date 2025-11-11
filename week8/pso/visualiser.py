import matplotlib.pyplot as plt
from typing import List, Tuple


class Visualiser:
    """
    Visualises the swarm movement towards the treasure.
    """

    def __init__(self, bounds: List[Tuple[float, float]], treasure_location: List[float]) -> None:
        self.__bounds = bounds
        self.__treasure_location = treasure_location
        self.__fig, self.__ax = plt.subplots()
        self.__swarm_plot = None

    def setup(self) -> None:
        """Configure plot limits, labels, and treasure marker."""
        self.__ax.set_xlim(self.__bounds[0])
        self.__ax.set_ylim(self.__bounds[1])
        self.__ax.set_aspect("equal", "box")
        self.__ax.set_xlabel("X Position")
        self.__ax.set_ylabel("Y Position")
        self.__ax.set_title("Treasure Hunters (Particle Swarm Optimization)")

        self.__ax.scatter(
            self.__treasure_location[0],
            self.__treasure_location[1],
            color="red",
            marker="*",
            s=150,
            label="Treasure Chest",
        )
        self.__ax.legend()

    def update(self, particle_positions: List[List[float]]) -> None:
        """Update swarm positions on the plot."""
        if self.__swarm_plot:
            self.__swarm_plot.remove()

        x = [pos[0] for pos in particle_positions]
        y = [pos[1] for pos in particle_positions]
        self.__swarm_plot = self.__ax.scatter(x, y, color="blue", label="Hunters")

        plt.pause(0.3)
