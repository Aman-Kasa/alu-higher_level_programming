import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_constructor(self):
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 3)
        self.assertEqual(s4.id, 4)

    def test_invalid_constructor(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_str(self):
        s1 = Square(5, 1, 2, 9)
        self.assertEqual(str(s1), "[Square] (9) 1/2 - 5")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(s1_dictionary, {'id': 9, 'size': 10, 'x': 2, 'y': 1})

    def test_update(self):
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

        s1.update(id=89, size=2, x=3, y=4)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_create(self):
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_save_to_file(self):
        s1 = Square(10)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1, "size": 10, "x": 0, "y": 0}]')

    def test_load_from_file(self):
        s1 = Square(10)
        Square.save_to_file([s1])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), str(s1))

if __name__ == "__main__":
    unittest.main()
