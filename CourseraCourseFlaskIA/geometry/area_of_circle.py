import math
import unittest

def area_triangle(base, height):
    """
    Calcula el área de un triángulo.

    Args:
        base (float): La base del triángulo.
        height (float): La altura del triángulo.

    Returns:
        float: El área del triángulo.
    """
    return 0.5 * base * height

def area_circle(radius):
    """
    Calcula el área de un círculo.

    Args:
        radius (float): El radio del círculo.

    Returns:
        float: El área del círculo.
    """
    return math.pi * radius * radius

class TestAreaFunctions(unittest.TestCase):
    
    def test_area_triangle(self):
        # Test case 1: Área de un triángulo con base 3 y altura 4 debe ser 6
        self.assertEqual(area_triangle(3, 4), 6)
        
        # Test case 2: Área de un triángulo con base 5 y altura 10 debe ser 25
        self.assertEqual(area_triangle(5, 10), 25)
        
        # Test case 3: Área de un triángulo con base 0 y altura 10 debe ser 0
        self.assertEqual(area_triangle(0, 10), 0)
        
        # Test case 4: Área de un triángulo con base 5 y altura 0 debe ser 0
        self.assertEqual(area_triangle(5, 0), 0)
    
    def test_area_circle(self):
        # Test case 1: Área de un círculo con radio 3 debe ser aproximadamente 28.2743
        self.assertAlmostEqual(area_circle(3), 28.2743, places=4)
        
        # Test case 2: Área de un círculo con radio 0 debe ser 0
        self.assertEqual(area_circle(0), 0)
        
        # Test case 3: Área de un círculo con radio 1 debe ser aproximadamente 3.1416
        self.assertAlmostEqual(area_circle(1), 3.1416, places=4)
        
        # Test case 4: Área de un círculo con radio 2.5 debe ser aproximadamente 19.6349
        self.assertAlmostEqual(area_circle(2.5), 19.6349, places=4)

if __name__ == '__main__':
    unittest.main()