# Cambiamos las importaciones a los nuevos archivos generados
from LenguajeDLVisitor import LenguajeDLVisitor
from LenguajeDLParser import LenguajeDLParser

# Heredamos del nuevo Visitor generado
class EvalVisitor(LenguajeDLVisitor):
    def __init__(self):
        self.memory = {}

    # Actualizamos todas las referencias a LenguajeDLParser
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

    def visitMulDivExpr(self, ctx: LenguajeDLParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LenguajeDLParser.MUL:
            return left * right
        return left / right

    def visitAddSubExpr(self, ctx: LenguajeDLParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LenguajeDLParser.ADD:
            return left + right
        return left - right

    def visitArrayExpr(self, ctx: LenguajeDLParser.ArrayExprContext):
        return [self.visit(expr) for expr in ctx.expr()]

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