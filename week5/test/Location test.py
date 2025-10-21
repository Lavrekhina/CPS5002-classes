import unittest
from week5.model.location import Location


class TestLocation(unittest.TestCase):
    """Unit tests for the Location class."""

    def test_init(self):
        """Test that a Location object initializes with correct x and y values."""
        loc = Location(3, 4)
        # Check that the x and y values are correctly assigned
        self.assertEqual(loc.get_x(), 3)
        self.assertEqual(loc.get_y(), 4)

    def test_setters(self):
        """Test that set_x() and set_y() correctly update the coordinates."""
        loc = Location(0, 0)
        loc.set_x(5)
        loc.set_y(10)
        # Verify that the new values are set properly
        self.assertEqual(loc.get_x(), 5)
        self.assertEqual(loc.get_y(), 10)

    def test_equals(self):
        """Test that equals() correctly compares two Location objects."""
        loc1 = Location(2, 3)
        loc2 = Location(2, 3)
        loc3 = Location(5, 6)
        # loc1 and loc2 should be equal; loc3 should not
        self.assertTrue(loc1.equals(loc2))
        self.assertFalse(loc1.equals(loc3))

    def test_str(self):
        """Test that __str__() returns the correct string representation."""
        loc = Location(7, 8)
        # The string should match the expected format
        self.assertEqual(str(loc), "Location (7, 8)")


if __name__ == '__main__':
    unittest.main()
