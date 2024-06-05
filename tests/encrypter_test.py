import unittest
from src import encrypter

if __name__ == '__main__':
    unittest.main()


class encrypter_test(unittest.TestCase):
    '''Encrypter test class'''

    def test_encrypt_returns_dict(self):
        """Test if the encrypt function returns a dictionary"""
        result = encrypter.encrypt("test_password")
        self.assertIsInstance(result, dict)

    def test_encrypt_contains_keys(self):
        """Test if the returned dictionary contains the correct keys"""
        result = encrypter.encrypt("test_password")
        self.assertIn("key", result)
        self.assertIn("nonce", result)
        self.assertIn("ciphertext", result)
        self.assertIn("tag", result)

    def test_encrypt_key_length(self):
        """Test if the key length is 16 bytes"""
        result = encrypter.encrypt("test_password")
        self.assertEqual(len(result["key"]), 16)

    def test_encrypt_nonce_length(self):
        """Test if the nonce length is 16 bytes"""
        result = encrypter.encrypt("test_password")
        self.assertEqual(len(result["nonce"]), 16)

    def test_encrypt_ciphertext_not_empty(self):
        """Test if the ciphertext is not empty"""
        result = encrypter.encrypt("test_password")
        self.assertGreater(len(result["ciphertext"]), 0)

    def test_encrypt_tag_not_empty(self):
        """Test if the tag is not empty"""
        result = encrypter.encrypt("test_password")
        self.assertGreater(len(result["tag"]), 0)

    def test_encrypt_different_inputs(self):
        """Test the function with different password inputs"""
        passwords = ["short", "long_password_12345",
                     "", "special_chars_!@#$%^&*()"]
        for password in passwords:
            with self.subTest(password=password):
                result = encrypter.encrypt(password)
                self.assertIsInstance(result, dict)
                self.assertIn("key", result)
                self.assertIn("nonce", result)
                self.assertIn("ciphertext", result)
                self.assertIn("tag", result)
