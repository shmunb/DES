import des_lib as lib

inputfile = 'C:/Users/mi/Desktop/прога/des/testinput.txt'
outputfile = "C:/Users/mi/Desktop/прога/des/testoutput.txt"

testkey = 0b11111101110101010101001010100101010101001010010110100011

print(lib.con.IP_scheme)
test = lib.DES(testkey, outputfile, inputfile, 'utf-8')
test.decrypt()


