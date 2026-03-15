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

    def visitMostrarStmt(self, ctx: LenguajeDLParser.MostrarStmtContext):
        value = self.visit(ctx.expr())
        print(f"> {value}")
        return None

    def visitExprStmt(self, ctx: LenguajeDLParser.ExprStmtContext):
        return self.visit(ctx.expr())

    def visitUnaryMinusExpr(self, ctx: LenguajeDLParser.UnaryMinusExprContext):
        return -self.visit(ctx.expr())

    def visitPowerExpr(self, ctx: LenguajeDLParser.PowerExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right

    def visitMulDivModExpr(self, ctx: LenguajeDLParser.MulDivModExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*': return left * right
        if op == '/': return left / right
        if op == '%': return left % right

    def visitAddSubExpr(self, ctx: LenguajeDLParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+': return left + right
        if ctx.op.text == '-': return left - right

    def visitRelationalExpr(self, ctx: LenguajeDLParser.RelationalExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '<':  return left < right
        if op == '<=': return left <= right
        if op == '>':  return left > right
        if op == '>=': return left >= right
        if op == '==': return left == right
        if op == '!=': return left != right

    def visitArrayExpr(self, ctx: LenguajeDLParser.ArrayExprContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitBoolExpr(self, ctx: LenguajeDLParser.BoolExprContext):
        return ctx.getText() == 'true'

    # --- NUEVO: Procesar Strings ---
    def visitStringExpr(self, ctx: LenguajeDLParser.StringExprContext):
        text = ctx.getText()
        return text[1:-1] # Retorna el texto sin las comillas dobles de los extremos

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
