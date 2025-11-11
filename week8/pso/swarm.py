from typing import Callable, List, Tuple
from particle import Particle


class Swarm:
    """
    Represents a swarm of particles in a PSO system.
    Manages particles, global best position, and global best value.
    """

    def __init__(
        self,
        num_particles: int,
        bounds: List[Tuple[float, float]],
        objective_function: Callable[[List[float]], float],
    ) -> None:
        self.particles = [
            Particle(len(bounds), bounds, objective_function)
            for _ in range(num_particles)
        ]

        # Initialize global best as the best of the initial particles
        self.g_best_position = self.particles[0].p_best_position.copy()
        self.g_best_value = self.particles[0].p_best_value

        self.evaluate_particles()

    def evaluate_particles(self) -> None:
        """
        Evaluate all particles and update the global best if any personal best is better.
        """
        for particle in self.particles:
            particle.evaluate()
            if particle.p_best_value < self.g_best_value:
                self.g_best_value = particle.p_best_value
                self.g_best_position = particle.p_best_position.copy()

    def update_particles(self, w: float, c1: float, c2: float) -> None:
        """
        Update velocity and position of each particle in the swarm.
        """
        for particle in self.particles:
            particle.update_velocity(self.g_best_position, w, c1, c2)
            particle.update_position()

    def get_global_best(self) -> Tuple[List[float], float]:
        """Return the current global best position and value."""
        return self.g_best_position, self.g_best_value

    def get_particles(self) -> List[Particle]:
        """Return the list of particles in the swarm."""
        return self.particles
