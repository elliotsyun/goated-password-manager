import unittest
from src import encrypter

# go to goated-password-manager and type python -m unittest


class TestEncrypter(unittest.TestCase):

    def test_encrypt_and_decrypt(self):
        password = "my_password"
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)


if __name__ == '__main__':
    unittest.main()
