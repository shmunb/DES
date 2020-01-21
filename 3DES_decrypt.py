import des_lib as DES

files = ("C:/Users/mi/Desktop/прога/des/3des/encrypted_3.txt",
         "C:/Users/mi/Desktop/прога/des/3des/encrypted_2.txt",
         "C:/Users/mi/Desktop/прога/des/3des/encrypted_1.txt",
         "C:/Users/mi/Desktop/прога/des/3des/final.txt")

# keys = (input() for i in range 3)

keys = (0b10010101010101010101011110110011011000011100110110101011,
        0b01101111101101111010001101010111011010111101010101110110,
        0b11101011010101011111001000001111010101010111100001100001)

print(keys)

print('Enter padding')
padding = int(input())

for i in range(3):
    tmp = DES.DES(keys[2 - i], files[i], files[i+1], 'cp1251')
    tmp.decrypt(padding if i == 2 else 0)


