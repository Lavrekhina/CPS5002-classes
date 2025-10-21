import unittest
from week5.model.agent import Agent
from week5.model.location import Location


# A simple concrete subclass of Agent (since Agent is abstract)
class TestAgentClass(Agent):
    def act(self, environment):
        pass


class TestAgent(unittest.TestCase):

    def setUp(self):
        # Create a Location and an Agent before each test
        self.location = Location(3, 4)
        self.agent = TestAgentClass(self.location)

    def test_get_location(self):
        """Test that get_location() returns the correct Location object."""
        self.assertEqual(self.agent.get_location(), self.location)

    def test_set_location(self):
        """Test that set_location() correctly updates the Agent's location."""
        new_location = Location(7, 8)
        self.agent.set_location(new_location)
        self.assertEqual(self.agent.get_location(), new_location)

    def test_location_attributes(self):
        """Test that Location stores x and y correctly."""
        self.assertEqual(self.location.get_x(), 3)
        self.assertEqual(self.location.get_y(), 4)

    def test_location_setters(self):
        """Test that set_x() and set_y() correctly change the coordinates."""
        self.location.set_x(10)
        self.location.set_y(20)
        self.assertEqual(self.location.get_x(), 10)
        self.assertEqual(self.location.get_y(), 20)


if __name__ == '__main__':
    unittest.main()
