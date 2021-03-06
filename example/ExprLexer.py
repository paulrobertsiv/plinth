# $ANTLR 3.1.2 Expr.g 2010-04-20 15:39:29

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
WS=7
NEWLINE=4
T__12=12
T__11=11
T__13=13
T__10=10
INT=6
ID=5
EOF=-1
T__9=9
T__8=8


class ExprLexer(Lexer):

    grammarFileName = "Expr.g"
    antlr_version = version_str_to_tuple("3.1.2")
    antlr_version_str = "3.1.2"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        Lexer.__init__(self, input, state)

        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )






    # $ANTLR start "T__8"
    def mT__8(self, ):

        try:
            _type = T__8
            _channel = DEFAULT_CHANNEL

            # Expr.g:7:6: ( '=' )
            # Expr.g:7:8: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__8"



    # $ANTLR start "T__9"
    def mT__9(self, ):

        try:
            _type = T__9
            _channel = DEFAULT_CHANNEL

            # Expr.g:8:6: ( '+' )
            # Expr.g:8:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__9"



    # $ANTLR start "T__10"
    def mT__10(self, ):

        try:
            _type = T__10
            _channel = DEFAULT_CHANNEL

            # Expr.g:9:7: ( '-' )
            # Expr.g:9:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__10"



    # $ANTLR start "T__11"
    def mT__11(self, ):

        try:
            _type = T__11
            _channel = DEFAULT_CHANNEL

            # Expr.g:10:7: ( '*' )
            # Expr.g:10:9: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__11"



    # $ANTLR start "T__12"
    def mT__12(self, ):

        try:
            _type = T__12
            _channel = DEFAULT_CHANNEL

            # Expr.g:11:7: ( '(' )
            # Expr.g:11:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__12"



    # $ANTLR start "T__13"
    def mT__13(self, ):

        try:
            _type = T__13
            _channel = DEFAULT_CHANNEL

            # Expr.g:12:7: ( ')' )
            # Expr.g:12:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__13"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # Expr.g:28:3: ( ( 'a' .. 'z' | 'A' .. 'Z' )+ )
            # Expr.g:28:4: ( 'a' .. 'z' | 'A' .. 'Z' )+
            pass 
            # Expr.g:28:4: ( 'a' .. 'z' | 'A' .. 'Z' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((65 <= LA1_0 <= 90) or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # Expr.g:
                    pass 
                    if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # Expr.g:30:4: ( ( '0' .. '9' )+ )
            # Expr.g:30:5: ( '0' .. '9' )+
            pass 
            # Expr.g:30:5: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # Expr.g:30:5: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):

        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # Expr.g:32:8: ( ( '\\r' )? '\\n' )
            # Expr.g:32:9: ( '\\r' )? '\\n'
            pass 
            # Expr.g:32:9: ( '\\r' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 13) :
                alt3 = 1
            if alt3 == 1:
                # Expr.g:32:9: '\\r'
                pass 
                self.match(13)



            self.match(10)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # Expr.g:34:3: ( ( ' ' | '\\t' | '\\n' | '\\r' )+ )
            # Expr.g:34:4: ( ' ' | '\\t' | '\\n' | '\\r' )+
            pass 
            # Expr.g:34:4: ( ' ' | '\\t' | '\\n' | '\\r' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((9 <= LA4_0 <= 10) or LA4_0 == 13 or LA4_0 == 32) :
                    alt4 = 1


                if alt4 == 1:
                    # Expr.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1


            #action start
            self.skip()
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    def mTokens(self):
        # Expr.g:1:8: ( T__8 | T__9 | T__10 | T__11 | T__12 | T__13 | ID | INT | NEWLINE | WS )
        alt5 = 10
        alt5 = self.dfa5.predict(self.input)
        if alt5 == 1:
            # Expr.g:1:10: T__8
            pass 
            self.mT__8()


        elif alt5 == 2:
            # Expr.g:1:15: T__9
            pass 
            self.mT__9()


        elif alt5 == 3:
            # Expr.g:1:20: T__10
            pass 
            self.mT__10()


        elif alt5 == 4:
            # Expr.g:1:26: T__11
            pass 
            self.mT__11()


        elif alt5 == 5:
            # Expr.g:1:32: T__12
            pass 
            self.mT__12()


        elif alt5 == 6:
            # Expr.g:1:38: T__13
            pass 
            self.mT__13()


        elif alt5 == 7:
            # Expr.g:1:44: ID
            pass 
            self.mID()


        elif alt5 == 8:
            # Expr.g:1:47: INT
            pass 
            self.mINT()


        elif alt5 == 9:
            # Expr.g:1:51: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt5 == 10:
            # Expr.g:1:59: WS
            pass 
            self.mWS()







    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\11\uffff\1\13\1\14\2\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\11\10\uffff\1\12\1\11\2\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\172\10\uffff\1\12\1\40\2\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\2\uffff\1\12\1\11"
        )

    DFA5_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA5_transition = [
        DFA.unpack(u"\1\13\1\12\2\uffff\1\11\22\uffff\1\13\7\uffff\1\5\1"
        u"\6\1\4\1\2\1\uffff\1\3\2\uffff\12\10\3\uffff\1\1\3\uffff\32\7\6"
        u"\uffff\32\7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u"\2\13\2\uffff\1\13\22\uffff\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    DFA5 = DFA
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(ExprLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
