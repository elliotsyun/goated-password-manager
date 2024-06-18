import unittest
from src import generator
import string


# in root dir, python -m unittest tests.test_generator


class TestGenerator(unittest.TestCase):

    def test_generate_length(self):
        length = 14
        iterations = 100  # Number of iterations to increase the likelihood of capturing all character types

        for _ in range(iterations):
            password = generator.generate(length)
            self.assertEqual(
                len(password),
                length,
                "Password length should match the specified length.",
            )

        # Checking the likelihood of the password containing digits, letters, and punctuation over multiple iterations
        contains_digit = any(
            any(char.isdigit() for char in generator.generate(length))
            for _ in range(iterations)
        )
        contains_letter = any(
            any(char.isalpha() for char in generator.generate(length))
            for _ in range(iterations)
        )
        contains_punctuation = any(
            any(char in string.punctuation for char in generator.generate(length))
            for _ in range(iterations)
        )

        self.assertTrue(contains_digit, "Password should contain digits.")
        self.assertTrue(contains_letter, "Password should contain letters.")
        self.assertTrue(contains_punctuation, "Password should contain punctuation.")

    def test_generate_with_string_keywords(self):
        input_string = "example keyword"
        password = generator.generate_with_string(input_string)
        self.assertIn(
            "examplekeyword",
            password,
            "Password should contain the combined keywords 'example' and 'keyword'.",
        )
        self.assertTrue(
            len(password) > len("examplekeyword"),
            "Password should contain additional random characters.",
        )

    def test_generate_with_string_seed(self):
        input_string = "example keyword"
        seed = 42
        password1 = generator.generate_with_string(input_string, seed)
        password2 = generator.generate_with_string(input_string, seed)
        self.assertEqual(
            password1,
            password2,
            "Passwords should be identical when using the same seed.",
        )

    def test_regular_password(self):
        user_password = "user_password"
        returned_password = generator.regular_password(user_password)
        self.assertEqual(
            returned_password,
            user_password,
            "Returned password should match the user-provided password.",
        )


if __name__ == "__main__":
    unittest.main()
