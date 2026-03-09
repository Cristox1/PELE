# LenguajeDL - Proyecto de Lenguaje de Programación

Este repositorio contiene el desarrollo de un lenguaje de programación construido desde cero, diseñado con una orientación futura hacia el **Deep Learning**. El proyecto utiliza **ANTLR4** para la generación del analizador léxico y sintáctico, y **Python** como lenguaje anfitrión para la lógica de evaluación mediante el patrón de diseño *Visitor*.

---

## Características Actuales (Fase 1.5)

En esta actualización, el lenguaje ha expandido sus capacidades para soportar operaciones lógicas y matemáticas avanzadas, además de una interfaz interactiva:

* **Tipos de datos numéricos:** Soporte nativo para números enteros (INT), punto flotante (FLOAT) y booleanos (`true`, `false`).
* **Estructuras de datos básicas:** Soporte para arreglos (listas) de una dimensión, sentando las bases para futuros tensores o matrices.
* **Asignación de variables:** Capacidad de almacenar y recuperar valores en memoria durante la ejecución del programa.
* **Operaciones aritméticas extendidas:** Suma (`+`), resta (`-`), multiplicación (`*`), división (`/`), módulo (`%`) y potencia (`**`), respetando la precedencia de operadores.
* **Operadores relacionales:** `<`, `<=`, `>`, `>=`, `==`, `!=`.
* **Operadores lógicos:** `and`, `or`, `not`.
* **Interfaz interactiva:** Menú en terminal para realizar operaciones rápidas o escribir código libre en el lenguaje.
* **Control de flujo básico:** Sentencias delimitadas por punto y coma (`;`) y función nativa de impresión (`print`).

---

## Estructura del Proyecto

El proyecto se compone de tres archivos principales creados manualmente, más los archivos subyacentes generados por la herramienta ANTLR4:

* `LenguajeDL.g4`
  Archivo principal de gramática. Define las reglas léxicas (tokens) y sintácticas (relaciones estructurales) del lenguaje, incluyendo la precedencia de todos los operadores.

* `demo_visitor.py`
  Implementa el patrón de diseño **Visitor** extendiendo las clases generadas por ANTLR. Contiene la lógica en Python que le da significado y acción a todas las operaciones definidas en la gramática (el "cerebro" del lenguaje).

* `main.py`
  Archivo de entrada principal. Gestiona el menú interactivo en terminal e inicializa el flujo de datos: pasa el código fuente al Lexer, luego al Parser, construye el árbol de sintaxis y lo recorre con el Visitor.

---

## Requisitos Previos

Para compilar y ejecutar este proyecto, el entorno debe contar con:

1. Python 3.x
2. Java (necesario para ejecutar la herramienta de generación de código de ANTLR4)
3. La herramienta de línea de comandos de ANTLR4 instalada

---

## Instalación y Configuración

A continuación se detallan los pasos para configurar el entorno de desarrollo en sistemas basados en Unix (Linux/macOS).

### 1. Crear un entorno virtual

```bash
python3 -m venv env
```

### 2. Activar el entorno virtual

```bash
source env/bin/activate
```

### 3. Instalar las dependencias de Python

```bash
pip install antlr4-python3-runtime
```

---

## Compilación y Ejecución

Cada vez que se realicen modificaciones en el archivo de gramática (`LenguajeDL.g4`), es necesario volver a generar los analizadores.

### Limpiar archivos generados anteriores (recomendado)

```bash
rm -f LenguajeDL*.py LenguajeDL*.tokens LenguajeDL*.interp
rm -rf __pycache__ .antlr
```

### Generar el código de ANTLR

```bash
antlr4 -Dlanguage=Python3 -visitor LenguajeDL.g4
```

### Ejecutar la calculadora interactiva

```bash
python3 main.py
```

---

## Ejemplo de Código en LenguajeDL

Al ejecutar `main.py`, se presenta un menú interactivo. En el **Modo Libre (opción 9)** puedes escribir código directamente en LenguajeDL:

```lenguajedl
// Definición de variables
variable_1 = 100;
variable_2 = 50;

// Operaciones aritméticas extendidas
potencia = 2 ** 8;
residuo = 10 % 3;

// Operadores relacionales y lógicos
es_valido = (variable_1 > variable_2) and (residuo != 0);

// Probabilidades y pesos
probabilidades = [0.5, -0.2, 0.1];

print(potencia);      // Salida: > 256
print(residuo);       // Salida: > 1
print(es_valido);     // Salida: > True
print(probabilidades);
```
