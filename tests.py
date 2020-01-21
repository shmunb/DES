import unittest
import des_lib

input_txt = 'C:/Users/mi/Desktop/прога/des/tests/cp1251_input.txt'
encrypted_txt_file = "C:/Users/mi/Desktop/прога/des/cp1251_encrypted.txt"
decrypted_txt_file = "C:/Users/mi/Desktop/прога/des/cp1251_decrypted.txt"

input_binary = 'C:/Users/mi/Desktop/прога/des/tests/binary_input.txt'
encrypted_binary_file = "C:/Users/mi/Desktop/прога/des/binary_encrypted.txt"
decrypted_binary_file = "C:/Users/mi/Desktop/прога/des/binary_decrypted.txt"

key = 0b01010101010110110111010011001010000101010111110101101111


class GenerationTests(unittest.TestCase):

    def test_invalid_key(self):

        fake_key = 0x1ffffffffffffff
        fake_key_2 = 'aaaaaaaaaaaaa'

        with self.assertRaises(ValueError):
            test = des_lib.DES(fake_key, input_txt, encrypted_txt_file, 'cp1251')

        with self.assertRaises(TypeError):
            test = des_lib.DES(fake_key_2, input_txt, encrypted_txt_file, 'cp1251')

    def test_invalid_input_file(self):

        input_not_file = 'C:/Users/mi/Desktop/прога/des/tests/'
        fake_input = 'C:/Users/mi/Desktop/прога/des/tests/fake_input.txt'

        with self.assertRaises(ValueError):
            test = des_lib.DES(key, fake_input, encrypted_txt_file, 'cp1251')

        with self.assertRaises(ValueError):
            test = des_lib.DES(key, input_not_file, encrypted_txt_file, 'cp1251')

    def test_key_gen(self):
        self.assertEqual(16, len(des_lib.key_list_gen(key)))

    def test_encrypt_func(self):
        pass

    def test_text_mode(self):
        test = des_lib.DES(key, input_txt, encrypted_txt_file, 'cp1251')
        test.encrypt()

        test = des_lib.DES(key, encrypted_txt_file, decrypted_txt_file, 'cp1251')
        test.decrypt(8)

    def test_binary_mode(self):
        test = des_lib.DES(key, input_binary, encrypted_binary_file, 'bin')
        test.encrypt()

        test = des_lib.DES(key, encrypted_binary_file, decrypted_binary_file, 'bin')
        test.decrypt(8)

    def test_console_mode(self):
        test_enc = des_lib.DES(key)
        test_enc.encrypt()

        test_dec = des_lib.DES(key)
        test_dec.decrypt()


if __name__ == '__main__':
        unittest.main()

