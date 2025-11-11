import random
from typing import Callable, List, Tuple


class Particle:
    """
    Represents a particle in a Particle Swarm Optimization (PSO) system.
    Each particle has a position, velocity, and personal best, all constrained
    within specified bounds. Velocity is clamped to prevent excessive jumps.
    """

    def __init__(
        self,
        dimensions: int,
        bounds: List[Tuple[float, float]],
        objective_function: Callable[[List[float]], float],
        velocity_ratio: float = 0.5  # max velocity as fraction of range
    ) -> None:
        self.dimensions = dimensions
        self.bounds = bounds
        self.objective_function = objective_function

        # Initialize random position within bounds
        self.position = [
            random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimensions)
        ]

        # Maximum velocity per dimension (fraction of range)
        self.vmax = [
            velocity_ratio * (bounds[i][1] - bounds[i][0]) for i in range(dimensions)
        ]

        # Initialize random velocity within [-vmax, vmax]
        self.velocity = [
            random.uniform(-self.vmax[i], self.vmax[i]) for i in range(dimensions)
        ]

        # Personal best
        self.p_best_position = self.position.copy()
        self.p_best_value = self.objective_function(self.position)

    def evaluate(self) -> float:
        """Evaluate objective function and update personal best if improved."""
        current_value = self.objective_function(self.position)
        if current_value < self.p_best_value:
            self.p_best_value = current_value
            self.p_best_position = self.position.copy()
        return current_value

    def update_velocity(self, g_best_position: List[float], w: float, c1: float, c2: float) -> None:
        """Update velocity with inertia, cognitive, and social components and clamp it."""
        for i in range(self.dimensions):
            r1 = random.random()
            r2 = random.random()

            inertia = w * self.velocity[i]
            cognitive = c1 * r1 * (self.p_best_position[i] - self.position[i])
            social = c2 * r2 * (g_best_position[i] - self.position[i])

            new_velocity = inertia + cognitive + social

            # Clamp velocity within [-vmax, vmax]
            self.velocity[i] = max(min(new_velocity, self.vmax[i]), -self.vmax[i])

    def update_position(self) -> None:
        """Update position based on velocity and clamp within bounds."""
        for i in range(self.dimensions):
            self.position[i] += self.velocity[i]
            low, high = self.bounds[i]
            # Clamp position within bounds
            self.position[i] = max(min(self.position[i], high), low)

    def __repr__(self) -> str:
        return (
            f"Particle(pos={self.position}, vel={self.velocity}, "
            f"p_best={self.p_best_value:.4f})"
        )
