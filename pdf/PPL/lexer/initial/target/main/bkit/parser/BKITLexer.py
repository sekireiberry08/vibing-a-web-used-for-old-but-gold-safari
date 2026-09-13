# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,6,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,5,0,23,8,0,10,0,12,0,26,
        9,0,3,0,28,8,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,4,4,41,
        8,4,11,4,12,4,42,1,4,1,4,1,5,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,
        6,1,0,3,1,0,49,57,1,0,48,57,3,0,9,10,13,13,32,32,52,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,27,
        1,0,0,0,3,31,1,0,0,0,5,33,1,0,0,0,7,35,1,0,0,0,9,40,1,0,0,0,11,46,
        1,0,0,0,13,28,5,48,0,0,14,24,7,0,0,0,15,17,5,95,0,0,16,15,1,0,0,
        0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,21,1,0,0,0,20,18,
        1,0,0,0,21,23,7,1,0,0,22,18,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,
        24,25,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,27,13,1,0,0,0,27,14,1,
        0,0,0,28,29,1,0,0,0,29,30,6,0,0,0,30,2,1,0,0,0,31,32,5,59,0,0,32,
        4,1,0,0,0,33,34,5,58,0,0,34,6,1,0,0,0,35,36,5,86,0,0,36,37,5,97,
        0,0,37,38,5,114,0,0,38,8,1,0,0,0,39,41,7,2,0,0,40,39,1,0,0,0,41,
        42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,45,6,4,1,
        0,45,10,1,0,0,0,46,47,9,0,0,0,47,48,6,5,2,0,48,12,1,0,0,0,5,0,18,
        24,27,42,3,1,0,0,6,0,0,1,5,1
    ]

class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    WS = 5
    ERROR_CHAR = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR" ]

    ruleNames = [ "ID", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.ID_action 
            actions[5] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ID_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text.replace('_', '') 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


