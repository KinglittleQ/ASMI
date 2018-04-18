opcodes_table = {
    'lw': 0x23,
    'lb': 0x20,
    'lbu': 0x24,
    'lh': 0x21,
    'lhu': 0x25,
    'sw': 0x2B,
    'sb': 0x28,
    'sh': 0x29,

    'add': 0x00,
    'addu': 0x00,
    'sub': 0x00,
    'subu': 0x00,
    'slt': 0x00,
    'sltu': 0x00,
    'and': 0x00,
    'or': 0x00,
    'xor': 0x00,
    'nor': 0x00,
    'sll': 0x00,
    'srl': 0x00,
    'sra': 0x00,
    'mult': 0x00,
    'multu': 0x00,
    'div': 0x00,
    'divu': 0x00,

    'addi': 0x08,
    'addiu': 0x09,
    'andi': 0x0C,
    'ori': 0x0D,
    'xori': 0x0E,
    'lui': 0x0F,
    'slti': 0x0A,
    'sltiu': 0x0B,

    'beq': 0x04,
    'bne': 0x05,
    'blez': 0x06,
    'bgtz': 0x07,
    # 'bltz': 0x01,
    # 'bgez'

    'j': 0x02,
    'jal': 0x03,
    'jalr': 0x00,
    'jr': 0x00,
    'mfhi': 0x00,
    'mflo': 0x00,
    'mthi': 0x00,
    'mtlo': 0x00,

    'eret': 0x10,
    # 'mfco': 0x10,
    # 'mtco'

    'break': 0x00,
    'syscall': 0x00,
}

funcs_table = {
    'add': 0x20,
    'addu': 0x21,
    'sub': 0x22,
    'subu': 0x23,
    'slt': 0x2A,
    'sltu': 0x2B,
    'and': 0x24,
    'or': 0x25,
    'xor': 0x26,
    'nor': 0x27,

    'sll': 0x00,
    'srl': 0x02,
    'sra': 0x03,
    'mult': 0x18,
    'multu': 0x19,
    'div': 0x1A,
    'divu': 0x1B,

    'jalr': 0x09,
    'jr': 0x08,
    'mfhi': 0x10,
    'mflo': 0x12,
    'mthi': 0x11,
    'mtlo': 0x13,

    'eret': 0x18,
    'break': 0x0D,
    'syscall': 0x0C,
}

registers_table = {
    '$zero': 0,
    '$at': 1,

    '$v0': 2,
    '$v1': 3,

    '$a0': 4,
    '$a1': 5,
    '$a2': 6,
    '$a3': 7,

    '$t0': 8,
    '$t1': 9,
    '$t2': 10,
    '$t3': 11,
    '$t4': 12,
    '$t5': 13,
    '$t6': 14,
    '$t7': 15,

    '$s0': 16,
    '$s1': 17,
    '$s2': 18,
    '$s3': 19,
    '$s4': 20,
    '$s5': 21,
    '$s6': 22,
    '$s7': 23,

    '$t8': 24,
    '$t9': 25,

    '$k0': 26,
    '$k1': 27,

    '$gp': 28,
    '$sp': 29,
    '$fp': 30,
    '$ra': 31,
}

num2reg = {registers_table[key]: key for key in registers_table.keys()}

R1_inst = set([''])


def is_R1(tokens):
    if len(tokens) != 4:
        return False
    else:
        for i in range(1, 4):
            if tokens[i].find('$') == -1:
                return False
    return True


def to_bin(num, n, signed=False):
    if isinstance(num, str):
        try:
            num = int(num)
        except Exception as e:
            try:
                num = int(num, 16)
            except Exception as e:
                num = int(num, 2)

    # if signed:
    #     if num >= 0:
    #         binary = [0] * n
    #     else:
    #         binary = [1] + [0] * (n - 1)
    #         num = -num
    #     p = n - 1
    # else:
    #     binary = [0] * n
    #     p = n - 1
    # while True:
    #     binary[p] = num % 2
    #     num = num // 2
    #     if num == 0 or p == 0:
    #         break
    #     p = p - 1

    v = abs(num)
    if signed:
        if num < 0:
            v = int(pow(2, n)) - v

    binary = [0] * n

    p = n - 1
    while True:
        binary[p] = num % 2
        num = num // 2
        if num == 0 or p == 0:
            break
        p = p - 1

    string = ''
    for i in range(len(binary)):
        string = string + str(binary[i])

    return string


def opcodes(inst):
    global opcodes_table
    code = opcodes_table[inst]
    return to_bin(code, 6)


def funcs(inst):
    global funcs_table
    code = funcs_table[inst]
    return to_bin(code, 6)


def registers(reg):
    global registers_table
    code = registers_table[reg]
    return to_bin(code, 5)


def bin2int(bin, signed=False):
    if not signed:
        num = int(bin, 2)
        return num
    else:
        mag = int(bin, 2)
        if bin[0] == '1':
            mag = mag - int(pow(2, len(bin)))
        return str(mag)


if __name__ == '__main__':
    print(to_bin(8, 32, True))
