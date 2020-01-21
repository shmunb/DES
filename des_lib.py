import read_lib as r
import conversion_lib as con
import os.path
import random


def encrypt_func(R, k):
    ERn = con.E_expansion(R) ^ k
    ER = f'{ERn:048b}'
    Bend = ''
    for t in range(8):
        B = (ER[6*t:6*(t+1)])
        a = int(B[0] + B[5], 2)
        b = int(B[1:5], 2)
        s = f'{con.S_scheme[t][a][b]:04b}'
        Bend = Bend + s
    r = con.P_permutation(Bend)
    return r


def key_gen():
    key = random.randint(0x0, 0xffffffffffffff)
    if key in con.weak_keys:
        key = key_gen()
    print('Your randomly generated key:', key)
    return key


def key_list_gen(k):

    s = f'{k:056b}'
    n = [abs(int(s[7*i: 7*(i+1)], 2) % 2 - 1) for i in range(8)]
    s = s[0:7] + f'{n[0]}' + s[7:14] + f'{n[1]}' + s[14:21] + f'{n[2]}' + s[21:28] + f'{n[3]}' + s[28:35] + f'{n[4]}' + s[35:42] + f'{n[5]}' + s[42:49] + f'{n[6]}' + s[49:] + f'{n[7]}'
    print(hex(int(s, 2)), " - Your expanded key!")

    key_list = []
    steps = 0

    for i in range(16):
        steps += con.CD_step[i]
        C = con.C0[steps:] + con.C0[:steps]
        D = con.D0[steps:] + con.D0[:steps]
        st = ""

        for t in range(len(C)):
                st = st + s[C[t]]
        for t in range(len(D)):
                st = st + s[D[t]]

        key = ""
        for t in range(len(con.key_scheme)):
            key = key + st[con.key_scheme[t]]
        key_list.append(int(key, 2))
    return tuple(key_list)


class DES:
    def __init__(self, key=key_gen(), input_file='', output_file='', mode='console'):

        if mode in ('bin', 'cp1251', 'console'):
            self.mode = mode
        else:
            raise ValueError("Mode must be 'console'(default), 'bin' or 'cp1251'")

        if mode != 'console':
            if not os.path.exists(input_file):
                raise ValueError("Input file doesn't exist")
            if not os.path.isfile(input_file):
                raise ValueError("Input file isn't a file LOL")

        if key in con.weak_keys:
            print('Key is weak! Try another key')
            key = input()
        if not isinstance(key, int):
            raise TypeError('Only integer keys allowed')
        if key > 0xffffffffffffff:
            raise ValueError('Key is longer than 56 bit')

        self.key = key
        self.key_list = key_list_gen(self.key)
        self.block = ""

        if mode == 'console':
            print('Enter something(cp1251 symbols allowed)')
            self.input = input()
            self.output = ''
        else:
            self.input = open(input_file, 'r' if mode == 'bin' else 'rb')
            self.output = open(output_file, 'w' if mode == 'bin' else 'wb')

        print('DES generated')

    def encrypt(self):

        # print(self.input.read(3), '- Мы любим Microsoft Notepad!')  # костыль от первых трёх байтов в utf-8 notepad
        self.block = r.padding(r.read_block(self.input, self.mode))
        if self.mode == 'console':
            self.input = self.input[8:]

        while self.block != "-1":

            self.block = f'{con.IP_permutation(self.block):064b}'
            R = int(self.block[:32], 2)
            L = int(self.block[32:], 2)

            for i in range(16):
                R, L = L ^ encrypt_func(R, self.key_list[i]), R

            L = f'{L:032b}'
            R = f'{R:032b}'

            self.block = f'{con.IPb_permutation(L + R):064b}'

            if self.mode == 'console':
                self.output = self.output + r.write_block(self.output, self.block, self.mode)
            else:
                r.write_block(self.output, self.block, self.mode)

            self.block = r.padding(r.read_block(self.input, self.mode))
            if self.mode == 'console':
                self.input = self.input[8:]

        if self.mode == 'console':
            print('Encrypted data:', self.output)
        else:
            self.input.close()
            self.output.close()

    def decrypt(self, padding=0):

        self.block = r.read_block(self.input, self.mode)
        if self.mode == 'console':
            self.input = self.input[8:]

        while self.block != "-1" and self.block != '':

            if len(self.block) < 64:
                print(self.block, len(self.block))
                raise ValueError('Incorrect data: block is shorter than 64-bit!')

            self.block = f'{con.IP_permutation(self.block):064b}'

            L = int(self.block[:32], 2)
            R = int(self.block[32:], 2)

            for i in reversed(list(range(16))):
                L, R = R ^ encrypt_func(L, self.key_list[i]), L

            L = f'{L:032b}'
            R = f'{R:032b}'

            self.block = f'{con.IPb_permutation(L + R):064b}'
            output_block = self.block
            self.block = r.read_block(self.input, self.mode)
            if self.mode == 'console':
                self.input = self.input[8:]

            if self.block == "" and padding > 0:
                print(padding, 'padded bit(s) erased, output data may appear incorrect')

            if self.mode == 'console':
                data = r.write_block(self.output, (r.swap_nearby_bits(output_block)[:-padding] if self.block == "" and padding > 0 else
                                                   r.swap_nearby_bits(output_block)), self.mode)
                self.output = self.output + data
            else:
                r.write_block(self.output, r.swap_nearby_bits(output_block)[:-padding] if self.block == "" and padding > 0 else
                                           r.swap_nearby_bits(output_block), self.mode)

        if self.mode == 'console':
            print('Decrypted data:', self.output)
        else:
            self.input.close()
            self.output.close()





