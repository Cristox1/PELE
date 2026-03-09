import sys
from antlr4 import *
from LenguajeDLLexer import LenguajeDLLexer
from LenguajeDLParser import LenguajeDLParser
from demo_visitor import EvalVisitor

def run_code(code):
    input_stream = InputStream(code)
    lexer = LenguajeDLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LenguajeDLParser(stream)
    tree = parser.program()
    visitor = EvalVisitor()
    visitor.visit(tree)

def menu():
    print("\n╔══════════════════════════════════╗")
    print("║     Calculadora - LenguajeDL     ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Suma          (a + b)        ║")
    print("║  2. Resta         (a - b)        ║")
    print("║  3. Multiplicación(a * b)        ║")
    print("║  4. División      (a / b)        ║")
    print("║  5. Módulo        (a % b)        ║")
    print("║  6. Potencia      (a ** b)       ║")
    print("║  7. Comparación   (a == b, etc.) ║")
    print("║  8. Lógica        (and, or, not) ║")
    print("║  0. Salir                        ║")
    print("╚══════════════════════════════════╝")

def pedir_dos_numeros():
    a = input("  Ingresa el primer número: ")
    b = input("  Ingresa el segundo número: ")
    return a, b

def main():
    print("\n¡Bienvenido a LenguajeDL!")

    while True:
        menu()
        opcion = input("\n¿Qué quieres hacer hoy? (0-9): ").strip()

        try:
            if opcion == '0':
                print("¡Hasta luego!")
                break

            elif opcion == '1':
                a, b = pedir_dos_numeros()
                run_code(f"resultado = {a} + {b}; print(resultado);")

            elif opcion == '2':
                a, b = pedir_dos_numeros()
                run_code(f"resultado = {a} - {b}; print(resultado);")

            elif opcion == '3':
                a, b = pedir_dos_numeros()
                run_code(f"resultado = {a} * {b}; print(resultado);")

            elif opcion == '4':
                a, b = pedir_dos_numeros()
                run_code(f"resultado = {a} / {b}; print(resultado);")

            elif opcion == '5':
                a, b = pedir_dos_numeros()
                run_code(f"resultado = {a} % {b}; print(resultado);")

            elif opcion == '6':
                a, b = pedir_dos_numeros()
                run_code(f"resultado = {a} ** {b}; print(resultado);")

            elif opcion == '7':
                a = input("  Ingresa el primer número: ")
                op = input("  Operador (==, !=, <, <=, >, >=): ").strip()
                b = input("  Ingresa el segundo número: ")
                run_code(f"resultado = {a} {op} {b}; print(resultado);")

            elif opcion == '8':
                print("  Ejemplos: 'true and false', 'not true', '5 > 3 or 2 == 1'")
                expr = input("  Escribe tu expresión lógica: ").strip()
                run_code(f"resultado = {expr}; print(resultado);")

            elif opcion == '9':
                print("  Modo libre: escribe código en LenguajeDL.")
                print("  Escribe 'FIN' en una línea sola para ejecutar.\n")
                lines = []
                while True:
                    line = input("  > ")
                    if line.strip() == 'FIN':
                        break
                    lines.append(line)
                run_code("\n".join(lines))

            else:
                print("  Opción no válida, intenta de nuevo.")

        except Exception as e:
            print(f"\n  ⚠ Error: {e}")

if __name__ == '__main__':
    main()