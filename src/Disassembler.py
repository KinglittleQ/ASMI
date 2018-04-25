from Utils import *


def disassembler(lines):
    codes = []
    labels = {}

    for i, line in enumerate(lines):
        code = ''

        if line[0:6] == '000000' and line[21:32] == '00000100000':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            rd = num2reg[bin2int(line[16:21])]
            code = 'add' + ' ' + rd + ', ' + rs + ', ' + rt

        elif line[0:6] == '001000':
            # print(bin2int(line[6:11]))
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            imm = bin2int(line[16:32], True)
            code = 'addi' + ' ' + rt + ', ' + rs + ', ' + imm

        elif line[0:6] == '000000' and line[21:32] == '00000100100':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            rd = num2reg[bin2int(line[16:21])]
            code = 'and' + ' ' + rd + ', ' + rs + ', ' + rt

        elif line[0:6] == '000100':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            imm_str = bin2int(line[16:32], True)
            imm = int(imm_str)
            if imm not in labels:
                label = 'L{}'.format(imm + i + 1)
                labels[imm + i + 1] = label
            L = labels[imm + i + 1]
            code = 'beq' + ' ' + rs + ', ' + rt + ', ' + L

        elif line[0:6] == '000101':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            imm_str = bin2int(line[16:32], True)
            imm = int(imm_str)
            if imm not in labels:
                label = 'L{}'.format(imm + i + 1)
                labels[imm + i + 1] = label
            L = labels[imm + i + 1]
            code = 'bne' + ' ' + rs + ', ' + rt + ', ' + L

        elif line[0:6] == '000010':
            imm_str = bin2int(line[6:32], True)
            imm = int(imm_str)
            if imm not in labels:
                label = 'L{}'.format(imm)
                labels[imm] = label
            L = labels[imm]
            code = 'j' + ' ' + L

        elif line[0:6] == '000011':
            imm_str = bin2int(line[6:32], True)
            imm = int(imm_str)
            if imm not in labels:
                label = 'L{}'.format(imm - i)
                labels[imm] = label
            L = labels[imm]
            code = 'jal' + ' ' + L

        elif line[0:6] == 000000 and line[11:32] == '000000000000000001000':
            rs = num2reg[bin2int(line[6:11])]
            code = 'jr' + ' ' + rs

        elif line[0:6] == '100011':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            imm = bin2int(line[16:32], True)
            code = 'lw' + ' ' + rt + ', ' + imm + '(' + rs + ')'

        elif line[0:6] == '001111':
            rt = num2reg[bin2int(line[11:16])]
            imm = bin2int(line[16:32], True)
            code = 'lui' + ' ' + rt + ', ' + imm

        elif line[0:6] == '000000' and line[21:32] == '00000100101':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            rd = num2reg[bin2int(line[16:21])]
            code = 'or' + ' ' + rd + ', ' + rs + ', ' + rt

        elif line[0:6] == '001101':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            imm = bin2int(line[16:32], True)
            code = 'ori' + ' ' + rt + ', ' + rs + ', ' + imm

        elif line[0:6] == '000000' and line[26:32] == '000000':
            # rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            rd = num2reg[bin2int(line[16:21])]
            h = bin2int(line[21:26], True)
            code = 'sll' + ' ' + rd + ', ' + rt + ', ' + h

        elif line[0:6] == '000000' and line[21:32] == '00000101010':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            rd = num2reg[bin2int(line[16:21])]
            code = 'slt' + ' ' + rd + ', ' + rs + ', ' + rt

        elif line[0:6] == '001010':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            imm = bin2int(line[16:32], True)
            code = 'slti' + ' ' + rt + ', ' + rs + ', ' + imm

        elif line[0:6] == '000000' and line[26:32] == '000010':
            # rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            rd = num2reg[bin2int(line[16:21])]
            h = bin2int(line[21:26], True)
            code = 'srl' + ' ' + rd + ', ' + rt + ', ' + h

        elif line[0:6] == '101011':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            imm = bin2int(line[16:32], True)
            code = 'sw' + ' ' + rt + ', ' + imm + '(' + rs + ')'

        elif line[0:6] == '000000' and line[21:32] == '00000100010':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            rd = num2reg[bin2int(line[16:21])]
            code = 'sub' + ' ' + rd + ', ' + rs + ', ' + rt

        # extension ------------------------------------

        # xor
        elif line[0:6] == '000000' and code[26:32] == '100110':
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            rd = num2reg[bin2int(line[16:21])]
            code = 'xor' + ' ' + rd + ', ' + rs + ', ' + rt

        elif line[0:6] == '001110':
            # print(bin2int(line[6:11]))
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            imm = bin2int(line[16:32], True)
            code = 'xori' + ' ' + rt + ', ' + rs + ', ' + imm

        elif line[0:6] == '001100':
            # print(bin2int(line[6:11]))
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            imm = bin2int(line[16:32], True)
            code = 'andi' + ' ' + rt + ', ' + rs + ', ' + imm

        elif line[0:6] == '001101':
            # print(bin2int(line[6:11]))
            rs = num2reg[bin2int(line[6:11])]
            rt = num2reg[bin2int(line[11:16])]
            imm = bin2int(line[16:32], True)
            code = 'ori' + ' ' + rt + ', ' + rs + ', ' + imm

        codes.append(code)

    result = []
    for i in range(len(codes)):
        if i in labels:
            result.append(labels[i] + ':')
        result.append(codes[i])

    return result


if __name__ == '__main__':
    f = open('bin.txt')
    bins = f.readline()
    lines = []
    for i in range(len(bins) // 32):
        lines.append(bins[i * 32:(i + 1) * 32])

    print(lines)
    print(disassembler(lines))
