# Generated from LenguajeDL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LenguajeDLParser import LenguajeDLParser
else:
    from LenguajeDLParser import LenguajeDLParser

# This class defines a complete generic visitor for a parse tree produced by LenguajeDLParser.

class LenguajeDLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LenguajeDLParser#program.
    def visitProgram(self, ctx:LenguajeDLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#assignStmt.
    def visitAssignStmt(self, ctx:LenguajeDLParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#exprStmt.
    def visitExprStmt(self, ctx:LenguajeDLParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#printStmt.
    def visitPrintStmt(self, ctx:LenguajeDLParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#assignment.
    def visitAssignment(self, ctx:LenguajeDLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#ArrayExpr.
    def visitArrayExpr(self, ctx:LenguajeDLParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#FloatExpr.
    def visitFloatExpr(self, ctx:LenguajeDLParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:LenguajeDLParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#IdExpr.
    def visitIdExpr(self, ctx:LenguajeDLParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#ParensExpr.
    def visitParensExpr(self, ctx:LenguajeDLParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#IntExpr.
    def visitIntExpr(self, ctx:LenguajeDLParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:LenguajeDLParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDLParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:LenguajeDLParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)



del LenguajeDLParser