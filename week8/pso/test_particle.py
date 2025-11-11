import unittest
from particle import Particle


class TestParticle(unittest.TestCase):
    def test_position_update_and_clamping(self):
        def objective(x): return sum(i ** 2 for i in x)

        bounds = [(-5, 5), (-10, 10)]
        p = Particle(2, bounds, objective)
        p.velocity = [3.0, -12.0]

        old_position = p.position.copy()
        p.update_position()

        for i, (low, high) in enumerate(bounds):
            expected = old_position[i] + p.velocity[i]
            if expected < low:
                expected = low
            elif expected > high:
                expected = high
            self.assertAlmostEqual(p.position[i], expected)
            self.assertTrue(low <= p.position[i] <= high)

    def test_evaluate_updates_personal_best(self):
        def objective(x): return sum(i ** 2 for i in x)
        p = Particle(2, [(-10, 10), (-10, 10)], objective)
        old_best = p.p_best_value
        p.position = [0.0, 0.0]
        p.evaluate()
        self.assertTrue(p.p_best_value <= old_best)


if __name__ == "__main__":
    unittest.main()
