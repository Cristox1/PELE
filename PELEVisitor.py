# Generated from PELE.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PELEParser import PELEParser
else:
    from PELEParser import PELEParser

# This class defines a complete generic visitor for a parse tree produced by PELEParser.

class PELEVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PELEParser#program.
    def visitProgram(self, ctx:PELEParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#block.
    def visitBlock(self, ctx:PELEParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#funcDeclStmt.
    def visitFuncDeclStmt(self, ctx:PELEParser.FuncDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#retStmt.
    def visitRetStmt(self, ctx:PELEParser.RetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#assignStmt.
    def visitAssignStmt(self, ctx:PELEParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#exprStmt.
    def visitExprStmt(self, ctx:PELEParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#mostrarStmt.
    def visitMostrarStmt(self, ctx:PELEParser.MostrarStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#ifStmt.
    def visitIfStmt(self, ctx:PELEParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#whileStmt.
    def visitWhileStmt(self, ctx:PELEParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#forStmt.
    def visitForStmt(self, ctx:PELEParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#functionDecl.
    def visitFunctionDecl(self, ctx:PELEParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#returnStatement.
    def visitReturnStatement(self, ctx:PELEParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#ifStatement.
    def visitIfStatement(self, ctx:PELEParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#whileStatement.
    def visitWhileStatement(self, ctx:PELEParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#forStatement.
    def visitForStatement(self, ctx:PELEParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#assignment.
    def visitAssignment(self, ctx:PELEParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#BoolExpr.
    def visitBoolExpr(self, ctx:PELEParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#StringExpr.
    def visitStringExpr(self, ctx:PELEParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#FloatExpr.
    def visitFloatExpr(self, ctx:PELEParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#IdExpr.
    def visitIdExpr(self, ctx:PELEParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#RelationalExpr.
    def visitRelationalExpr(self, ctx:PELEParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#PowerExpr.
    def visitPowerExpr(self, ctx:PELEParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#ArrayExpr.
    def visitArrayExpr(self, ctx:PELEParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#MulDivModExpr.
    def visitMulDivModExpr(self, ctx:PELEParser.MulDivModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#ParensExpr.
    def visitParensExpr(self, ctx:PELEParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#IntExpr.
    def visitIntExpr(self, ctx:PELEParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:PELEParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:PELEParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PELEParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:PELEParser.FuncCallExprContext):
        return self.visitChildren(ctx)



del PELEParser