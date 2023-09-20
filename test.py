import unittest
import figures


class TestMain(unittest.TestCase):

    def test_circle_area(self):
        self.assertEqual(figures.Circle(5).area(), 78.5398163375)

    def test_triangle_area(self):
        self.assertEqual(figures.Triangle(3, 4, 5).area(), 6)


if __name__ == "__main__":
    unittest.main()
