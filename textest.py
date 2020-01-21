import des_lib as lib

file = 'C:/Users/mi/Desktop/прога/des/tests/cp1251_input.txt'
encrypted_file = "C:/Users/mi/Desktop/прога/des/tests/cp1251_output.txt"
decrypted_file = "C:/Users/mi/Desktop/прога/des/tests/cp1251_result.txt"

test_key = 0b11111101110101010101001010100101010101001010010110100011

test = lib.DES(test_key, file, encrypted_file, 'cp1251')
test.encrypt()

test = lib.DES(test_key, encrypted_file, decrypted_file, 'cp1251')
test.decrypt(8)
