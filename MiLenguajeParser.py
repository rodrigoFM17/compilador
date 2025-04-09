# Generated from MiLenguaje.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,290,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,
        68,8,1,1,1,1,1,3,1,72,8,1,1,1,1,1,1,1,1,1,1,1,3,1,79,8,1,1,2,3,2,
        82,8,2,1,2,1,2,1,2,1,2,1,2,3,2,89,8,2,3,2,91,8,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,104,8,4,10,4,12,4,107,9,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,117,8,5,1,6,1,6,1,6,1,6,3,6,123,8,
        6,1,6,1,6,1,6,1,6,1,6,5,6,130,8,6,10,6,12,6,133,9,6,1,6,1,6,1,7,
        1,7,1,7,1,7,3,7,141,8,7,1,7,1,7,1,7,5,7,146,8,7,10,7,12,7,149,9,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,159,8,8,10,8,12,8,162,9,8,
        1,9,1,9,1,9,1,9,1,9,5,9,169,8,9,10,9,12,9,172,9,9,3,9,174,8,9,1,
        9,1,9,1,10,1,10,1,10,3,10,181,8,10,1,11,1,11,1,11,1,11,1,11,1,11,
        5,11,189,8,11,10,11,12,11,192,9,11,1,11,1,11,1,11,1,11,5,11,198,
        8,11,10,11,12,11,201,9,11,1,11,3,11,204,8,11,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,3,13,215,8,13,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,223,8,13,10,13,12,13,226,9,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,240,8,15,10,15,12,15,243,
        9,15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,251,8,16,1,17,1,17,1,17,
        1,17,1,17,1,17,5,17,259,8,17,10,17,12,17,262,9,17,1,17,3,17,265,
        8,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,21,
        1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,0,0,
        27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,0,3,1,0,18,22,1,0,23,28,1,0,29,30,302,0,57,1,0,0,
        0,2,78,1,0,0,0,4,81,1,0,0,0,6,94,1,0,0,0,8,99,1,0,0,0,10,116,1,0,
        0,0,12,118,1,0,0,0,14,136,1,0,0,0,16,152,1,0,0,0,18,163,1,0,0,0,
        20,180,1,0,0,0,22,182,1,0,0,0,24,205,1,0,0,0,26,209,1,0,0,0,28,229,
        1,0,0,0,30,233,1,0,0,0,32,250,1,0,0,0,34,252,1,0,0,0,36,268,1,0,
        0,0,38,271,1,0,0,0,40,275,1,0,0,0,42,277,1,0,0,0,44,279,1,0,0,0,
        46,281,1,0,0,0,48,283,1,0,0,0,50,285,1,0,0,0,52,287,1,0,0,0,54,56,
        3,2,1,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,
        58,60,1,0,0,0,59,57,1,0,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,79,3,4,
        2,0,63,79,3,6,3,0,64,79,3,20,10,0,65,67,3,18,9,0,66,68,5,1,0,0,67,
        66,1,0,0,0,67,68,1,0,0,0,68,79,1,0,0,0,69,71,3,34,17,0,70,72,5,1,
        0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,79,1,0,0,0,73,79,3,12,6,0,74,
        79,3,14,7,0,75,76,3,36,18,0,76,77,5,1,0,0,77,79,1,0,0,0,78,62,1,
        0,0,0,78,63,1,0,0,0,78,64,1,0,0,0,78,65,1,0,0,0,78,69,1,0,0,0,78,
        73,1,0,0,0,78,74,1,0,0,0,78,75,1,0,0,0,79,3,1,0,0,0,80,82,3,44,22,
        0,81,80,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,3,32,16,0,84,90,
        5,35,0,0,85,88,5,2,0,0,86,89,3,8,4,0,87,89,3,38,19,0,88,86,1,0,0,
        0,88,87,1,0,0,0,89,91,1,0,0,0,90,85,1,0,0,0,90,91,1,0,0,0,91,92,
        1,0,0,0,92,93,5,1,0,0,93,5,1,0,0,0,94,95,5,35,0,0,95,96,5,2,0,0,
        96,97,3,8,4,0,97,98,5,1,0,0,98,7,1,0,0,0,99,105,3,10,5,0,100,101,
        3,40,20,0,101,102,3,10,5,0,102,104,1,0,0,0,103,100,1,0,0,0,104,107,
        1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,9,1,0,0,0,107,105,1,
        0,0,0,108,117,3,18,9,0,109,110,5,3,0,0,110,111,3,8,4,0,111,112,5,
        4,0,0,112,117,1,0,0,0,113,117,5,35,0,0,114,117,5,36,0,0,115,117,
        5,37,0,0,116,108,1,0,0,0,116,109,1,0,0,0,116,113,1,0,0,0,116,114,
        1,0,0,0,116,115,1,0,0,0,117,11,1,0,0,0,118,119,5,5,0,0,119,120,5,
        35,0,0,120,122,5,3,0,0,121,123,3,16,8,0,122,121,1,0,0,0,122,123,
        1,0,0,0,123,124,1,0,0,0,124,125,5,4,0,0,125,126,5,6,0,0,126,127,
        3,32,16,0,127,131,5,7,0,0,128,130,3,2,1,0,129,128,1,0,0,0,130,133,
        1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,
        1,0,0,0,134,135,5,8,0,0,135,13,1,0,0,0,136,137,5,5,0,0,137,138,5,
        35,0,0,138,140,5,3,0,0,139,141,3,16,8,0,140,139,1,0,0,0,140,141,
        1,0,0,0,141,142,1,0,0,0,142,143,5,4,0,0,143,147,5,7,0,0,144,146,
        3,2,1,0,145,144,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,
        1,0,0,0,148,150,1,0,0,0,149,147,1,0,0,0,150,151,5,8,0,0,151,15,1,
        0,0,0,152,153,3,32,16,0,153,160,5,35,0,0,154,155,5,9,0,0,155,156,
        3,32,16,0,156,157,5,35,0,0,157,159,1,0,0,0,158,154,1,0,0,0,159,162,
        1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,17,1,0,0,0,162,160,1,
        0,0,0,163,164,5,35,0,0,164,173,5,3,0,0,165,170,3,8,4,0,166,167,5,
        9,0,0,167,169,3,8,4,0,168,166,1,0,0,0,169,172,1,0,0,0,170,168,1,
        0,0,0,170,171,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,173,165,1,
        0,0,0,173,174,1,0,0,0,174,175,1,0,0,0,175,176,5,4,0,0,176,19,1,0,
        0,0,177,181,3,22,11,0,178,181,3,26,13,0,179,181,3,30,15,0,180,177,
        1,0,0,0,180,178,1,0,0,0,180,179,1,0,0,0,181,21,1,0,0,0,182,183,5,
        10,0,0,183,184,5,3,0,0,184,185,3,24,12,0,185,186,5,4,0,0,186,190,
        5,7,0,0,187,189,3,2,1,0,188,187,1,0,0,0,189,192,1,0,0,0,190,188,
        1,0,0,0,190,191,1,0,0,0,191,193,1,0,0,0,192,190,1,0,0,0,193,203,
        5,8,0,0,194,195,5,11,0,0,195,199,5,7,0,0,196,198,3,2,1,0,197,196,
        1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,202,
        1,0,0,0,201,199,1,0,0,0,202,204,5,8,0,0,203,194,1,0,0,0,203,204,
        1,0,0,0,204,23,1,0,0,0,205,206,3,8,4,0,206,207,3,42,21,0,207,208,
        3,8,4,0,208,25,1,0,0,0,209,210,5,12,0,0,210,214,5,3,0,0,211,215,
        3,4,2,0,212,215,3,6,3,0,213,215,5,1,0,0,214,211,1,0,0,0,214,212,
        1,0,0,0,214,213,1,0,0,0,215,216,1,0,0,0,216,217,3,24,12,0,217,218,
        5,1,0,0,218,219,3,28,14,0,219,220,5,4,0,0,220,224,5,7,0,0,221,223,
        3,2,1,0,222,221,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,
        1,0,0,0,225,227,1,0,0,0,226,224,1,0,0,0,227,228,5,8,0,0,228,27,1,
        0,0,0,229,230,5,35,0,0,230,231,5,2,0,0,231,232,3,8,4,0,232,29,1,
        0,0,0,233,234,5,13,0,0,234,235,5,3,0,0,235,236,3,24,12,0,236,237,
        5,4,0,0,237,241,5,7,0,0,238,240,3,2,1,0,239,238,1,0,0,0,240,243,
        1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,244,1,0,0,0,243,241,
        1,0,0,0,244,245,5,8,0,0,245,31,1,0,0,0,246,251,3,46,23,0,247,251,
        3,48,24,0,248,251,3,50,25,0,249,251,3,52,26,0,250,246,1,0,0,0,250,
        247,1,0,0,0,250,248,1,0,0,0,250,249,1,0,0,0,251,33,1,0,0,0,252,253,
        5,14,0,0,253,264,5,3,0,0,254,265,3,8,4,0,255,260,5,37,0,0,256,257,
        5,15,0,0,257,259,5,35,0,0,258,256,1,0,0,0,259,262,1,0,0,0,260,258,
        1,0,0,0,260,261,1,0,0,0,261,265,1,0,0,0,262,260,1,0,0,0,263,265,
        5,35,0,0,264,254,1,0,0,0,264,255,1,0,0,0,264,263,1,0,0,0,265,266,
        1,0,0,0,266,267,5,4,0,0,267,35,1,0,0,0,268,269,5,16,0,0,269,270,
        3,8,4,0,270,37,1,0,0,0,271,272,5,17,0,0,272,273,5,3,0,0,273,274,
        5,4,0,0,274,39,1,0,0,0,275,276,7,0,0,0,276,41,1,0,0,0,277,278,7,
        1,0,0,278,43,1,0,0,0,279,280,7,2,0,0,280,45,1,0,0,0,281,282,5,31,
        0,0,282,47,1,0,0,0,283,284,5,32,0,0,284,49,1,0,0,0,285,286,5,33,
        0,0,286,51,1,0,0,0,287,288,5,34,0,0,288,53,1,0,0,0,26,57,67,71,78,
        81,88,90,105,116,122,131,140,147,160,170,173,180,190,199,203,214,
        224,241,250,260,264
    ]

class MiLenguajeParser ( Parser ):

    grammarFileName = "MiLenguaje.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'('", "')'", "'fct'", "':'", 
                     "'{'", "'}'", "','", "'if'", "'else'", "'for'", "'while'", 
                     "'clg'", "'$'", "'rtn'", "'scn'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'const'", "'final'", "'ent'", "'flt'", "'lg'", 
                     "'str'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMERO_VALORES", 
                      "STRING", "WS", "COMMENT" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_declaracion = 2
    RULE_asignacion = 3
    RULE_expresion = 4
    RULE_termino = 5
    RULE_funcionConRetorno = 6
    RULE_funcionSinRetorno = 7
    RULE_parametros = 8
    RULE_llamadaFuncion = 9
    RULE_estructuraDeControl = 10
    RULE_estructuraIf = 11
    RULE_expresionLogica = 12
    RULE_cicloFor = 13
    RULE_asignacionFor = 14
    RULE_cicloWhile = 15
    RULE_tipo = 16
    RULE_kwClg = 17
    RULE_retornoSentencia = 18
    RULE_kwScn = 19
    RULE_operadoresAritmeticos = 20
    RULE_operadoresComparacion = 21
    RULE_kwUnmutable = 22
    RULE_kwEnt = 23
    RULE_kwFlt = 24
    RULE_kwLg = 25
    RULE_kwStr = 26

    ruleNames =  [ "programa", "sentencia", "declaracion", "asignacion", 
                   "expresion", "termino", "funcionConRetorno", "funcionSinRetorno", 
                   "parametros", "llamadaFuncion", "estructuraDeControl", 
                   "estructuraIf", "expresionLogica", "cicloFor", "asignacionFor", 
                   "cicloWhile", "tipo", "kwClg", "retornoSentencia", "kwScn", 
                   "operadoresAritmeticos", "operadoresComparacion", "kwUnmutable", 
                   "kwEnt", "kwFlt", "kwLg", "kwStr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    ID=35
    NUMERO_VALORES=36
    STRING=37
    WS=38
    COMMENT=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiLenguajeParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = MiLenguajeParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68182701088) != 0):
                self.state = 54
                self.sentencia()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(MiLenguajeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(MiLenguajeParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(MiLenguajeParser.AsignacionContext,0)


        def estructuraDeControl(self):
            return self.getTypedRuleContext(MiLenguajeParser.EstructuraDeControlContext,0)


        def llamadaFuncion(self):
            return self.getTypedRuleContext(MiLenguajeParser.LlamadaFuncionContext,0)


        def kwClg(self):
            return self.getTypedRuleContext(MiLenguajeParser.KwClgContext,0)


        def funcionConRetorno(self):
            return self.getTypedRuleContext(MiLenguajeParser.FuncionConRetornoContext,0)


        def funcionSinRetorno(self):
            return self.getTypedRuleContext(MiLenguajeParser.FuncionSinRetornoContext,0)


        def retornoSentencia(self):
            return self.getTypedRuleContext(MiLenguajeParser.RetornoSentenciaContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = MiLenguajeParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        self._la = 0 # Token type
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.estructuraDeControl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.llamadaFuncion()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 66
                    self.match(MiLenguajeParser.T__0)


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.kwClg()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 70
                    self.match(MiLenguajeParser.T__0)


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.funcionConRetorno()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.funcionSinRetorno()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.retornoSentencia()
                self.state = 76
                self.match(MiLenguajeParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(MiLenguajeParser.TipoContext,0)


        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def kwUnmutable(self):
            return self.getTypedRuleContext(MiLenguajeParser.KwUnmutableContext,0)


        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def kwScn(self):
            return self.getTypedRuleContext(MiLenguajeParser.KwScnContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = MiLenguajeParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 80
                self.kwUnmutable()


            self.state = 83
            self.tipo()
            self.state = 84
            self.match(MiLenguajeParser.ID)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 85
                self.match(MiLenguajeParser.T__1)
                self.state = 88
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 35, 36, 37]:
                    self.state = 86
                    self.expresion()
                    pass
                elif token in [17]:
                    self.state = 87
                    self.kwScn()
                    pass
                else:
                    raise NoViableAltException(self)



            self.state = 92
            self.match(MiLenguajeParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = MiLenguajeParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(MiLenguajeParser.ID)
            self.state = 95
            self.match(MiLenguajeParser.T__1)
            self.state = 96
            self.expresion()
            self.state = 97
            self.match(MiLenguajeParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.TerminoContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.TerminoContext,i)


        def operadoresAritmeticos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.OperadoresAritmeticosContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.OperadoresAritmeticosContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = MiLenguajeParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.termino()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8126464) != 0):
                self.state = 100
                self.operadoresAritmeticos()
                self.state = 101
                self.termino()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def llamadaFuncion(self):
            return self.getTypedRuleContext(MiLenguajeParser.LlamadaFuncionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def NUMERO_VALORES(self):
            return self.getToken(MiLenguajeParser.NUMERO_VALORES, 0)

        def STRING(self):
            return self.getToken(MiLenguajeParser.STRING, 0)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = MiLenguajeParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_termino)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.llamadaFuncion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(MiLenguajeParser.T__2)
                self.state = 110
                self.expresion()
                self.state = 111
                self.match(MiLenguajeParser.T__3)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.match(MiLenguajeParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.match(MiLenguajeParser.NUMERO_VALORES)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 115
                self.match(MiLenguajeParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionConRetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def tipo(self):
            return self.getTypedRuleContext(MiLenguajeParser.TipoContext,0)


        def parametros(self):
            return self.getTypedRuleContext(MiLenguajeParser.ParametrosContext,0)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_funcionConRetorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionConRetorno" ):
                listener.enterFuncionConRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionConRetorno" ):
                listener.exitFuncionConRetorno(self)




    def funcionConRetorno(self):

        localctx = MiLenguajeParser.FuncionConRetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcionConRetorno)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MiLenguajeParser.T__4)
            self.state = 119
            self.match(MiLenguajeParser.ID)
            self.state = 120
            self.match(MiLenguajeParser.T__2)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0):
                self.state = 121
                self.parametros()


            self.state = 124
            self.match(MiLenguajeParser.T__3)
            self.state = 125
            self.match(MiLenguajeParser.T__5)
            self.state = 126
            self.tipo()
            self.state = 127
            self.match(MiLenguajeParser.T__6)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68182701088) != 0):
                self.state = 128
                self.sentencia()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(MiLenguajeParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionSinRetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def parametros(self):
            return self.getTypedRuleContext(MiLenguajeParser.ParametrosContext,0)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_funcionSinRetorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionSinRetorno" ):
                listener.enterFuncionSinRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionSinRetorno" ):
                listener.exitFuncionSinRetorno(self)




    def funcionSinRetorno(self):

        localctx = MiLenguajeParser.FuncionSinRetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcionSinRetorno)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MiLenguajeParser.T__4)
            self.state = 137
            self.match(MiLenguajeParser.ID)
            self.state = 138
            self.match(MiLenguajeParser.T__2)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0):
                self.state = 139
                self.parametros()


            self.state = 142
            self.match(MiLenguajeParser.T__3)
            self.state = 143
            self.match(MiLenguajeParser.T__6)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68182701088) != 0):
                self.state = 144
                self.sentencia()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(MiLenguajeParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.TipoContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.TipoContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiLenguajeParser.ID)
            else:
                return self.getToken(MiLenguajeParser.ID, i)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = MiLenguajeParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.tipo()
            self.state = 153
            self.match(MiLenguajeParser.ID)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 154
                self.match(MiLenguajeParser.T__8)
                self.state = 155
                self.tipo()
                self.state = 156
                self.match(MiLenguajeParser.ID)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_llamadaFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFuncion" ):
                listener.enterLlamadaFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFuncion" ):
                listener.exitLlamadaFuncion(self)




    def llamadaFuncion(self):

        localctx = MiLenguajeParser.LlamadaFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_llamadaFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MiLenguajeParser.ID)
            self.state = 164
            self.match(MiLenguajeParser.T__2)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 240518168584) != 0):
                self.state = 165
                self.expresion()
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 166
                    self.match(MiLenguajeParser.T__8)
                    self.state = 167
                    self.expresion()
                    self.state = 172
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 175
            self.match(MiLenguajeParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstructuraDeControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estructuraIf(self):
            return self.getTypedRuleContext(MiLenguajeParser.EstructuraIfContext,0)


        def cicloFor(self):
            return self.getTypedRuleContext(MiLenguajeParser.CicloForContext,0)


        def cicloWhile(self):
            return self.getTypedRuleContext(MiLenguajeParser.CicloWhileContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_estructuraDeControl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstructuraDeControl" ):
                listener.enterEstructuraDeControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstructuraDeControl" ):
                listener.exitEstructuraDeControl(self)




    def estructuraDeControl(self):

        localctx = MiLenguajeParser.EstructuraDeControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_estructuraDeControl)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.estructuraIf()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.cicloFor()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.cicloWhile()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstructuraIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionLogica(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionLogicaContext,0)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_estructuraIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstructuraIf" ):
                listener.enterEstructuraIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstructuraIf" ):
                listener.exitEstructuraIf(self)




    def estructuraIf(self):

        localctx = MiLenguajeParser.EstructuraIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_estructuraIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(MiLenguajeParser.T__9)
            self.state = 183
            self.match(MiLenguajeParser.T__2)
            self.state = 184
            self.expresionLogica()
            self.state = 185
            self.match(MiLenguajeParser.T__3)
            self.state = 186
            self.match(MiLenguajeParser.T__6)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68182701088) != 0):
                self.state = 187
                self.sentencia()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
            self.match(MiLenguajeParser.T__7)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 194
                self.match(MiLenguajeParser.T__10)
                self.state = 195
                self.match(MiLenguajeParser.T__6)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68182701088) != 0):
                    self.state = 196
                    self.sentencia()
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 202
                self.match(MiLenguajeParser.T__7)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionLogicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,i)


        def operadoresComparacion(self):
            return self.getTypedRuleContext(MiLenguajeParser.OperadoresComparacionContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_expresionLogica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionLogica" ):
                listener.enterExpresionLogica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionLogica" ):
                listener.exitExpresionLogica(self)




    def expresionLogica(self):

        localctx = MiLenguajeParser.ExpresionLogicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expresionLogica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.expresion()
            self.state = 206
            self.operadoresComparacion()
            self.state = 207
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionLogica(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionLogicaContext,0)


        def asignacionFor(self):
            return self.getTypedRuleContext(MiLenguajeParser.AsignacionForContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(MiLenguajeParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(MiLenguajeParser.AsignacionContext,0)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_cicloFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCicloFor" ):
                listener.enterCicloFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCicloFor" ):
                listener.exitCicloFor(self)




    def cicloFor(self):

        localctx = MiLenguajeParser.CicloForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_cicloFor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiLenguajeParser.T__11)
            self.state = 210
            self.match(MiLenguajeParser.T__2)
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30, 31, 32, 33, 34]:
                self.state = 211
                self.declaracion()
                pass
            elif token in [35]:
                self.state = 212
                self.asignacion()
                pass
            elif token in [1]:
                self.state = 213
                self.match(MiLenguajeParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 216
            self.expresionLogica()
            self.state = 217
            self.match(MiLenguajeParser.T__0)
            self.state = 218
            self.asignacionFor()
            self.state = 219
            self.match(MiLenguajeParser.T__3)
            self.state = 220
            self.match(MiLenguajeParser.T__6)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68182701088) != 0):
                self.state = 221
                self.sentencia()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self.match(MiLenguajeParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiLenguajeParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_asignacionFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionFor" ):
                listener.enterAsignacionFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionFor" ):
                listener.exitAsignacionFor(self)




    def asignacionFor(self):

        localctx = MiLenguajeParser.AsignacionForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_asignacionFor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MiLenguajeParser.ID)
            self.state = 230
            self.match(MiLenguajeParser.T__1)
            self.state = 231
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionLogica(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionLogicaContext,0)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiLenguajeParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiLenguajeParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_cicloWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCicloWhile" ):
                listener.enterCicloWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCicloWhile" ):
                listener.exitCicloWhile(self)




    def cicloWhile(self):

        localctx = MiLenguajeParser.CicloWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cicloWhile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MiLenguajeParser.T__12)
            self.state = 234
            self.match(MiLenguajeParser.T__2)
            self.state = 235
            self.expresionLogica()
            self.state = 236
            self.match(MiLenguajeParser.T__3)
            self.state = 237
            self.match(MiLenguajeParser.T__6)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68182701088) != 0):
                self.state = 238
                self.sentencia()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 244
            self.match(MiLenguajeParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kwEnt(self):
            return self.getTypedRuleContext(MiLenguajeParser.KwEntContext,0)


        def kwFlt(self):
            return self.getTypedRuleContext(MiLenguajeParser.KwFltContext,0)


        def kwLg(self):
            return self.getTypedRuleContext(MiLenguajeParser.KwLgContext,0)


        def kwStr(self):
            return self.getTypedRuleContext(MiLenguajeParser.KwStrContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = MiLenguajeParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tipo)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.kwEnt()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.kwFlt()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.kwLg()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.kwStr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KwClgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def STRING(self):
            return self.getToken(MiLenguajeParser.STRING, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiLenguajeParser.ID)
            else:
                return self.getToken(MiLenguajeParser.ID, i)

        def getRuleIndex(self):
            return MiLenguajeParser.RULE_kwClg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKwClg" ):
                listener.enterKwClg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKwClg" ):
                listener.exitKwClg(self)




    def kwClg(self):

        localctx = MiLenguajeParser.KwClgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_kwClg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(MiLenguajeParser.T__13)
            self.state = 253
            self.match(MiLenguajeParser.T__2)
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 254
                self.expresion()
                pass

            elif la_ == 2:
                self.state = 255
                self.match(MiLenguajeParser.STRING)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 256
                    self.match(MiLenguajeParser.T__14)
                    self.state = 257
                    self.match(MiLenguajeParser.ID)
                    self.state = 262
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.state = 263
                self.match(MiLenguajeParser.ID)
                pass


            self.state = 266
            self.match(MiLenguajeParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoSentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(MiLenguajeParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_retornoSentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetornoSentencia" ):
                listener.enterRetornoSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetornoSentencia" ):
                listener.exitRetornoSentencia(self)




    def retornoSentencia(self):

        localctx = MiLenguajeParser.RetornoSentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_retornoSentencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MiLenguajeParser.T__15)
            self.state = 269
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KwScnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_kwScn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKwScn" ):
                listener.enterKwScn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKwScn" ):
                listener.exitKwScn(self)




    def kwScn(self):

        localctx = MiLenguajeParser.KwScnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_kwScn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MiLenguajeParser.T__16)
            self.state = 272
            self.match(MiLenguajeParser.T__2)
            self.state = 273
            self.match(MiLenguajeParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadoresAritmeticosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_operadoresAritmeticos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadoresAritmeticos" ):
                listener.enterOperadoresAritmeticos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadoresAritmeticos" ):
                listener.exitOperadoresAritmeticos(self)




    def operadoresAritmeticos(self):

        localctx = MiLenguajeParser.OperadoresAritmeticosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operadoresAritmeticos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8126464) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperadoresComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_operadoresComparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadoresComparacion" ):
                listener.enterOperadoresComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadoresComparacion" ):
                listener.exitOperadoresComparacion(self)




    def operadoresComparacion(self):

        localctx = MiLenguajeParser.OperadoresComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_operadoresComparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KwUnmutableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_kwUnmutable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKwUnmutable" ):
                listener.enterKwUnmutable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKwUnmutable" ):
                listener.exitKwUnmutable(self)




    def kwUnmutable(self):

        localctx = MiLenguajeParser.KwUnmutableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_kwUnmutable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KwEntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_kwEnt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKwEnt" ):
                listener.enterKwEnt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKwEnt" ):
                listener.exitKwEnt(self)




    def kwEnt(self):

        localctx = MiLenguajeParser.KwEntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_kwEnt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(MiLenguajeParser.T__30)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KwFltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_kwFlt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKwFlt" ):
                listener.enterKwFlt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKwFlt" ):
                listener.exitKwFlt(self)




    def kwFlt(self):

        localctx = MiLenguajeParser.KwFltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_kwFlt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MiLenguajeParser.T__31)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KwLgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_kwLg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKwLg" ):
                listener.enterKwLg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKwLg" ):
                listener.exitKwLg(self)




    def kwLg(self):

        localctx = MiLenguajeParser.KwLgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_kwLg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(MiLenguajeParser.T__32)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KwStrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiLenguajeParser.RULE_kwStr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKwStr" ):
                listener.enterKwStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKwStr" ):
                listener.exitKwStr(self)




    def kwStr(self):

        localctx = MiLenguajeParser.KwStrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_kwStr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(MiLenguajeParser.T__33)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





