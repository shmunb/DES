def padding(block):
    if len(block) != 0 and len(block) != 64:
        print('Padding:', 64-len(block), 'bit(s)')
    return block + '0'*(64-len(block)) if len(block) != 0 else "-1"


def write_block(output, block, mode):
    if mode == 'bin':
        output.write(block)
    elif mode == 'console':
        data = ""
        for i in range(len(block) // 8):
            data = data + ((int(block[8*i:8*(i+1)], 2)).to_bytes(1, 'big')).decode('cp1251')
        return data
    else:
        for i in range(len(block) // 8):
            data = int(block[8*i:8*(i+1)], 2)
            output.write(data.to_bytes(1, 'big'))


def read_block(input_, mode):
    if mode == 'bin':
        block = input_.read(64)
        return block
    elif mode == 'console':
        block = ""
        inp = " "
        while len(block) < 64 and len(input_) > 0:
            inp = input_[0]
            input_ = input_[1:]
            b = int.from_bytes(inp.encode('1251'), 'big')
            block = block + f"{b:08b}"
    else:
        block = ""
        while len(block) < 64:
            inp = input_.read(1)
            if len(inp) == 0:
                break
            b = int.from_bytes(inp, 'big')
            block = block + f"{b:08b}"

    return block


def swap_nearby_bits(block):
    new_block = ''.join(block[i*2+1] + block[i*2] for i in range(len(block)//2))
    if len(block) % 2 == 1:
        new_block = new_block + block[-1]
    return new_block
