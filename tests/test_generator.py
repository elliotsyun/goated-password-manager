import unittest
from src import generator
import string


# in root dir, python -m unittest tests.test_generator


class TestGenerator(unittest.TestCase):

    def test_generate_length(self):
        length = 14
        password = generator.generate(length)
        self.assertEqual(len(password), length)

    def test_generate_with_string_minimum_length(self):
        input_string = "example keyword"
        password = generator.generate_with_string(input_string)
        self.assertGreaterEqual(len(password), generator.DEFAULT_LENGTH)

    def test_generate_with_string_contains_keywords(self):
        input_string = "example keyword"
        password = generator.generate_with_string(input_string)
        self.assertIn("example", password)
        self.assertIn("keyword", password)

    def test_generate_with_string_randomness(self):
        seed = 100
        input_string = "example keyword"
        password1 = generator.generate_with_string(input_string, seed)
        password2 = generator.generate_with_string(input_string, seed)
        self.assertNotEqual(password1, password2)

    def test_regular_password(self):
        input_password = "user_password"
        returned_password = generator.regular_password(input_password)
        self.assertEqual(input_password, returned_password)

    def test_generate_non_default_length(self):
        length = 20
        password = generator.generate(length)
        self.assertEqual(len(password), length)

    def test_generate_special_characters(self):
        length = 50
        password = generator.generate(length)
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_with_string_exact_length(self):
        input_string = "thisisfourteen"
        password = generator.generate_with_string(input_string)
        self.assertEqual(len(password), generator.DEFAULT_LENGTH)

    def test_generate_with_string_longer_than_default(self):
        input_string = "thisisaverylongkeywordinputstring"
        password = generator.generate_with_string(input_string)
        self.assertEqual(len(password), len(input_string))

    def test_generate_with_string_shuffled(self):
        input_string = "shuffle test"
        password = generator.generate_with_string(input_string)
        self.assertNotEqual(password, input_string.replace(" ", ""))


if __name__ == "__main__":
    unittest.main()
