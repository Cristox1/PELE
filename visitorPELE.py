from PELEVisitor import PELEVisitor
from PELEParser import PELEParser

class EvalVisitor(PELEVisitor):
    def __init__(self):
        self.memory = {}

    def visitProgram(self, ctx: PELEParser.ProgramContext):
        return self.visit(ctx.block()) 
    
    def visitBlock(self, ctx: PELEParser.BlockContext):
        for stmt in ctx.statement():
            try:
                self.visit(stmt)
            except Exception as e:
                print(f"Error en statement: {e}")
        return None

    def visitAssignStmt(self, ctx: PELEParser.AssignStmtContext):
        var_name = ctx.assignment().ID().getText()
        value = self.visit(ctx.assignment().expr())
        self.memory[var_name] = value
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
        op = ctx.op.text
        if op == '*': return left * right
        if op == '/': return left / right
        if op == '%': return left % right

    def visitAddSubExpr(self, ctx: PELEParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+': return left + right
        if ctx.op.text == '-': return left - right

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
        if var_name in self.memory:
            return self.memory[var_name]
        raise Exception(f"Error: Variable '{var_name}' no definida.")

    def visitParensExpr(self, ctx: PELEParser.ParensExprContext):
        return self.visit(ctx.expr())
    
    def visitIfStmt(self, ctx: PELEParser.IfStmtContext):
            condition = self.visit(ctx.ifStatement().expr())
            if condition:
                return self.visit(ctx.ifStatement().block(0))
            elif ctx.ifStatement().block(1):
                return self.visit(ctx.ifStatement().block(1))
            return None
    #
    #
    def visitFuncCallExpr(self, ctx: PELEParser.FuncCallExprContext):
        func_name = ctx.ID().getText()
        # obtener args: ctx.expr() devuelve lista de subctx
        args = []
        if ctx.expr():
            args = [self.visit(e) for e in ctx.expr()]
        # dispatch a funciones internas
        if func_name in self.builtins():
            return self.builtins()[func_name](*args)
        else:
            raise Exception(f"Error: Funcion builtin '{func_name}' no definida.")

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