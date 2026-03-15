import sys
from antlr4 import *
from LenguajeDLLexer import LenguajeDLLexer
from LenguajeDLParser import LenguajeDLParser
from demo_visitor import EvalVisitor

def main():
    code = """
    // --- Pruebas de Strings ---
    saludo = "Hola, bienvenido a LenguajeDL";
    modelo = "Red Neuronal";
    
    // --- Pruebas de Datos Basicos ---
    epocas = 100;
    learning_rate = 0.05;
    entrenamiento_activo = true;
    
    // --- Pruebas de Tensores (Arreglos) ---
    pesos = [0.1, -0.5, 0.8];
    
    // --- Pruebas Matematicas ---
    calculo_potencia = 2 ** 3;
    calculo_modulo = 10 % 3;
    
    // --- Mostrar Resultados ---
    mostrar(saludo);
    mostrar(modelo);
    mostrar(epocas);
    mostrar(entrenamiento_activo);
    mostrar(pesos);
    mostrar(calculo_potencia);
    mostrar(calculo_modulo);
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
