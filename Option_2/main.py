import sys
from compiler import Compiler

if __name__ == "__main__":
    comp = Compiler()
    comp.execute(sys.argv[1])
