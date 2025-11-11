import math
from swarm import Swarm
from visualiser import Visualiser

# Objective function: distance to treasure chest
def objective_function(position):
    treasure_location = [5.0, 5.0]  # hidden treasure
    return math.sqrt((position[0] - treasure_location[0]) ** 2 + (position[1] - treasure_location[1]) ** 2)

def main():
    bounds = [(-10, 10), (-10, 10)]  # 2D space
    num_particles = 4
    swarm = Swarm(num_particles, bounds, objective_function)

    visualiser = Visualiser(bounds, [5.0, 5.0])
    visualiser.setup()

    # Hyperparameters
    w = 0.5   # inertia
    c1 = 1.5  # cognitive
    c2 = 1.5  # social

    iterations = 20
    for step in range(iterations):
        swarm.update_particles(w, c1, c2)
        swarm.evaluate_particles()
        g_best_position, g_best_value = swarm.get_global_best()

        positions = [p.position for p in swarm.get_particles()]
        visualiser.update(positions)

        print(f"Iteration {step + 1}: Best Value = {g_best_value:.4f} at {g_best_position}")

    print("\nTreasure found near:", g_best_position)

if __name__ == "__main__":
    main()
