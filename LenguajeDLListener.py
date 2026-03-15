# Generated from LenguajeDL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LenguajeDLParser import LenguajeDLParser
else:
    from LenguajeDLParser import LenguajeDLParser

# This class defines a complete listener for a parse tree produced by LenguajeDLParser.
class LenguajeDLListener(ParseTreeListener):

    # Enter a parse tree produced by LenguajeDLParser#program.
    def enterProgram(self, ctx:LenguajeDLParser.ProgramContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#program.
    def exitProgram(self, ctx:LenguajeDLParser.ProgramContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#assignStmt.
    def enterAssignStmt(self, ctx:LenguajeDLParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#assignStmt.
    def exitAssignStmt(self, ctx:LenguajeDLParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#exprStmt.
    def enterExprStmt(self, ctx:LenguajeDLParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#exprStmt.
    def exitExprStmt(self, ctx:LenguajeDLParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#mostrarStmt.
    def enterMostrarStmt(self, ctx:LenguajeDLParser.MostrarStmtContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#mostrarStmt.
    def exitMostrarStmt(self, ctx:LenguajeDLParser.MostrarStmtContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#assignment.
    def enterAssignment(self, ctx:LenguajeDLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#assignment.
    def exitAssignment(self, ctx:LenguajeDLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#BoolExpr.
    def enterBoolExpr(self, ctx:LenguajeDLParser.BoolExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#BoolExpr.
    def exitBoolExpr(self, ctx:LenguajeDLParser.BoolExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#StringExpr.
    def enterStringExpr(self, ctx:LenguajeDLParser.StringExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#StringExpr.
    def exitStringExpr(self, ctx:LenguajeDLParser.StringExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#PowerExpr.
    def enterPowerExpr(self, ctx:LenguajeDLParser.PowerExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#PowerExpr.
    def exitPowerExpr(self, ctx:LenguajeDLParser.PowerExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#ArrayExpr.
    def enterArrayExpr(self, ctx:LenguajeDLParser.ArrayExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#ArrayExpr.
    def exitArrayExpr(self, ctx:LenguajeDLParser.ArrayExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#FloatExpr.
    def enterFloatExpr(self, ctx:LenguajeDLParser.FloatExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#FloatExpr.
    def exitFloatExpr(self, ctx:LenguajeDLParser.FloatExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#IdExpr.
    def enterIdExpr(self, ctx:LenguajeDLParser.IdExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#IdExpr.
    def exitIdExpr(self, ctx:LenguajeDLParser.IdExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#MulDivModExpr.
    def enterMulDivModExpr(self, ctx:LenguajeDLParser.MulDivModExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#MulDivModExpr.
    def exitMulDivModExpr(self, ctx:LenguajeDLParser.MulDivModExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#ParensExpr.
    def enterParensExpr(self, ctx:LenguajeDLParser.ParensExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#ParensExpr.
    def exitParensExpr(self, ctx:LenguajeDLParser.ParensExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#IntExpr.
    def enterIntExpr(self, ctx:LenguajeDLParser.IntExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#IntExpr.
    def exitIntExpr(self, ctx:LenguajeDLParser.IntExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#RelationalExpr.
    def enterRelationalExpr(self, ctx:LenguajeDLParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#RelationalExpr.
    def exitRelationalExpr(self, ctx:LenguajeDLParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:LenguajeDLParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:LenguajeDLParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by LenguajeDLParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:LenguajeDLParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by LenguajeDLParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:LenguajeDLParser.UnaryMinusExprContext):
        pass



del LenguajeDLParser