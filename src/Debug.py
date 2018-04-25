from Utils import *


def run(code, regs, PC, labels):
    # print(code)
    if code[0:6] == '000000' and code[21:32] == '00000100000':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        rd = num2reg[bin2int(code[16:21])]
        # code = 'add' + ' ' + rd + ', ' + rs + ', ' + rt
        regs[rd] = regs[rs] + regs[rt]
        PC = PC + 4

    elif code[0:6] == '001000':
        # print(bin2int(code[6:11]))
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        imm = bin2int(code[16:32], True)
        # code = 'addi' + ' ' + rt + ', ' + rs + ', ' + imm
        regs[rt] = regs[rs] + int(imm)
        PC = PC + 4

    elif code[0:6] == '000000' and code[21:32] == '00000100100':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        rd = num2reg[bin2int(code[16:21])]
        # code = 'and' + ' ' + rd + ', ' + rs + ', ' + rt
        regs[rd] = (regs[rs] & regs[rt])
        PC = PC + 4

    elif code[0:6] == '000100':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        imm_str = bin2int(code[16:32], True)
        imm = int(imm_str)
        if imm not in labels:
            label = 'L{}'.format(imm + PC // 4 + 1)
            labels[imm + PC // 4 + 1] = label
        # L = labels[imm + PC // 4 + 1]
        # code = 'beq' + ' ' + rs + ', ' + rt + ', ' + L
        if regs[rs] == regs[rt]:
            PC = PC + 4 + imm * 4
        else:
            PC = PC + 4

    elif code[0:6] == '000101':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        imm_str = bin2int(code[16:32], True)
        imm = int(imm_str)
        if imm not in labels:
            label = 'L{}'.format(imm + PC // 4 + 1)
            labels[imm + PC // 4 + 1] = label
        # L = labels[imm + PC // 4 + 1]
        # code = 'bne' + ' ' + rs + ', ' + rt + ', ' + L
        if regs[rs] != regs[rt]:
            PC = PC + 4 + imm * 4
        else:
            PC = PC + 4

    elif code[0:6] == '000010':
        imm_str = bin2int(code[6:32], True)
        imm = int(imm_str)
        if imm not in labels:
            label = 'L{}'.format(imm + PC // 4 + 1)
            labels[imm + PC // 4 + 1] = label
        # L = labels[imm + PC // 4]
        # code = 'j' + ' ' + L
        PC = (PC & 0xf0000000) + imm * 4

    elif code[0:6] == '000011':
        imm_str = bin2int(code[6:32], True)
        imm = int(imm_str)
        if imm not in labels:
            label = 'L{}'.format(imm + PC // 4 + 1)
            labels[imm + PC // 4 + 1] = label
        # L = labels[imm + PC // 4]
        # code = 'jal' + ' ' + L
        PC = (PC & 0xf0000000) + imm * 4

    elif code[0:6] == 000000 and code[11:32] == '000000000000000001000':
        rs = num2reg[bin2int(code[6:11])]
        # code = 'jr' + ' ' + rs
        PC = regs[rs]

    elif code[0:6] == '100011':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        imm = bin2int(code[16:32], True)
        # code = 'lw' + ' ' + rt + ', ' + imm + '(' + rs + ')'
        PC = PC + 4  # not implement

    elif code[0:6] == '001111':
        rt = num2reg[bin2int(code[11:16])]
        imm = bin2int(code[16:32], True)
        # code = 'lui' + ' ' + rt + ', ' + imm
        regs[rt] = bin2int(code[16:32] + '0' * 16, True)
        PC = PC + 4

    elif code[0:6] == '000000' and code[21:32] == '00000100101':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        rd = num2reg[bin2int(code[16:21])]
        # code = 'or' + ' ' + rd + ', ' + rs + ', ' + rt
        regs[rd] = (regs[rs] | regs[rt])
        PC = PC + 4

    elif code[0:6] == '001101':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        imm = bin2int(code[16:32], True)
        # code = 'ori' + ' ' + rt + ', ' + rs + ', ' + imm
        regs[rt] = (regs[rs] | int(imm))
        PC = PC + 4

    elif code[0:6] == '000000' and code[26:32] == '000000':
        # rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        rd = num2reg[bin2int(code[16:21])]
        h = bin2int(code[21:26], True)
        # code = 'sll' + ' ' + rd + ', ' + rt + ', ' + h
        regs[rd] = (regs[rt] << int(h))
        PC = PC + 4

    elif code[0:6] == '000000' and code[21:32] == '00000101010':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        rd = num2reg[bin2int(code[16:21])]
        # code = 'slt' + ' ' + rd + ', ' + rs + ', ' + rt
        regs[rd] = (regs[rs] < regs[rt])
        PC = PC + 4

    elif code[0:6] == '001010':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        imm = bin2int(code[16:32], True)
        # code = 'slti' + ' ' + rt + ', ' + rs + ', ' + imm
        regs[rt] = (regs[rs] < int(imm))
        PC = PC + 4

    elif code[0:6] == '000000' and code[26:32] == '000010':
        # rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        rd = num2reg[bin2int(code[16:21])]
        h = bin2int(code[21:26], True)
        # code = 'srl' + ' ' + rd + ', ' + rt + ', ' + h
        regs[rd] = (regs[rt] << int(h))
        PC = PC + 4

    elif code[0:6] == '101011':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        imm = bin2int(code[16:32], True)
        # code = 'sw' + ' ' + rt + ', ' + imm + '(' + rs + ')'
        PC = PC + 4

    elif line[0:6] == '000000' and line[21:32] == '00000100010':
        rs = num2reg[bin2int(line[6:11])]
        rt = num2reg[bin2int(line[11:16])]
        rd = num2reg[bin2int(line[16:21])]
        # code = 'sub' + ' ' + rd + ', ' + rs + ', ' + rt
        regs[rd] = regs[rs] - regs[rt]
        PC = PC + 4

    # extension ----------------------------------------------

    # xor
    elif code[0:6] == '000000' and code[26:32] == '100110':
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        rd = num2reg[bin2int(code[16:21])]
        regs[rd] = (regs[rs] ^ regs[rt])
        PC = PC + 4

    # xori
    elif code[0:6] == '001110':
        # print(bin2int(code[6:11]))
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        imm = bin2int(code[16:32], True)
        # code = 'addi' + ' ' + rt + ', ' + rs + ', ' + imm
        regs[rt] = (regs[rs] ^ int(imm))
        PC = PC + 4

    # andi
    elif code[0:6] == '001100':
        # print(bin2int(code[6:11]))
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        imm = bin2int(code[16:32], True)
        regs[rt] = (regs[rs] & int(imm))
        PC = PC + 4

    # ori
    elif code[0:6] == '001101':
        # print(bin2int(code[6:11]))
        rs = num2reg[bin2int(code[6:11])]
        rt = num2reg[bin2int(code[11:16])]
        imm = bin2int(code[16:32], True)
        regs[rt] = (regs[rs] | int(imm))
        PC = PC + 4

    return regs, PC
