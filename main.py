import sys
from antlr4 import *
# Importamos los nuevos archivos generados
from LenguajeDLLexer import LenguajeDLLexer
from LenguajeDLParser import LenguajeDLParser
# Importamos tu clase EvalVisitor desde tu nuevo archivo demo_visitor.py
from demo_visitor import EvalVisitor

def main():
    code = """
    // Configuración variables
    variable_1 = 100;
    variable_2 = 50;
    
    // Probabilidades (¡ahora ya entiende los negativos!)
    probabilidades = [0.5, -0.2, 0.1];
    
    // Un cálculo simple
    variable_1_n = variable_1 * 2.5;
    
    print(variable_1);
    print(probabilidades);
    print(variable_1_n);
    """

    input_stream = InputStream(code)
    
    # Instanciamos el Lexer y Parser con los nuevos nombres
    lexer = LenguajeDLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    parser = LenguajeDLParser(stream)
    tree = parser.program()
    
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()