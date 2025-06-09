import unittest
import my_calculator


class TestCalc(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(my_calculator.add(1, 1), 2)

    def test_addition_with_string(self):
        with self.assertRaises(TypeError):
            my_calculator.add(1, "bla")

    def test_nonsense(self):
        # this tests nonsense
        yourmom = "fat"
        assert yourmom == "fat"

    def test_sub(self):
        # does this test nonsense too?
        self.assertEqual(my_calculator.sub(1, 1), 0)


if __name__ == "__main__":
    unittest.main()
