import sys
from antlr4 import *
from LenguajeDLLexer import LenguajeDLLexer
from LenguajeDLParser import LenguajeDLParser
from demo_visitor import EvalVisitor

def main():
    code = """
    // Pruebas de Strings
    saludo = "Hola, bienvenido a LenguajeDL";
    modelo = "Red Neuronal";
    
    // Pruebas de Datos Basicos
    entero = 100;
    double = 0.05;
    activo = true;
    
    // Pruebas de Arreglos
    pesos = [0.1, -0.5, 0.8];
    
    // Pruebas Matematicas
    potencia = 2 ** 3;
    modulo = 10 % 3;
    
    // Mostrar Resultados
    mostrar(saludo);
    mostrar(modelo);
    mostrar(entero);
    mostrar(double);
    mostrar(activo);
    mostrar(pesos);
    mostrar(potencia);
    mostrar(modulo);
    """

    input_stream = InputStream(code)
    lexer = LenguajeDLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LenguajeDLParser(stream)
    tree = parser.program()
    
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
