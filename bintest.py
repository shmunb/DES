import des_lib as lib

input_binary = 'C:/Users/mi/Desktop/прога/des/tests/binary_input.txt'
encrypted_binary_file = "C:/Users/mi/Desktop/прога/des/tests/binary_encrypted.txt"
decrypted_binary_file = "C:/Users/mi/Desktop/прога/des/tests/binary_decrypted.txt"

test_key = 0b11101001010101010011001010101100101010101111001001010101

test = lib.DES(test_key, input_binary, encrypted_binary_file, 'bin')
test.encrypt()

test = lib.DES(test_key, encrypted_binary_file, decrypted_binary_file)
test.decrypt(41)