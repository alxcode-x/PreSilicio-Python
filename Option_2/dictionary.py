class Dictionary:

    opcodes = {
        "x0":   "00000000",
        "x1":   "00000001",
        "x2":   "00000010",
        "x3":   "00000011",
        "x4":   "00000100",
        "x5":   "00000101",
        "x6":   "00000110",
        "x7":   "00000111",
        "add":  "00000000",
        "addi": "00000001",
        "and":  "00000010",
        "andi": "00000011",
        "beq":  "00000100",
        "bne":  "00000101",
        "j":    "00000110",
        "jal":  "00000111",
        "jr":   "00001010",
        "lb":   "00001011",
        "or":   "00001100",
        "sb":   "00001101",
        "sll":  "00001110",
        "srl":  "00001111",
    }

    imms = {
        "main": 1,
        "inc":  4,
        "func": 8,
        "dec":  9,
        "exit": 15    
    }

    def assign_opcode(self, items,line_position):
        opcode_list = []
        opcode_ordered = []
        for item in items:
            if(item in self.opcodes):
                opcode_list.append(self.opcodes[item])
            elif(item in self.imms):
                opcode_list.append(self.convert_imm(self.imms[item], line_position))
            elif("-" in item):
                opcode_list.append(self.a2_comp(item[1:]))
            elif("0x" in item):
                opcode_list.append(self.hex_to_bin(item))
            elif(item.isdigit()):
                opcode_list.append(self.dec_to_bin(item))
            else:
                opcode_list.append("xxxxxErr")
        
        return self.order_opcode_list(opcode_list)  


    def a2_comp(self, dec):
        a = []
        b = []
        binary = bin(int(dec))[2:].zfill(8)
        bin_back = binary[::-1]

        flag = False
        for item in bin_back:
            if (flag == True):
                if(item == '0'):
                    b.append('1')
                else:
                    b.append('0')
            else:
                if (item == '1' and flag == False):
                    a.append(item)
                    flag = True
                else:
                    a.append(item)
        
        a_b = a + b
        c_a2 ="".join([str(item) for item in a_b])
        return c_a2[::-1]


    def hex_to_bin(self, hex):
        return bin(int(hex, 16))[2:].zfill(8)


    def dec_to_bin(self, dec):
        return bin(int(dec))[2:].zfill(8)


    def convert_imm(self, imm, position):
        if(imm>position):
            return bin(imm)[2:].zfill(8)
        else:
            return self.a2_comp(imm)

    
    def order_opcode_list(self, list):
        ordered_list = []
        if(list[0] == '00000000' or list[0] == '00001100'):
            ordered_list = (list[0][4:8], list[2][5:8], list[3][5:8], list[1][5:8], '00000')

        elif(list[0] == '00000001' or list[0] == '00000011'):
            ordered_list = (list[0][4:8], list[2][5:8], list[1][5:8], list[3])
            
        elif(list[0] == '00000010'):
            ordered_list = (list[0][4:8], list[2][5:8], list[3][5:8], list[1][5:8], '00000')

        elif(list[0] == '00000100' or list[0] == '00000101'):
            ordered_list = (list[0][4:8], list[1][5:8], list[2][5:8], list[3])

        elif(list[0] == '00000110' or list[0] == '00000111'):
            ordered_list = (list[0][4:8], list[1].zfill(14))

        elif(list[0] == '00001010'):
            ordered_list = (list[0][4:8], list[1][5:8], '0000000000')
        
        elif(list[0] == '00001101' or list[0] == '00001011'):
            ordered_list = (list[0][4:8], list[3][5:8], list[1][5:8], list[2])

        elif(list[0] == '00001110' or list[0] == '00001111'):
            ordered_list = (list[0][4:8], list[3][5:8], list[2][5:8], list[1])

        return ordered_list