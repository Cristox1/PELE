# PELE - Proyecto de Lenguaje de Programacion

Este repositorio contiene el desarrollo de un lenguaje de programacion interpretado y construido desde cero, disenado con una orientacion futura hacia el Deep Learning. El proyecto utiliza ANTLR4 para la generacion del analizador lexico y sintactico (Parser/Lexer), y Python como lenguaje anfitrion para la logica de evaluacion y el arbol de sintaxis abstracta (AST).

## Caracteristicas Actuales

El lenguaje PELE ha evolucionado significativamente, logrando la completitud de Turing al soportar las siguientes caracteristicas:

*   **Tipos de datos:** Soporte nativo para numeros enteros (INT), de punto flotante (FLOAT), valores booleanos (true, false) y cadenas de texto (Strings).
*   **Estructuras de datos avanzadas:** Soporte nativo y funciones integradas para Arreglos (listas 1D), Mapas (diccionarios), Pilas, Colas, Conjuntos, Matrices, Arboles y Grafos.
*   **Manejo de Memoria y Ambitos (Scopes):** Sistema de asignacion de variables con soporte para una Pila de Llamadas (Call Stack), lo que permite separar la memoria global de las memorias locales de ejecucion.
*   **Operaciones aritmeticas:** Suma (+), resta (-), multiplicacion (*), division (/), modulo (%) y potencia (**). Incluye soporte para numeros negativos respetando la precedencia de operadores.
*   **Operadores relacionales:** Comparacion logica mediante <, <=, >, >=, == y !=.
*   **Control de flujo condicional:** Ramificacion de codigo utilizando las palabras clave nativas `si` (if), `sino` (elif) y `entonces` (else).
*   **Control de flujo iterativo:** Soporte para bucles a traves de las instrucciones `mientras` (while) y `por` (for).
*   **Funciones y Recursividad:** Declaracion de subrutinas definidas por el usuario con la palabra clave `funcion`, paso de parametros, y devolucion de resultados mediante `retornar`. Soporte absoluto para recursividad pura.

## Estructura del Proyecto

El proyecto se compone de archivos principales creados manualmente, mas los archivos subyacentes generados por la herramienta ANTLR4:

*   `PELE.g4`: Archivo principal de gramatica. Define las reglas lexicas (tokens) y sintacticas del lenguaje.
*   `visitorPELE.py`: Implementa el patron de diseno Visitor extendiendo las clases generadas por ANTLR. Es el "motor semantico" que ejecuta el codigo.
*   `pele.py`: Archivo de entrada principal que lee el archivo fuente, inicializa el pipeline de datos (Lexer -> Parser -> AST) y llama al Visitor.
*   `programa.txt`: Archivo de texto plano donde se escribe el codigo fuente de PELE a ser ejecutado.

## Requisitos Previos

Para compilar y ejecutar este proyecto, el entorno debe contar con:

1.  Python 3.x
2.  Java (necesario para ejecutar la herramienta de generacion de codigo de ANTLR4)
3.  La herramienta de linea de comandos de ANTLR4 instalada.

## Instalacion y Configuracion

Pasos para configurar el entorno de desarrollo en sistemas basados en Unix (Linux/macOS):

1.  **Crear un entorno virtual:**
    ```bash
    python3 -m venv env
    ```

2.  **Activar el entorno virtual:**
    ```bash
    source env/bin/activate
    ```

3.  **Instalar las dependencias de Python:**
    ```bash
    pip install antlr4-python3-runtime
    ```

## Compilacion y Ejecucion

Cada vez que se realicen modificaciones estructurales en la gramatica (`PELE.g4`), es necesario volver a generar los analizadores:

1.  **Generar el codigo de ANTLR:**
    ```bash
    antlr4 -Dlanguage=Python3 -visitor PELE.g4
    ```

2.  **Ejecutar el programa:**
    Asegurate de escribir tu codigo en el archivo `programa.txt` y luego ejecuta el interprete:
    ```bash
    python3 pele.py
    ```

## Ejemplo de Codigo en PELE

El lenguaje ahora es capaz de ejecutar algoritmos complejos como la recursividad. Un ejemplo del codigo que puedes escribir en `programa.txt` es:

```text
    // 1. Condicionales y Ciclos
    por (i = 0; i < 5; i = i + 1) {
        si (i % 2 == 0) {
            mostrar("Es par:");
        } sino (i == 3) {
            mostrar("Es el numero tres");
        } entonces {
            mostrar("Es otro impar");
        }
        mostrar(i);
    }

    // 2. Funciones de usuario y Recursividad
    funcion factorial(n) {
        si (n <= 1) {
            retornar 1;
        }
        retornar n * factorial(n - 1);
    }

    resultado = factorial(5);
    mostrar("El factorial de 5 es:");
    mostrar(resultado);
```

---

# Historial de Avances

## Avances Recientes:

En las ultimas iteraciones, el lenguaje PELE sufrio una transformacion arquitectonica profunda para pasar de ser una calculadora secuencial a un lenguaje de programacion completo:

1. **Lectura de codigo desde archivo:** Se abstrajo la ejecucion hacia `programa.txt` para separar el interprete del codigo fuente.
2. **Control de Flujo:** Se anadieron reglas sintacticas y semanticas para soportar decisiones logicas (`si`, `sino`, `entonces`) y bucles (`por`, `mientras`).
3. **Pila de Llamadas (Call Stack):** Se reemplazo la memoria global estatica por un sistema de contextos dinamicos (Scopes) basados en diccionarios apilados, vital para aislar variables locales.
4. **Funciones Personalizadas:** Se integro el soporte para que el usuario defina bloques de codigo reusables y pueda utilizar la palabra clave `retornar` (implementada mediante interrupciones de excepcion en el arbol AST).
5. **Pruebas Exhaustivas:** Se construyo un script de pruebas robusto que valida todos los tipos de datos, operaciones matematicas, y todas las estructuras de datos complejas (desde arreglos hasta grafos).