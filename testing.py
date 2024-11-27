import unittest

from Final_project import Housing

class TestHousing(unittest.TestCase):
    
    """Unit tests for the Housing class."""

    def test_initialization(self):
        
        """Test the initialization of the Housing class."""
        # Create a Housing object
        housing = Housing(1, "Terrapin Row", 3, 2, 1200.0, 1000, 0.5)
        
        # Check if the attributes are correctly assigned
        self.assertEqual(housing.id, 1)
        self.assertEqual(housing.name, "Terrapin Row")
        self.assertEqual(housing.bed, 3)
        self.assertEqual(housing.bath, 2)
        self.assertEqual(housing.price, 1200.0)
        self.assertEqual(housing.sqft, 1000)
        self.assertEqual(housing.proximity, 0.5)

if __name__ == '__main__':
    unittest.main()