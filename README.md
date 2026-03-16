# PELE - Proyecto de Lenguaje de Programacion

Este repositorio contiene la primera fase del desarrollo de un lenguaje de programacion construido desde cero, diseñado con una orientacion futura hacia el Deep Learning. El proyecto utiliza ANTLR4 para la generacion del analizador lexico y sintactico, y Python como lenguaje anfitrion para la logica de evaluacion.

## Caracteristicas Actuales (Fase 1)

En esta primera entrega de avance, el lenguaje soporta las siguientes caracteristicas fundamentales:

*   **Tipos de datos:** Soporte nativo para numeros enteros (INT), de punto flotante (FLOAT), valores booleanos (true, false) y cadenas de texto (Strings).
*   **Estructuras de datos basicas:** Soporte para arreglos (listas) de una dimension, sentando las bases para futuros tensores o matrices.
*   **Asignacion de variables:** Capacidad de almacenar y recuperar valores en memoria durante la ejecucion del programa.
*   **Operaciones aritmeticas extendidas:** Suma (+), resta (-), multiplicacion (*), division (/), modulo (%) y potencia (**). Incluye soporte para numeros negativos (menos unario) respetando estrictamente la precedencia de operadores.
*   **Operadores relacionales:** Capacidad de comparar expresiones y variables utilizando los operadores <, <=, >, >=, == y !=.
*   **Control de flujo basico:** Sentencias delimitadas por punto y coma (;) y funcion nativa de impresion en consola mediante la instruccion `mostrar()`.

## Estructura del Proyecto

El proyecto se compone de tres archivos principales creados manualmente, mas los archivos subyacentes generados por la herramienta ANTLR4:

*   `PELE.g4`: Archivo principal de gramatica. Define las reglas lexicas (tokens) y sintacticas (relaciones estructurales) de nuestro lenguaje.
*   `visitorPELE.py`: Implementa el patron de diseño Visitor extendiendo las clases generadas por ANTLR. Contiene la logica en Python que le da significado y accion a las operaciones definidas en la gramatica (el "cerebro" del lenguaje).
*   `pele.py`: Archivo de entrada principal que inicializa el flujo de datos: pasa el codigo fuente al Lexer, luego al Parser, construye el arbol de sintaxis y finalmente lo recorre utilizando el Visitor.

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

Cada vez que se realicen modificaciones estructurales en el archivo de gramatica (`PELE.g4`), es estrictamente necesario volver a generar los analizadores.

1.  **Generar el codigo de ANTLR:**
    Ejecuta el siguiente comando en la raiz del proyecto para que ANTLR genere los archivos de Python correspondientes.
    ```bash
    antlr4 -Dlanguage=Python3 -visitor PELE.g4
    ```

2.  **Ejecutar el programa de prueba:**
    Una vez generados los archivos, puedes ejecutar el interprete para evaluar el codigo fuente definido.
    ```bash
    python pele.py
    ```

## Ejemplo de Codigo en PELE

El archivo `pele.py` procesa internamente un bloque de codigo escrito en PELE similar a este:

```text
    // Pruebas de Strings
    saludo = "Hola mundo con PELE";
    
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
    mostrar(entero);
    mostrar(double);
    mostrar(activo);
    mostrar(pesos);
    mostrar(potencia);
    mostrar(modulo);
```
