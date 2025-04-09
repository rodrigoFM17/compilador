# Generated from MiLenguaje.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiLenguajeParser import MiLenguajeParser
else:
    from MiLenguajeParser import MiLenguajeParser

# This class defines a complete listener for a parse tree produced by MiLenguajeParser.
class MiLenguajeListener(ParseTreeListener):

    # Enter a parse tree produced by MiLenguajeParser#programa.
    def enterPrograma(self, ctx:MiLenguajeParser.ProgramaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#programa.
    def exitPrograma(self, ctx:MiLenguajeParser.ProgramaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#sentencia.
    def enterSentencia(self, ctx:MiLenguajeParser.SentenciaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#sentencia.
    def exitSentencia(self, ctx:MiLenguajeParser.SentenciaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#declaracion.
    def enterDeclaracion(self, ctx:MiLenguajeParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#declaracion.
    def exitDeclaracion(self, ctx:MiLenguajeParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#asignacion.
    def enterAsignacion(self, ctx:MiLenguajeParser.AsignacionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#asignacion.
    def exitAsignacion(self, ctx:MiLenguajeParser.AsignacionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#expresion.
    def enterExpresion(self, ctx:MiLenguajeParser.ExpresionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#expresion.
    def exitExpresion(self, ctx:MiLenguajeParser.ExpresionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#termino.
    def enterTermino(self, ctx:MiLenguajeParser.TerminoContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#termino.
    def exitTermino(self, ctx:MiLenguajeParser.TerminoContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#funcionConRetorno.
    def enterFuncionConRetorno(self, ctx:MiLenguajeParser.FuncionConRetornoContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#funcionConRetorno.
    def exitFuncionConRetorno(self, ctx:MiLenguajeParser.FuncionConRetornoContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#funcionSinRetorno.
    def enterFuncionSinRetorno(self, ctx:MiLenguajeParser.FuncionSinRetornoContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#funcionSinRetorno.
    def exitFuncionSinRetorno(self, ctx:MiLenguajeParser.FuncionSinRetornoContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#parametros.
    def enterParametros(self, ctx:MiLenguajeParser.ParametrosContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#parametros.
    def exitParametros(self, ctx:MiLenguajeParser.ParametrosContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:MiLenguajeParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:MiLenguajeParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#estructuraDeControl.
    def enterEstructuraDeControl(self, ctx:MiLenguajeParser.EstructuraDeControlContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#estructuraDeControl.
    def exitEstructuraDeControl(self, ctx:MiLenguajeParser.EstructuraDeControlContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#estructuraIf.
    def enterEstructuraIf(self, ctx:MiLenguajeParser.EstructuraIfContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#estructuraIf.
    def exitEstructuraIf(self, ctx:MiLenguajeParser.EstructuraIfContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#expresionLogica.
    def enterExpresionLogica(self, ctx:MiLenguajeParser.ExpresionLogicaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#expresionLogica.
    def exitExpresionLogica(self, ctx:MiLenguajeParser.ExpresionLogicaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#cicloFor.
    def enterCicloFor(self, ctx:MiLenguajeParser.CicloForContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#cicloFor.
    def exitCicloFor(self, ctx:MiLenguajeParser.CicloForContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#asignacionFor.
    def enterAsignacionFor(self, ctx:MiLenguajeParser.AsignacionForContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#asignacionFor.
    def exitAsignacionFor(self, ctx:MiLenguajeParser.AsignacionForContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#cicloWhile.
    def enterCicloWhile(self, ctx:MiLenguajeParser.CicloWhileContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#cicloWhile.
    def exitCicloWhile(self, ctx:MiLenguajeParser.CicloWhileContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#tipo.
    def enterTipo(self, ctx:MiLenguajeParser.TipoContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#tipo.
    def exitTipo(self, ctx:MiLenguajeParser.TipoContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#kwClg.
    def enterKwClg(self, ctx:MiLenguajeParser.KwClgContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#kwClg.
    def exitKwClg(self, ctx:MiLenguajeParser.KwClgContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#retornoSentencia.
    def enterRetornoSentencia(self, ctx:MiLenguajeParser.RetornoSentenciaContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#retornoSentencia.
    def exitRetornoSentencia(self, ctx:MiLenguajeParser.RetornoSentenciaContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#kwScn.
    def enterKwScn(self, ctx:MiLenguajeParser.KwScnContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#kwScn.
    def exitKwScn(self, ctx:MiLenguajeParser.KwScnContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#operadoresAritmeticos.
    def enterOperadoresAritmeticos(self, ctx:MiLenguajeParser.OperadoresAritmeticosContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#operadoresAritmeticos.
    def exitOperadoresAritmeticos(self, ctx:MiLenguajeParser.OperadoresAritmeticosContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#operadoresComparacion.
    def enterOperadoresComparacion(self, ctx:MiLenguajeParser.OperadoresComparacionContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#operadoresComparacion.
    def exitOperadoresComparacion(self, ctx:MiLenguajeParser.OperadoresComparacionContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#kwUnmutable.
    def enterKwUnmutable(self, ctx:MiLenguajeParser.KwUnmutableContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#kwUnmutable.
    def exitKwUnmutable(self, ctx:MiLenguajeParser.KwUnmutableContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#kwEnt.
    def enterKwEnt(self, ctx:MiLenguajeParser.KwEntContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#kwEnt.
    def exitKwEnt(self, ctx:MiLenguajeParser.KwEntContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#kwFlt.
    def enterKwFlt(self, ctx:MiLenguajeParser.KwFltContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#kwFlt.
    def exitKwFlt(self, ctx:MiLenguajeParser.KwFltContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#kwLg.
    def enterKwLg(self, ctx:MiLenguajeParser.KwLgContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#kwLg.
    def exitKwLg(self, ctx:MiLenguajeParser.KwLgContext):
        pass


    # Enter a parse tree produced by MiLenguajeParser#kwStr.
    def enterKwStr(self, ctx:MiLenguajeParser.KwStrContext):
        pass

    # Exit a parse tree produced by MiLenguajeParser#kwStr.
    def exitKwStr(self, ctx:MiLenguajeParser.KwStrContext):
        pass



del MiLenguajeParser