from PELEVisitor import PELEVisitor
from PELEParser import PELEParser

class EvalVisitor(PELEVisitor):
    def __init__(self):
        self.memory = {}

    def visitProgram(self, ctx: PELEParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
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
        op = ctx.op.text
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
