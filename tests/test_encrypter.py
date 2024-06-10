import unittest
from src import encrypter
from Crypto.Random import get_random_bytes


# in root dir, python -m unittest tests.test_encrypter


class TestEncrypter(unittest.TestCase):

    def test_encrypt_and_decrypt(self):
        print("test1: e, d basic")
        password = "my_password"
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)

    def test_encrypt_and_decrypt_special_characters(self):
        print("test2: e, d special_characters")
        password = "p@$$w0rd!#"
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)

    def test_encrypt_and_decrypt_empty_string(self):
        print("test3: e, d empty_string")
        password = ""
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)

    def test_encrypt_and_decrypt_unicode_characters(self):
        print("test4: e, d unicode")
        password = "密码"  # Chinese characters for 'password'
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)

    def test_encrypt_and_decrypt_long_string(self):
        print("test5: e, d long_string")
        password = "a" * 100
        encryption = encrypter.encrypt(password)
        decrypted_password = encrypter.decrypt(encryption)
        self.assertEqual(password, decrypted_password)

    def test_encrypt_and_decrypt_similar_passwords(self):
        print("test6: e, d similar")
        password1 = "password123"
        password2 = "password124"
        encryption1 = encrypter.encrypt(password1)
        encryption2 = encrypter.encrypt(password2)
        self.assertNotEqual(
            encryption1["ciphertext"], encryption2["ciphertext"])
        self.assertEqual(password1, encrypter.decrypt(encryption1))
        self.assertEqual(password2, encrypter.decrypt(encryption2))

    def test_encrypt_and_decrypt_same_password_multiple_times(self):
        print("test7: e, d repeat")
        password = "repeated_password"
        encryptions = [encrypter.encrypt(password) for _ in range(5)]
        decrypted_passwords = [encrypter.decrypt(enc) for enc in encryptions]
        self.assertTrue(all(p == password for p in decrypted_passwords))
        ciphertexts = [enc["ciphertext"] for enc in encryptions]
        self.assertEqual(len(set(ciphertexts)), len(ciphertexts))

    def test_encrypt_with_non_string_input(self):
        print("test9: non_string input")
        with self.assertRaises(TypeError):
            encrypter.encrypt(12345)

    def test_decrypt_with_non_dict_input(self):
        print("test10: non_dict input")
        with self.assertRaises(TypeError):
            encrypter.decrypt("not_a_dict")

    def test_decrypt_with_invalid_key(self):
        print("test11: invalid key")
        password = "secure_password"
        encryption = encrypter.encrypt(password)
        encryption["key"] = get_random_bytes(16)  # Replace with a wrong key
        with self.assertRaises(ValueError):
            encrypter.decrypt(encryption)

    def test_decrypt_with_invalid_nonce(self):
        print("test12: invalid_nonce")
        password = "secure_password"
        encryption = encrypter.encrypt(password)
        encryption["nonce"] = get_random_bytes(
            16)  # Replace with a wrong nonce
        with self.assertRaises(ValueError):
            encrypter.decrypt(encryption)

    def test_decrypt_with_invalid_ciphertext(self):
        print("test13: invalid_ciphertext")
        password = "secure_password"
        encryption = encrypter.encrypt(password)
        encryption["ciphertext"] = get_random_bytes(
            len(encryption["ciphertext"]))  # Replace with invalid ciphertext
        with self.assertRaises(ValueError):
            encrypter.decrypt(encryption)

    def test_decrypt_with_invalid_tag(self):
        print("test14: invalid_tag")
        password = "secure_password"
        encryption = encrypter.encrypt(password)
        encryption["tag"] = get_random_bytes(
            len(encryption["tag"]))  # Replace with invalid tag
        with self.assertRaises(ValueError):
            encrypter.decrypt(encryption)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
