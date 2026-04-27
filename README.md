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
# PELE - Avance de implementación

## ¿Qué hice en el proyecto?

En este avance realicé una modificación importante en el intérprete del lenguaje **PELE** para que ya no dependa de código escrito directamente dentro de `pele.py`, sino que pueda leer el programa desde un archivo externo `.txt`.

### Cambios principales realizados

1. **Lectura de código desde archivo**
   - Modifiqué `pele.py` para que lea el contenido de `programa.txt`.
   - Esto permite escribir el código PELE en un archivo de texto separado y luego ejecutarlo desde el intérprete.

2. **Ejecución del programa desde consola**
   - El intérprete toma el archivo `.txt`, lo procesa con ANTLR4 y luego ejecuta las instrucciones.
   - El resultado se muestra directamente por consola usando la función nativa `mostrar()`.

3. **Actualización de la gramática**
   - Se realizaron cambios en `PELE.g4` para preparar el lenguaje para nuevas estructuras.
   - Se reorganizó la gramática para trabajar con bloques y permitir una evolución futura del lenguaje.

4. **Primeras pruebas de estructuras**
   - Se hicieron pruebas con expresiones, variables, arreglos y operaciones básicas.
   - También se preparó el terreno para agregar estructuras más avanzadas del lenguaje.

5. **Mejoras en el intérprete**
   - Se ajustó `visitorPELE.py` para que evalúe correctamente las expresiones del lenguaje.
   - Se trabajó en la lógica de recorrido del árbol sintáctico para que el lenguaje funcione de manera interpretada.

> En este punto, el proyecto ya tiene una base funcional para ejecutar código PELE desde un archivo `.txt`.

---

## ¿Qué dice el README del repositorio actualmente?

Según el README del repositorio [Cristox1/PELE](https://github.com/Cristox1/PELE), este proyecto es la primera fase de un lenguaje de programación construido desde cero, con orientación futura hacia **Deep Learning**.

### Características que el README indica que ya existen

El lenguaje PELE actualmente soporta:

- **Tipos de datos básicos**
  - `INT`
  - `FLOAT`
  - `true` / `false`
  - `Strings`

- **Estructuras de datos básicas**
  - arreglos de una dimensión

- **Asignación de variables**
  - guardar y recuperar valores en memoria durante la ejecución

- **Operaciones aritméticas**
  - suma `+`
  - resta `-`
  - multiplicación `*`
  - división `/`
  - módulo `%`
  - potencia `**`
  - soporte para números negativos

- **Operadores relacionales**
  - `<`
  - `<=`
  - `>`
  - `>=`
  - `==`
  - `!=`

- **Control de flujo básico**
  - sentencias terminadas con `;`
  - función nativa `mostrar()`

---

## Estructura actual del proyecto

El README también explica que el proyecto se compone de tres archivos principales hechos manualmente, más los generados por ANTLR4:

- `PELE.g4`
  - contiene la gramática del lenguaje

- `visitorPELE.py`
  - implementa la lógica de evaluación del lenguaje

- `pele.py`
  - es el archivo de entrada principal que carga y ejecuta el programa

Y además existen varios archivos generados por ANTLR como:

- `PELELexer.py`
- `PELEParser.py`
- `PELEVisitor.py`
- `PELEListener.py`
- archivos `.tokens`
- archivos `.interp`

---

## Relación entre lo que hice y el README

Lo que hice va totalmente alineado con la idea del proyecto, porque el README dice que PELE es un lenguaje en desarrollo, construido desde cero, y que usa ANTLR4 + Python para interpretar el código.

Mi avance encaja como una mejora de la **fase inicial** del lenguaje, ya que:

- permite ejecutar código desde un archivo externo
- hace que el intérprete sea más práctico
- mantiene la base para seguir agregando estructuras del lenguaje
- prepara el proyecto para crecer hacia funcionalidades más complejas en el futuro

---

## Conclusión

En resumen, lo que hice fue convertir el intérprete de PELE en una versión más práctica y funcional, permitiendo que lea y ejecute un programa desde `programa.txt`, en lugar de tener el código incrustado dentro del archivo principal.

Además, el proyecto sigue la línea descrita en su README:  
un lenguaje propio, interpretado con ANTLR4 y Python, con soporte actual para tipos básicos, operaciones, variables, arreglos y salida por consola, y con visión futura hacia estructuras más complejas y aplicaciones relacionadas con Deep Learning.