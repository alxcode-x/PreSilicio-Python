from dictionary import Dictionary

class Compiler():

    def execute(self, fileName):
        dic = Dictionary()
        code = []
        index = 0
        f = open(fileName)
        for line in f:
            formated_line = self.format_line(line)
            self.remove_imm(formated_line)
            code.append(dic.assign_opcode(formated_line, index))
            
            index += 1
        f.close()
        self.create_output_file(code, fileName)
            

    def format_line(self, line: str):
        return (line.replace(" ", "")
                    .replace(":", ":,")
                    .replace("\n", "")
                    .replace("\t", "")
                    .lower()
                    .split(","))

    def remove_imm(self, line):
        for item in line:
            if (":" in item):
                line.remove(item)
                break
   

    def create_output_file(self, code, fileName):
        file = open(fileName.split('.')[0]+"-output.txt", "w")
        for line in code:
            for item in line:
                file.write(item)
            file.write("\n")
        file.close

