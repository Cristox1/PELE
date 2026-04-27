import sys
from antlr4 import *
from PELELexer import PELELexer
from PELEParser import PELEParser
from visitorPELE import EvalVisitor

def main():
    
    with open("programa.txt", "r", encoding="utf-8") as f:
        code = f.read()

    input_stream = InputStream(code)
    lexer = PELELexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PELEParser(stream)
    tree = parser.program()
    
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
