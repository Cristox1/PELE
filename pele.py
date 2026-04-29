import sys
from antlr4 import *
from PELELexer import PELELexer
from PELEParser import PELEParser
from visitorPELE import EvalVisitor

def run_code(code: str, stop_on_error: bool = False) -> None:
    input_stream = InputStream(code)
    lexer = PELELexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PELEParser(stream)
    tree = parser.program()
    visitor = EvalVisitor()
    visitor.stop_on_error = stop_on_error
    visitor.visit(tree)

def main():
    with open("programa.txt", "r", encoding="utf-8") as f:
        code = f.read()
    run_code(code)

if __name__ == '__main__':
    main()