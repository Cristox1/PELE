from PELEVisitor import PELEVisitor
from PELEParser import PELEParser

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class EvalVisitor(PELEVisitor):
    def __init__(self):
        # self.memory = {}  <-- ELIMINAR LA MEMORIA GLOBAL VIEJA
        self.call_stack = [{}] # Pila de scopes. El indice 0 es el scope global.
        self.user_functions = {} # Diccionario para guardar los AST de las funciones

    def _set_var(self, name, value):
        self.call_stack[-1][name] = value

    def _get_var(self, name):
        for scope in reversed(self.call_stack):
            if name in scope:
                return scope[name]
        raise Exception(f"Error: Variable '{name}' no definida en este ambito.")

    def visitProgram(self, ctx: PELEParser.ProgramContext):
        return self.visit(ctx.block()) 
    
    def visitBlock(self, ctx: PELEParser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitAssignStmt(self, ctx: PELEParser.AssignStmtContext):
        # Este maneja: a = 5;
        return self.visit(ctx.assignment())

    def visitAssignment(self, ctx: PELEParser.AssignmentContext):
        # Este maneja la logica real de asignacion (usado por AssignStmt y por ForStmt)
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self._set_var(var_name, value)
        return value

    def visitMostrarStmt(self, ctx: PELEParser.MostrarStmtContext):
        value = self.visit(ctx.expr())
        print(f"> {value}")
        return None

    def visitExprStmt(self, ctx: PELEParser.ExprStmtContext):
        return self.visit(ctx.expr())

    def visitUnaryMinusExpr(self, ctx: PELEParser.UnaryMinusExprContext):
        return -self.visit(ctx.expr())

    def visitPowerExpr(self, ctx: PELEParser.PowerExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right

    def visitMulDivModExpr(self, ctx: PELEParser.MulDivModExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # CORRECCION: Obtenemos el operador accediendo al hijo 1 del nodo AST
        op = ctx.getChild(1).getText() 
        if op == '*': return left * right
        if op == '/': return left / right
        if op == '%': return left % right

    def visitAddSubExpr(self, ctx: PELEParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # CORRECCION: Obtenemos el operador accediendo al hijo 1 del nodo AST
        op = ctx.getChild(1).getText() 
        if op == '+': return left + right
        if op == '-': return left - right

    def visitRelationalExpr(self, ctx: PELEParser.RelationalExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '<':  return left < right
        if op == '<=': return left <= right
        if op == '>':  return left > right
        if op == '>=': return left >= right
        if op == '==': return left == right
        if op == '!=': return left != right

    def visitArrayExpr(self, ctx: PELEParser.ArrayExprContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitBoolExpr(self, ctx: PELEParser.BoolExprContext):
        return ctx.getText() == 'true'

    def visitStringExpr(self, ctx: PELEParser.StringExprContext):
        text = ctx.getText()
        return text[1:-1] 

    def visitIntExpr(self, ctx: PELEParser.IntExprContext):
        return int(ctx.getText())

    def visitFloatExpr(self, ctx: PELEParser.FloatExprContext):
        return float(ctx.getText())

    def visitIdExpr(self, ctx: PELEParser.IdExprContext):
        var_name = ctx.getText()
        return self._get_var(var_name)

    def visitParensExpr(self, ctx: PELEParser.ParensExprContext):
        return self.visit(ctx.expr())
    
    # Reemplaza tu visitIfStmt anterior con este:
    def visitIfStmt(self, ctx: PELEParser.IfStmtContext):
        if_ctx = ctx.ifStatement()
        exprs = if_ctx.expr()   # Lista de todas las condiciones (si y sino)
        blocks = if_ctx.block() # Lista de todos los bloques de codigo

        # Evaluar la primera condicion (el 'si')
        if self.visit(exprs[0]):
            return self.visit(blocks[0])

        # Iterar sobre las condiciones 'sino' (elifs)
        # Empiezan en el indice 1 hasta el final de las expresiones
        for i in range(1, len(exprs)):
            if self.visit(exprs[i]):
                return self.visit(blocks[i])

        # Si ninguna condicion fue verdadera, verificamos si existe el 'entonces' (else)
        # Sabemos que existe un 'entonces' si hay mas bloques que expresiones
        if len(blocks) > len(exprs):
            return self.visit(blocks[-1])

        return None

    # Agrega la logica para el ciclo 'mientras'
    def visitWhileStmt(self, ctx: PELEParser.WhileStmtContext):
        while_ctx = ctx.whileStatement()
        # En la teoria de compiladores, un interprete tree-walk evalua 
        # el AST dinamicamente apoyandose en el bucle del lenguaje anfitrion.
        while self.visit(while_ctx.expr()):
            self.visit(while_ctx.block())
        return None

    # Agrega la logica para el ciclo 'por'
    def visitForStmt(self, ctx: PELEParser.ForStmtContext):
        for_ctx = ctx.forStatement()
        
        # 1. Inicializacion: ejecutamos la primera asignacion
        self.visit(for_ctx.assignment(0))
        
        # 2. Condicion: comprobamos la expresion logica
        while self.visit(for_ctx.expr()):
            # 3. Cuerpo: ejecutamos el bloque de codigo principal
            self.visit(for_ctx.block())
            
            # 4. Actualizacion: ejecutamos la segunda asignacion (el paso)
            self.visit(for_ctx.assignment(1))
            
        return None    
    #
    def visitFuncCallExpr(self, ctx: PELEParser.FuncCallExprContext):
        func_name = ctx.ID().getText()
        args = []
        if ctx.expr():
            args = [self.visit(e) for e in ctx.expr()]

        # 1. Chequear funciones nativas (built-ins)
        if func_name in self.builtins():
            return self.builtins()[func_name](*args)

        # 2. Chequear funciones de usuario
        if func_name in self.user_functions:
            func_ctx = self.user_functions[func_name]
            
            # Extraer nombres de parametros del AST (ignorando el ID[0] que es el nombre)
            param_names = [param.getText() for param in func_ctx.ID()[1:]]
            
            if len(param_names) != len(args):
                raise Exception(f"Error: La funcion '{func_name}' espera {len(param_names)} argumentos, recibio {len(args)}.")
            
            # Crear un nuevo entorno local (Scope)
            local_scope = {}
            for i in range(len(param_names)):
                local_scope[param_names[i]] = args[i]
            
            # Entrar a la funcion (Push a la pila)
            self.call_stack.append(local_scope)
            
            return_value = None
            try:
                self.visit(func_ctx.block())
            except ReturnValue as ret:
                return_value = ret.value
            finally:
                # Salir de la funcion (Pop a la pila, destruye las variables locales)
                self.call_stack.pop()
                
            return return_value

        raise Exception(f"Error: Funcion '{func_name}' no definida.")

    def builtins(self):
        # devuelve un diccionario { 'nombre': function_pointer }
        return {
            # Mapas
            "crear_mapa": self._crear_mapa,
            "mapa_put": self._mapa_put,
            "mapa_get": self._mapa_get,
            "mapa_keys": self._mapa_keys,
            "mapa_values": self._mapa_values,
            # Pilas y colas
            "crear_pila": self._crear_pila,
            "pila_push": self._pila_push,
            "pila_pop": self._pila_pop,
            "crear_cola": self._crear_cola,
            "cola_enqueue": self._cola_enqueue,
            "cola_dequeue": self._cola_dequeue,
            # Conjuntos
            "crear_conjunto": self._crear_conjunto,
            "conjunto_add": self._conjunto_add,
            "conjunto_contains": self._conjunto_contains,
            # Matrices
            "crear_matriz": self._crear_matriz,
            "mat_get": self._mat_get,
            "mat_set": self._mat_set,
            # Arboles
            "crear_arbol": self._crear_arbol,
            "arbol_add_child": self._arbol_add_child,
            "arbol_preorder": self._arbol_preorder,
            # Grafos
            "crear_grafo": self._crear_grafo,
            "grafo_add_node": self._grafo_add_node,
            "grafo_add_edge": self._grafo_add_edge,
            "grafo_neighbors": self._grafo_neighbors,
            "grafo_bfs": self._grafo_bfs,
            # Helpers para arreglos (opcional)
            "arr_get": self._arr_get,
            "arr_set": self._arr_set,
        }

    # --- Implementaciones de builtins ---
    # Mapas
    def _format_value(self, v):
        # Formatea recursivamente para listas, dicts, sets, árboles y grafos
        if isinstance(v, dict):
            # Posible grafo o mapa o nodo de árbol
            # Distinguimos árbol por keys 'value' y 'children'
            if 'value' in v and 'children' in v:
                # árbol: mostramos preorder de valores
                return f"Arbol({self._format_value(v['value'])}, children={len(v['children'])})"
            else:
                # mapa/grafo: representarlo como dict normal
                items = ", ".join(f"{repr(k)}: {self._format_value(val)}" for k, val in v.items())
                return "{" + items + "}"
        if isinstance(v, list):
            inner = ", ".join(self._format_value(x) for x in v)
            return "[" + inner + "]"
        if isinstance(v, set):
            inner = ", ".join(self._format_value(x) for x in sorted(v, key=repr))
            return "{" + inner + "}"
        # tipos atómicos
        return repr(v)

    def visitMostrarStmt(self, ctx: PELEParser.MostrarStmtContext):
        value = self.visit(ctx.expr())
        print("> " + self._format_value(value))
        return None
    
    def _crear_mapa(self, pairs):
        # pairs esperado: array de pares [ [k,v], [k2,v2], ... ]
        m = {}
        if pairs is None:
            return m
        for pair in pairs:
            if isinstance(pair, list) and len(pair) == 2:
                m[pair[0]] = pair[1]
            else:
                raise Exception("crear_mapa espera un arreglo de pares [clave,valor]")
        return m

    def _mapa_put(self, m, k, v):
        m[k] = v
        return m

    def _mapa_get(self, m, k):
        return m.get(k, None)

    def _mapa_keys(self, m):
        return list(m.keys())

    def _mapa_values(self, m):
        return list(m.values())

    # Pilas
    def _crear_pila(self):
        return []

    def _pila_push(self, stack, value):
        stack.append(value)
        return None

    def _pila_pop(self, stack):
        if not stack:
            raise Exception("Error: pila vacia")
        return stack.pop()

    # Colas
    def _crear_cola(self):
        return []

    def _cola_enqueue(self, queue, value):
        queue.append(value)
        return None

    def _cola_dequeue(self, queue):
        if not queue:
            raise Exception("Error: cola vacia")
        return queue.pop(0)

    # Conjuntos
    def _crear_conjunto(self, arr):
        # arr opcional: lista para inicializar
        if arr is None:
            return set()
        return set(arr)

    def _conjunto_add(self, s, v):
        s.add(v)
        return None

    def _conjunto_contains(self, s, v):
        return v in s

    # Matrices
    def _crear_matriz(self, rows, cols, fill):
        rows_i = int(rows); cols_i = int(cols)
        return [[fill for _ in range(cols_i)] for _ in range(rows_i)]

    def _mat_get(self, mat, i, j):
        return mat[int(i)][int(j)]

    def _mat_set(self, mat, i, j, val):
        mat[int(i)][int(j)] = val
        return None

    # Arboles (nodo simple: dict {'value':..., 'children':[...]})
    def _crear_arbol(self, value):
        return {'value': value, 'children': []}

    def _arbol_add_child(self, node, child):
        node['children'].append(child)
        return child

    def _arbol_preorder(self, node):
        res = []
        def _rec(n):
            res.append(n['value'])
            for c in n['children']:
                _rec(c)
        _rec(node)
        return res

    # Grafos (dict de adyacencia)
    def _crear_grafo(self):
        return {}

    def _grafo_add_node(self, g, node):
        if node not in g:
            g[node] = []
        return None

    def _grafo_add_edge(self, g, u, v):
        if u not in g: g[u] = []
        if v not in g: g[v] = []
        g[u].append(v)
        # si grafo no dirigido: g[v].append(u)
        return None

    def _grafo_neighbors(self, g, node):
        return g.get(node, [])

    def _grafo_bfs(self, g, start):
        visited = set()
        queue = []
        order = []
        queue.append(start); visited.add(start)
        while queue:
            u = queue.pop(0)
            order.append(u)
            for v in g.get(u, []):
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        return order

    # Helpers para arrays
    def _arr_get(self, arr, idx):
        return arr[int(idx)]

    def _arr_set(self, arr, idx, val):
        arr[int(idx)] = val
        return None
    

    def visitFuncDeclStmt(self, ctx: PELEParser.FuncDeclStmtContext):
        # ID(0) es el nombre de la funcion. Los demas ID(1...) son los parametros.
        func_name = ctx.functionDecl().ID(0).getText()
        # Guardamos el nodo AST completo para ejecutarlo cuando llamen a la funcion
        self.user_functions[func_name] = ctx.functionDecl()
        return None

    def visitRetStmt(self, ctx: PELEParser.RetStmtContext):
        value = self.visit(ctx.returnStatement().expr())
        # Lanzamos la excepcion para romper el flujo y subir el valor
        raise ReturnValue(value)