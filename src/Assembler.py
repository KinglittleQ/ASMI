from enum import Enum
from Utils import *


class MIPS():

    def __init__(self):
        self.PC = 0x00000000
        self.labels = {}
        self.codes = []
        self.line_table = None
        self.base_addr = 0x00000000
        self.data_addr = 0x00000000
        self.lines = None

    def hexs(self):
        table = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        hexs = []
        for code in self.codes:
            h = ''
            num = int(code, 2)
            n = 0
            while True:
                if num % 16 < 10:
                    s = str(num % 16)
                else:
                    s = table[num % 16]
                h = s + h
                num = num // 16
                n = n + 1
                if n == 8:
                    break
            hexs.append(h)
        return hexs


# @unique
class Type(Enum):
    R1 = 0
    R2 = 1
    I1 = 2
    I2 = 3
    I3 = 4
    J = 5
    Jr = 6
    Addr = 7
    Label = 8
    Others = 9


def assembler(lines):
    mips = MIPS()
    lines = delete_comment(lines)
    lines = format_mips(lines)

    mips.lines = lines

    # last_t = None

    for line in lines:
        tokens, t = split(line)
        if t == Type.Addr:
            if tokens[0] == 'BaseAddr':
                mips.base_addr = int(tokens[1], 16)
            elif tokens[1] == 'DataAddr':
                mips.data_addr = int(tokens[1], 16)
        elif t == Type.Label:
            mips.labels[tokens[0]] = mips.PC
        else:
            mips.PC += 4

    mips.PC = 0x00000000

    n = 0
    line_table = {}
    for i, line in enumerate(lines):
        tokens, t = split(line)

        # print(t)

        if t != Type.Addr and t != Type.Label and t != Type.Others:
            line_table[n] = i
            n = n + 1

        if t == Type.Addr:
            if tokens[0] == 'BaseAddr':
                mips.base_addr = int(tokens[1], 16)
            elif tokens[1] == 'DataAddr':
                mips.data_addr = int(tokens[1], 16)
        elif t == Type.Label:
            mips.labels[tokens[0]] = mips.PC
        elif t == Type.R1:  # no shift
            opcode = opcodes(tokens[0])
            rd = registers(tokens[1])
            rs = registers(tokens[2])
            rt = registers(tokens[3])
            shamt = 5 * '0'
            func = funcs(tokens[0])

            code = opcode + rs + rt + rd + shamt + func
            mips.codes.append(code)

            mips.PC += 4
        elif t == Type.R2:  # shift  sll, srl
            opcode = opcodes(tokens[0])
            rs = 5 * '0'
            rd = registers(tokens[1])
            rt = registers(tokens[2])
            shamt = to_bin(tokens[3], 5)
            func = funcs(tokens[0])
            code = opcode + rs + rt + rd + shamt + func
            mips.codes.append(code)

            mips.PC += 4
        elif t == Type.I1:  # immediate number
            opcode = opcodes(tokens[0])
            rs = registers(tokens[1])
            rt = registers(tokens[2])
            imme = to_bin(tokens[3], 16, signed=True)

            code = opcode + rt + rs + imme
            mips.codes.append(code)

            mips.PC += 4
        elif t == Type.I2:  # () lw, sw
            opcode = opcodes(tokens[0])
            rs = registers(tokens[1])
            rt = registers(tokens[3])
            imme = to_bin(tokens[2], 16, signed=True)

            code = opcode + rs + rt + imme
            mips.codes.append(code)

            mips.PC += 4
        elif t == Type.I3:  # bne beq
            opcode = opcodes(tokens[0])
            rs = registers(tokens[1])
            rt = registers(tokens[2])
            # rs = registers(tokens[1])
            # rt = registers(tokens[2])
            offset = mips.labels[tokens[3]] - (mips.PC + 4)
            imme = to_bin(offset // 4, 16, True)

            code = opcode + rs + rt + imme
            mips.codes.append(code)

            mips.PC += 4
        elif t == Type.J:
            opcode = opcodes(tokens[0])
            if isinstance(tokens[1], int):
                target = to_bin(tokens[1], 26)
            elif isinstance(tokens[1], str):
                target = to_bin(mips.labels[tokens[1]] // 4, 26)

            code = opcode + target
            mips.codes.append(code)

            mips.PC += 4
        elif t == Type.Jr:
            opcode = opcodes(tokens[0])
            r = registers(tokens[1])

            code = opcode + r + '0' * 21
            mips.codes.append(code)

            mips.PC += 4

        # last_t = t

    mips.line_table = line_table

    return mips


def delete_comment(lines):
    result = []
    for line in lines:
        new_line = ''
        for i in range(len(line)):
            if line[i] == '#':
                break
            else:
                new_line += line[i]
        new_line = new_line.strip().strip(';')
        if new_line:
            result.append(new_line)
    return result


def format_mips(lines):
    result = []
    for line in lines:
        line = line.lower()
        pos = line.find(':')
        if pos != -1:
            line1 = line[:pos].strip()
            if line1 == 'BaseAddr' or line1 == 'DataAddr':
                result.append(line1 + line[pos + 1:])
            else:
                line2 = line[pos + 1:].strip()
                result.append(line1)
                if line2:
                    result.append(line2)
        else:
            result.append(line)
    return result


def split(line):
    t = Type.Others
    tokens1 = line.split()
    tokens = []
    for i in range(len(tokens1)):
        tokens1[i] = tokens1[i].strip(',')
        tokens += tokens1[i].split(',')
    # print(tokens)
    if tokens[0] == 'BaseAddr' or tokens[0] == 'DataAddr':
        t = Type.Addr
    elif len(tokens) == 1:
        t = Type.Label
    elif is_R1(tokens):  # add sub ...  R1
        t = Type.R1
    elif tokens[0] == 'sll' or tokens[0] == 'srl':  # R2
        t = Type.R2
    elif len(tokens) == 4 and (tokens[3].isdigit() or tokens[3][0] == '-'):  # I1
        t = Type.I1
    elif len(tokens) == 3 and line.find('(') != -1:  # I2 lw, sw ()
        t = Type.I2
        imm, reg = tokens[2].split('(')
        tokens[2] = imm
        tokens.append(reg.strip(')'))
    elif len(tokens) == 4:
        t = Type.I3
    elif len(tokens) == 2 and tokens[1].find('$') == -1:
        t = Type.J
    elif len(tokens) == 2 and tokens[1].find('$') != -1:
        t = Type.Jr
    else:
        t = Type.Others

    return tokens, t


if __name__ == '__main__':
    with open('D:/code/Python3/MIPS/02.txt') as f:
        lines = list(f.readlines())
        for line in lines:
            print(line)
        mips = assembler(lines)
        print(mips.hexs())
