# LenguajeDL - Proyecto de Lenguaje de Programacion

Este repositorio contiene la primera fase del desarrollo de un lenguaje de programacion construido desde cero, diseñado con una orientacion futura hacia el Deep Learning. El proyecto utiliza ANTLR4 para la generacion del analizador lexico y sintactico, y Python como lenguaje anfitrion para la logica de evaluacion.

## Caracteristicas Actuales (Fase 1)

En esta primera entrega de avance, el lenguaje soporta las siguientes caracteristicas fundamentales:

*   **Tipos de datos numericos:** Soporte nativo para numeros enteros (INT) y de punto flotante (FLOAT), esenciales para el futuro manejo de hiperparametros, pesos y sesgos.
*   **Estructuras de datos basicas:** Soporte para arreglos (listas) de una dimension, sentando las bases para futuros tensores o matrices.
*   **Asignacion de variables:** Capacidad de almacenar y recuperar valores en memoria durante la ejecucion del programa.
*   **Operaciones aritmeticas:** Suma, resta, multiplicacion, division y soporte para numeros negativos (menos unario), respetando la precedencia de operadores.
*   **Control de flujo basico:** Sentencias delimitadas por punto y coma (;) y funcion nativa de impresion (print).

## Estructura del Proyecto

El proyecto se compone de tres archivos principales creados manualmente, mas los archivos subyacentes generados por la herramienta ANTLR4:

*   `LenguajeDL.g4`: Archivo principal de gramatica. Define las reglas lexicas (tokens) y sintacticas (relaciones estructurales) de nuestro lenguaje.
*   `demo_visitor.py`: Implementa el patron de diseño Visitor extendiendo las clases generadas por ANTLR. Contiene la logica en Python que le da significado y accion a las operaciones definidas en la gramatica (el "cerebro" del lenguaje).
*   `main.py`: Archivo de entrada principal que inicializa el flujo de datos: pasa el codigo fuente al Lexer, luego al Parser, construye el arbol de sintaxis y finalmente lo recorre utilizando el Visitor.

## Requisitos Previos

Para compilar y ejecutar este proyecto, el entorno debe contar con:

1.  Python 3.x
2.  Java (necesario para ejecutar la herramienta de generacion de codigo de ANTLR4)
3.  La herramienta de linea de comandos de ANTLR4 instalada.

## Instalacion y Configuracion

A continuacion, se detallan los pasos para configurar el entorno de desarrollo en sistemas basados en Unix (Linux/macOS):

1.  **Crear un entorno virtual:**
    Se recomienda usar un entorno virtual para aislar las dependencias del proyecto del resto del sistema operativo.
    ```bash
    python3 -m venv env
    ```

2.  **Activar el entorno virtual:**
    ```bash
    source env/bin/activate
    ```

3.  **Instalar las dependencias de Python:**
    Se requiere instalar el runtime de ANTLR4 especifico para Python 3.
    ```bash
    pip install antlr4-python3-runtime
    ```

## Compilacion y Ejecucion

Cada vez que se realicen modificaciones estructurales en el archivo de gramatica (`LenguajeDL.g4`), es estrictamente necesario volver a generar los analizadores.

1.  **Generar el codigo de ANTLR:**
    Ejecuta el siguiente comando en la raiz del proyecto para que ANTLR genere los archivos de Python correspondientes.
    ```bash
    antlr4 -Dlanguage=Python3 -visitor LenguajeDL.g4
    ```

2.  **Ejecutar el programa de prueba:**
    Una vez generados los archivos, puedes ejecutar el interprete para evaluar el codigo fuente definido.
    ```bash
    python main.py
    ```

## Ejemplo de Codigo en LenguajeDL

El archivo `main.py` procesa internamente un bloque de codigo escrito en LenguajeDL similar a este:

```text
// Configuracion de variables
variable_1 = 100;
variable_2 = 50;

// Probabilidades y pesos (soporte para flotantes y negativos)
probabilidades = [0.5, -0.2, 0.1];

// Calculo con variables
variable_1_n = variable_1 * 2.5;

print(variable_1);
print(probabilidades);
print(variable_1_n);
```
# LenguajeDL
