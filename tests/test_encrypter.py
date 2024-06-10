import unittest
from src import encrypter


class TestEncrypter(unittest.TestCase):

    def test_encrypt_and_decrypt(self):
        print("test1")
        password = "my_password"
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)

    def test_encrypt_and_decrypt_special_characters(self):
        print("test2")
        password = "p@$$w0rd!#"
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)

    def test_encrypt_and_decrypt_empty_string(self):
        print("test3")
        password = ""
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)

    def test_encrypt_and_decrypt_unicode_characters(self):
        print("test4")
        password = "密码"  # Chinese characters for 'password'
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)

    def test_encrypt_and_decrypt_long_string(self):
        print("test5")
        password = "a" * 100
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestEncrypter('test_encrypt_and_decrypt'))
    suite.addTest(TestEncrypter('test_encrypt_and_decrypt_special_characters'))
    suite.addTest(TestEncrypter('test_encrypt_and_decrypt_empty_string'))
    suite.addTest(TestEncrypter('test_encrypt_and_decrypt_unicode_characters'))
    suite.addTest(TestEncrypter('test_encrypt_and_decrypt_long_string'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
