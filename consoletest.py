import des_lib as lib


test_key = 0b11111101110101010101001010100101010101001010010110100011

test = lib.DES(test_key)
test.encrypt()

test = lib.DES(test_key)
test.decrypt()
