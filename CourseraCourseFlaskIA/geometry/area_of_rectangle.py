import unittest


def area_rectangle(width, height):
    """
    Calcula el área de un rectángulo.

    Args:
        width (float): El ancho del rectángulo.
        height (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    return width * height


class TestAreaFunctions(unittest.TestCase):

    def area_rectangle(self):
        # Test case 1: Área de un rectángulo con ancho 3 y altura 4 debe ser 12
        self.assertEqual(area_rectangle(3, 4), 12)

        # Test case 2: Área de un rectángulo con ancho 5 y altura 10 debe ser 50
        self.assertEqual(area_rectangle(5, 10), 50)

        # Test case 3: Área de un rectángulo con ancho 0 y altura 10 debe ser 0
        self.assertEqual(area_rectangle(0, 10), 0)

        # Test case 4: Área de un rectángulo con ancho 5 y altura 0 debe ser 0
        self.assertEqual(area_rectangle(5, 0), 0)

        # Test case 5: Área de un rectángulo con ancho 7.5 y altura 3.2 debe ser 24.0
        self.assertAlmostEqual(area_rectangle(7.5, 3.2), 24.0)


if __name__ == '__main__':
    unittest.main()
