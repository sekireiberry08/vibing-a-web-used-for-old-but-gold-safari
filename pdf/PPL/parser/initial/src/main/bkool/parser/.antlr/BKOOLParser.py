# Generated from /Users/sekireiberry/Documents/HK261/PPL/parser/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
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
        4,1,19,178,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,56,8,1,1,2,1,2,3,2,60,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,
        1,5,3,5,72,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,3,8,85,
        8,8,1,9,1,9,1,9,1,9,1,9,3,9,92,8,9,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,12,3,12,105,8,12,1,13,1,13,3,13,109,8,13,1,
        14,1,14,1,14,3,14,114,8,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,3,17,132,8,17,1,18,1,
        18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,143,8,19,1,20,1,20,1,
        20,1,20,1,20,3,20,150,8,20,1,21,1,21,1,21,1,21,1,21,1,21,5,21,158,
        8,21,10,21,12,21,161,9,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        3,22,171,8,22,1,23,1,23,1,23,1,23,1,23,1,23,0,1,42,24,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,2,1,0,
        2,3,1,0,13,14,170,0,48,1,0,0,0,2,55,1,0,0,0,4,59,1,0,0,0,6,61,1,
        0,0,0,8,65,1,0,0,0,10,71,1,0,0,0,12,73,1,0,0,0,14,78,1,0,0,0,16,
        84,1,0,0,0,18,91,1,0,0,0,20,93,1,0,0,0,22,96,1,0,0,0,24,104,1,0,
        0,0,26,108,1,0,0,0,28,113,1,0,0,0,30,115,1,0,0,0,32,120,1,0,0,0,
        34,131,1,0,0,0,36,133,1,0,0,0,38,142,1,0,0,0,40,149,1,0,0,0,42,151,
        1,0,0,0,44,170,1,0,0,0,46,172,1,0,0,0,48,49,3,2,1,0,49,50,5,0,0,
        1,50,1,1,0,0,0,51,52,3,4,2,0,52,53,3,2,1,0,53,56,1,0,0,0,54,56,3,
        4,2,0,55,51,1,0,0,0,55,54,1,0,0,0,56,3,1,0,0,0,57,60,3,6,3,0,58,
        60,3,12,6,0,59,57,1,0,0,0,59,58,1,0,0,0,60,5,1,0,0,0,61,62,3,8,4,
        0,62,63,3,10,5,0,63,64,5,1,0,0,64,7,1,0,0,0,65,66,7,0,0,0,66,9,1,
        0,0,0,67,68,5,15,0,0,68,69,5,4,0,0,69,72,3,10,5,0,70,72,5,15,0,0,
        71,67,1,0,0,0,71,70,1,0,0,0,72,11,1,0,0,0,73,74,3,8,4,0,74,75,5,
        15,0,0,75,76,3,14,7,0,76,77,3,22,11,0,77,13,1,0,0,0,78,79,5,5,0,
        0,79,80,3,16,8,0,80,81,5,6,0,0,81,15,1,0,0,0,82,85,3,18,9,0,83,85,
        1,0,0,0,84,82,1,0,0,0,84,83,1,0,0,0,85,17,1,0,0,0,86,87,3,20,10,
        0,87,88,5,1,0,0,88,89,3,18,9,0,89,92,1,0,0,0,90,92,3,20,10,0,91,
        86,1,0,0,0,91,90,1,0,0,0,92,19,1,0,0,0,93,94,3,8,4,0,94,95,3,10,
        5,0,95,21,1,0,0,0,96,97,5,7,0,0,97,98,3,24,12,0,98,99,5,8,0,0,99,
        23,1,0,0,0,100,101,3,26,13,0,101,102,3,24,12,0,102,105,1,0,0,0,103,
        105,1,0,0,0,104,100,1,0,0,0,104,103,1,0,0,0,105,25,1,0,0,0,106,109,
        3,6,3,0,107,109,3,28,14,0,108,106,1,0,0,0,108,107,1,0,0,0,109,27,
        1,0,0,0,110,114,3,30,15,0,111,114,3,32,16,0,112,114,3,36,18,0,113,
        110,1,0,0,0,113,111,1,0,0,0,113,112,1,0,0,0,114,29,1,0,0,0,115,116,
        5,15,0,0,116,117,5,9,0,0,117,118,3,38,19,0,118,119,5,1,0,0,119,31,
        1,0,0,0,120,121,5,15,0,0,121,122,5,5,0,0,122,123,3,34,17,0,123,124,
        5,6,0,0,124,125,5,1,0,0,125,33,1,0,0,0,126,127,3,38,19,0,127,128,
        5,4,0,0,128,129,3,34,17,0,129,132,1,0,0,0,130,132,3,38,19,0,131,
        126,1,0,0,0,131,130,1,0,0,0,132,35,1,0,0,0,133,134,5,10,0,0,134,
        135,3,38,19,0,135,136,5,1,0,0,136,37,1,0,0,0,137,138,3,40,20,0,138,
        139,5,11,0,0,139,140,3,38,19,0,140,143,1,0,0,0,141,143,3,40,20,0,
        142,137,1,0,0,0,142,141,1,0,0,0,143,39,1,0,0,0,144,145,3,42,21,0,
        145,146,5,12,0,0,146,147,3,42,21,0,147,150,1,0,0,0,148,150,3,42,
        21,0,149,144,1,0,0,0,149,148,1,0,0,0,150,41,1,0,0,0,151,152,6,21,
        -1,0,152,153,3,44,22,0,153,159,1,0,0,0,154,155,10,2,0,0,155,156,
        7,1,0,0,156,158,3,44,22,0,157,154,1,0,0,0,158,161,1,0,0,0,159,157,
        1,0,0,0,159,160,1,0,0,0,160,43,1,0,0,0,161,159,1,0,0,0,162,171,5,
        16,0,0,163,171,5,17,0,0,164,171,5,15,0,0,165,171,3,46,23,0,166,167,
        5,5,0,0,167,168,3,38,19,0,168,169,5,6,0,0,169,171,1,0,0,0,170,162,
        1,0,0,0,170,163,1,0,0,0,170,164,1,0,0,0,170,165,1,0,0,0,170,166,
        1,0,0,0,171,45,1,0,0,0,172,173,5,15,0,0,173,174,5,5,0,0,174,175,
        3,34,17,0,175,176,5,6,0,0,176,47,1,0,0,0,13,55,59,71,84,91,104,108,
        113,131,142,149,159,170
    ]

class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'int'", "'float'", "','", "'('", 
                     "')'", "'{'", "'}'", "'='", "'return'", "'+'", "'-'", 
                     "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INTLIT", 
                      "FLOATLIT", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_typ_ = 4
    RULE_listid = 5
    RULE_funcdecl = 6
    RULE_paramdecl = 7
    RULE_paramlist = 8
    RULE_params = 9
    RULE_param = 10
    RULE_body = 11
    RULE_inner = 12
    RULE_member = 13
    RULE_stmt = 14
    RULE_assignment = 15
    RULE_call = 16
    RULE_exprlist = 17
    RULE_retur_ = 18
    RULE_expr = 19
    RULE_expr0 = 20
    RULE_expr1 = 21
    RULE_operand = 22
    RULE_call_ = 23

    ruleNames =  [ "program", "decls", "decl", "vardecl", "typ_", "listid", 
                   "funcdecl", "paramdecl", "paramlist", "params", "param", 
                   "body", "inner", "member", "stmt", "assignment", "call", 
                   "exprlist", "retur_", "expr", "expr0", "expr1", "operand", 
                   "call_" ]

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
    ID=15
    INTLIT=16
    FLOATLIT=17
    WS=18
    ERROR_CHAR=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(BKOOLParser.DeclsContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.decls()
            self.state = 49
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(BKOOLParser.DeclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decls




    def decls(self):

        localctx = BKOOLParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.decl()
                self.state = 52
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ_(self):
            return self.getTypedRuleContext(BKOOLParser.Typ_Context,0)


        def listid(self):
            return self.getTypedRuleContext(BKOOLParser.ListidContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.typ_()
            self.state = 62
            self.listid()
            self.state = 63
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typ_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_typ_




    def typ_(self):

        localctx = BKOOLParser.Typ_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typ_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
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


    class ListidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def listid(self):
            return self.getTypedRuleContext(BKOOLParser.ListidContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listid




    def listid(self):

        localctx = BKOOLParser.ListidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_listid)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(BKOOLParser.ID)
                self.state = 68
                self.match(BKOOLParser.T__3)
                self.state = 69
                self.listid()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ_(self):
            return self.getTypedRuleContext(BKOOLParser.Typ_Context,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParamdeclContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.typ_()
            self.state = 74
            self.match(BKOOLParser.ID)
            self.state = 75
            self.paramdecl()
            self.state = 76
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramdecl




    def paramdecl(self):

        localctx = BKOOLParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(BKOOLParser.T__4)
            self.state = 79
            self.paramlist()
            self.state = 80
            self.match(BKOOLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramlist)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.params()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)

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


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def params(self):
            return self.getTypedRuleContext(BKOOLParser.ParamsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_params




    def params(self):

        localctx = BKOOLParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_params)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.param()
                self.state = 87
                self.match(BKOOLParser.T__0)
                self.state = 88
                self.params()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ_(self):
            return self.getTypedRuleContext(BKOOLParser.Typ_Context,0)


        def listid(self):
            return self.getTypedRuleContext(BKOOLParser.ListidContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.typ_()
            self.state = 94
            self.listid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inner(self):
            return self.getTypedRuleContext(BKOOLParser.InnerContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_body




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKOOLParser.T__6)
            self.state = 97
            self.inner()
            self.state = 98
            self.match(BKOOLParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InnerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def inner(self):
            return self.getTypedRuleContext(BKOOLParser.InnerContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_inner




    def inner(self):

        localctx = BKOOLParser.InnerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inner)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 10, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.member()
                self.state = 101
                self.inner()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)

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


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_member)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.vardecl()
                pass
            elif token in [10, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.stmt()
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(BKOOLParser.AssignmentContext,0)


        def call(self):
            return self.getTypedRuleContext(BKOOLParser.CallContext,0)


        def retur_(self):
            return self.getTypedRuleContext(BKOOLParser.Retur_Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.retur_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignment




    def assignment(self):

        localctx = BKOOLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(BKOOLParser.ID)
            self.state = 116
            self.match(BKOOLParser.T__8)
            self.state = 117
            self.expr()
            self.state = 118
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_call




    def call(self):

        localctx = BKOOLParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(BKOOLParser.ID)
            self.state = 121
            self.match(BKOOLParser.T__4)
            self.state = 122
            self.exprlist()
            self.state = 123
            self.match(BKOOLParser.T__5)
            self.state = 124
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exprlist)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.expr()
                self.state = 127
                self.match(BKOOLParser.T__3)
                self.state = 128
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Retur_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_retur_




    def retur_(self):

        localctx = BKOOLParser.Retur_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_retur_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(BKOOLParser.T__9)
            self.state = 134
            self.expr()
            self.state = 135
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr0(self):
            return self.getTypedRuleContext(BKOOLParser.Expr0Context,0)


        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.expr0()
                self.state = 138
                self.match(BKOOLParser.T__10)
                self.state = 139
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.expr0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr1Context,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr0




    def expr0(self):

        localctx = BKOOLParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr0)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.expr1(0)
                self.state = 145
                self.match(BKOOLParser.T__11)
                self.state = 146
                self.expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(BKOOLParser.OperandContext,0)


        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 154
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 155
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 156
                    self.operand() 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def call_(self):
            return self.getTypedRuleContext(BKOOLParser.Call_Context,0)


        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_operand




    def operand(self):

        localctx = BKOOLParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operand)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(BKOOLParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.call_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.match(BKOOLParser.T__4)
                self.state = 167
                self.expr()
                self.state = 168
                self.match(BKOOLParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_call_




    def call_(self):

        localctx = BKOOLParser.Call_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_call_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(BKOOLParser.ID)
            self.state = 173
            self.match(BKOOLParser.T__4)
            self.state = 174
            self.exprlist()
            self.state = 175
            self.match(BKOOLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.expr1_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




