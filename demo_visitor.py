from LenguajeDLVisitor import LenguajeDLVisitor
from LenguajeDLParser import LenguajeDLParser

class EvalVisitor(LenguajeDLVisitor):
    def __init__(self):
        self.memory = {}

    def visitProgram(self, ctx: LenguajeDLParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitAssignStmt(self, ctx: LenguajeDLParser.AssignStmtContext):
        var_name = ctx.assignment().ID().getText()
        value = self.visit(ctx.assignment().expr())
        self.memory[var_name] = value
        return value

    def visitPrintStmt(self, ctx: LenguajeDLParser.PrintStmtContext):
        value = self.visit(ctx.expr())
        print(f"> {value}")
        return None

    def visitExprStmt(self, ctx: LenguajeDLParser.ExprStmtContext):
        return self.visit(ctx.expr())

    # --- Operaciones aritméticas ---
    def visitPowExpr(self, ctx: LenguajeDLParser.PowExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right

    def visitMulDivModExpr(self, ctx: LenguajeDLParser.MulDivModExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            return left * right
        elif op == '/':
            if right == 0:
                raise Exception("Error: División por cero.")
            return left / right
        elif op == '%':
            return left % right

    def visitAddSubExpr(self, ctx: LenguajeDLParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        return left - right

    def visitUnaryMinusExpr(self, ctx: LenguajeDLParser.UnaryMinusExprContext):
        return -self.visit(ctx.expr())

    # --- Comparaciones ---
    def visitCompareExpr(self, ctx: LenguajeDLParser.CompareExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '<':   return left < right
        if op == '<=':  return left <= right
        if op == '>':   return left > right
        if op == '>=':  return left >= right
        if op == '==':  return left == right
        if op == '!=':  return left != right

    # --- Lógica booleana ---
    def visitLogicExpr(self, ctx: LenguajeDLParser.LogicExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == 'and':
            return left and right
        return left or right

    def visitNotExpr(self, ctx: LenguajeDLParser.NotExprContext):
        return not self.visit(ctx.expr())

    def visitTrueExpr(self, ctx: LenguajeDLParser.TrueExprContext):
        return True

    def visitFalseExpr(self, ctx: LenguajeDLParser.FalseExprContext):
        return False

    # --- Estructuras de datos ---
    def visitArrayExpr(self, ctx: LenguajeDLParser.ArrayExprContext):
        return [self.visit(expr) for expr in ctx.expr()]

    # --- Literales y variables ---
    def visitIntExpr(self, ctx: LenguajeDLParser.IntExprContext):
        return int(ctx.getText())

    def visitFloatExpr(self, ctx: LenguajeDLParser.FloatExprContext):
        return float(ctx.getText())

    def visitIdExpr(self, ctx: LenguajeDLParser.IdExprContext):
        var_name = ctx.getText()
        if var_name in self.memory:
            return self.memory[var_name]
        raise Exception(f"Error: Variable '{var_name}' no definida.")

    def visitParensExpr(self, ctx: LenguajeDLParser.ParensExprContext):
        return self.visit(ctx.expr())