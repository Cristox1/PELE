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

#### Resumen
PELE es un lenguaje educativo/intermedio con:
- Gramática en `PELE.g4` (ANTLR4).
- Evaluador/ejecutor en `visitorPELE.py` (patrón Visitor).
- Ejecutable de entrada en `pele.py`.
- Archivo fuente de ejemplo: `programa.txt`.

### Características Actuales

#### Tipos de datos
- INT (enteros), FLOAT (decimales), BOOLEAN (`true` / `false`), STRING (cadenas entre comillas).
- Arreglos literales: `[1, 2, 3]` (listas 1D).

### Ciclos (iteración)

#### Soporte actual
PELE soporta dos estilos de bucles:

- Bucle while con palabra clave `mientras`:
  - Sintaxis: `mientras (condicion) { ... }`
  - El cuerpo se ejecuta mientras la condición booleana sea verdadera.
  - Ejemplo:
    ```text
    contador = 0;
    mientras (contador < 5) {
        mostrar(contador);
        contador = contador + 1;
    }
    ```

- Bucle for estilo C con palabra clave `por`:
  - Sintaxis: `por (inicializacion; condicion; incremento) { ... }`
  - Implementado como: ejecutar la asignación inicial, evaluar condición, ejecutar cuerpo, ejecutar incremento, repetir.
  - Atención: el visitor ejecuta manualmente las asignaciones inicial e incremento para actualizar correctamente las variables del scope.
  - Ejemplo:
    ```text
    por (i = 0; i < 5; i = i + 1) {
        mostrar(i);
    }
    ```

- Bucle for-each (iteración sobre arreglos) con `for (id in arr)`:
  - Sintaxis: `for (x in nums) { ... }`
  - Requiere que `nums` sea un arreglo (lista).
  - Ejemplo:
    ```text
    nums = [0,1,2,3,4];
    for (x in nums) {
        mostrar(x);
    }
    ```

#### Comportamiento de errores en ciclos
- Si ocurre una excepción dentro del cuerpo de un ciclo, existe manejo centralizado en `visitBlock` que imprime el error con la línea y, por defecto, continúa la ejecución (no detiene todo el programa).  
- Puedes forzar que el intérprete se detenga en el primer error activando `visitor.stop_on_error = True` (el wrapper `run_code` acepta este parámetro).

### Estructuras de datos (implementadas como builtins)

PELE expone un conjunto de funciones nativas (builtins) que implementan las estructuras solicitadas sin dependencias externas. Se usan desde el código PELE mediante llamadas de función, p. ej. `crear_pila()`, `mapa_get(m, "k")`.

#### Arreglos (listas 1D)
- Literal: `[1, 2, 3]`
- Helpers: `arr_get(arr, idx)`, `arr_set(arr, idx, val)`.

#### Mapas (diccionarios)
- Crear desde pares: `crear_mapa([["k1", v1], ["k2", v2]])`
- Operaciones: `mapa_get(m, k)`, `mapa_put(m, k, v)`, `mapa_keys(m)`, `mapa_values(m)`.

#### Pilas
- `crear_pila()` → devuelve una lista usada como pila.
- `pila_push(stack, value)`, `pila_pop(stack)`.

#### Colas
- `crear_cola()` → lista usada como cola FIFO.
- `cola_enqueue(queue, value)`, `cola_dequeue(queue)`.

#### Conjuntos
- `crear_conjunto(arr)` → crea un `set` desde un arreglo.
- `conjunto_add(s, v)`, `conjunto_contains(s, v)`.

#### Matrices
- `crear_matriz(rows, cols, fill)` → crea matriz (lista de listas).
- `mat_get(mat, i, j)`, `mat_set(mat, i, j, val)`.

#### Árboles (nodo simple)
- Nodo representado como `{'value': ..., 'children': [...]}` en el visitor.
- `crear_arbol(valor)`, `arbol_add_child(node, child)`, `arbol_preorder(node)`.

#### Grafos (lista de adyacencia)
- `crear_grafo()` → diccionario de adyacencia.
- `grafo_add_node(g, node)`, `grafo_add_edge(g, u, v)`, `grafo_neighbors(g, node)`, `grafo_bfs(g, start)`.

#### Notas sobre estructuras
- Todas las estructuras son implementadas en `visitorPELE.py` como funciones Python (builtins) y devuelven/aceptan estructuras Python nativas (listas, dicts, sets).
- La salida de `mostrar(...)` formatea estas estructuras para una visualización legible (función `_format_value`).
- Validaciones mínimas de tipo están implementadas; si se pasa un tipo incorrecto, se lanza una excepción capturada por `visitBlock`.

### Funciones y Recursividad

#### Soporte actual
- Declaración de funciones: `funcion nombre(params...) { block }`
- Retorno: `retornar expr;`
- Llamada: `resultado = nombre(arg1, arg2);`
- Recursividad: soportada plenamente (pila de scopes + excepción interna `ReturnValue` para implementar la salida de `retornar`).

#### Implementación interna
- Las funciones definidas por el usuario se almacenan en `self.functions` (nombre → {params, block_ctx}).
- Al llamar una función:
  - Se crea un nuevo scope (push).
  - Se asignan los parámetros en el scope local.
  - Se ejecuta su `block` y se captura `ReturnValue` para obtener el valor de retorno.
  - Se restablece el scope (pop).
- Si la función termina sin `retornar`, devuelve `None`.

#### Ejemplo (factorial recursivo)
```text
funcion factorial(n) {
    si (n <= 1) {
        retornar 1;
    }
    retornar n * factorial(n - 1);
}

mostrar(factorial(5)); // imprime 120
```

#### Scopes y variables locales
- El intérprete mantiene una pila de scopes (listas de diccionarios). Las variables definidas dentro de una función no contaminan el scope global.
- Acceso a variables sigue la búsqueda desde el scope actual hacia afuera (shadowing permitido).

### Condicionales (control de flujo condicional)

#### Soporte actual
- `si (cond) { ... } (sino { ... })?` — rama simple con opcional `sino`.
- En la gramática también se admiten variantes con `sino` que contienen otro `block`.
- Condiciones evaluadas son expresiones booleanas (resultado de comparaciones o valores booleanos).
- Ejemplo:
```text
si (x < 0) {
    mostrar("negativo");
} sino {
    mostrar("no negativo");
}
```

#### Evaluación y errores
- Si la condición no evalúa a booleano (ej. un número), el visitor puede lanzar un `TypeError` en contextos concretos (por ejemplo en `while` se valida que la condición sea booleana).
- Errores en bloques condicionales son capturados por `visitBlock` y reportados con la línea; ejecución continúa a menos que `stop_on_error` sea True.

### Manejo de errores global (try/except en el visitor)
- `visitBlock` contiene un `try/except` que:
  - Captura excepciones lanzadas al ejecutar cada `statement`.
  - Intenta extraer `line` desde el token `start` del `stmt` para reportar la línea.
  - Imprime: `[Linea X] Error en statement: <mensaje>`.
  - Si `self.stop_on_error` es True, relanza la excepción (detiene ejecución).
  - `ReturnValue` (la excepción usada para `retornar`) se re-lanza para permitir que `retornar` salga correctamente de funciones.
- Esto permite que el script de pruebas (programa.txt) muestre varios errores en una sola ejecución sin detenerse inmediatamente.

### Ejecución y pruebas

#### Generar artefactos ANTLR
```bash
antlr4 -Dlanguage=Python3 -visitor PELE.g4
```
(o usar el jar de ANTLR si no tienes el wrapper).

#### Ejecutar intérprete
- Coloca tu código en `programa.txt` y ejecuta:
```bash
python3 pele.py
```
- Para tests desde Python y detener en primer error:
```python
from pele import run_code
run_code(open("programa.txt").read(), stop_on_error=True)
```

### Ejemplos de uso (resumen)

- Ciclos:
```text
por (i = 0; i < 5; i = i + 1) { mostrar(i); }
mientras (cond) { ... }
for (x in arr) { ... }
```

- Condicionales:
```text
si (cond) { ... } sino { ... }
```

- Funciones:
```text
funcion suma(a,b) {
    retornar a + b;
}
mostrar(suma(2,3));
```

- Estructuras (ejemplos):
```text
p = crear_pila(); pila_push(p, 1); mostrar(pila_pop(p));
m = crear_mapa([["k", 1]]); mostrar(mapa_get(m, "k"));
mat = crear_matriz(2,2,0); mat_set(mat,0,1,42); mostrar(mat);
```