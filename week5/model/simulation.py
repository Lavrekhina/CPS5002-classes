from time import sleep
from week5.model.location import Location
from week5.model.ocean import Ocean
from week5.model.shark import Shark
from simulation_constants import GRID_ROWS, GRID_COLS


def run():
    """Run the main ocean simulation."""

    # Create the ocean environment with the specified grid size
    # The grid dimensions come from simulation_constants.py
    ocean = Ocean(GRID_COLS, GRID_ROWS)

    # Define the initial location of the shark (column 5, row 5)
    shark_location = Location(5, 5)

    # Create a Shark agent at that location
    shark = Shark(shark_location)

    # Place the shark in the ocean grid at the given coordinates
    ocean.set_agent(shark, shark_location)

    # Main simulation loop: runs indefinitely
    while True:
        # The shark performs its action (e.g., swim to an adjacent free cell)
        shark.act(ocean)

        # Print the current state of the ocean to visualize shark movement
        # Each grid update will show the shark's new position
        print(ocean)

        # Pause for 5 seconds before the next step
        sleep(5)


# Entry point: only runs if this script is executed directly
if __name__ == "__main__":
    run()
