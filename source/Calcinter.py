'''
Name: Calculator Simple language
Version: 1.0.0
Author: Naji Kadri
Description: A simple language that perfom mathemetical calculations
'''

from rply import LexerGenerator,ParserGenerator
import math
from sys import *

#LEXERS (TOKENS)

lg = LexerGenerator()

lg.add('NUMBER',r'\d+')
lg.add('PLUS',r'\+')
lg.add('MINUS',r'\-')
lg.add('MULT',r'\*')
lg.add('DIV',r'/')
lg.add('POW',r'\^')
lg.add('LOG',r'log')
lg.add('RAD',r'rad')
lg.add('OPEN_PARENS',r'\(')
lg.add('CLOSE_PARENS',r'\)')
lg.ignore(r'\s+')
lg.ignore(r'\Z')


lexer = lg.build()


#AST (ABSTRACT SYNTAX TREE)

class Number (object):
    def __init__(self,value):
        self.value = value
    def eval(self):
        return self.value

class BinaryOpr (object):
    def __init__(self,left,right):
        self.left = left
        self.right = right

class Add (BinaryOpr):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub (BinaryOpr):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mult (BinaryOpr):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div (BinaryOpr):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Pow (BinaryOpr):
    def eval(self):
        return self.left.eval() ** self.right.eval()

# PARSER

pg = ParserGenerator(
    ['NUMBER','OPEN_PARENS','CLOSE_PARENS','PLUS','MINUS','MULT','DIV','POW','LOG','RAD'],
    precedence = [
        ('left',['PLUS','MINUS']),
        ('left',['MULT','DIV']),
        ('left',['POW'])
        ]
    )

@pg.production('expression : NUMBER')
def expression_number(p):
    return Number(int(p[0].getstr()))

@pg.production('expression : RAD OPEN_PARENS expression CLOSE_PARENS')
def expression_radical (p):
    return Number(math.sqrt(p[2].value))

@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    return p[1]

@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MULT expression')
@pg.production('expression : expression DIV expression')
@pg.production('expression : expression POW expression')
def expression_binop(p):
    left = p[0]
    right = p[2]
    if p[1].gettokentype() == 'PLUS':
        return Add(left, right)
    elif p[1].gettokentype() == 'MINUS':
        return Sub(left, right)
    elif p[1].gettokentype() == 'MULT':
        return Mult(left, right)
    elif p[1].gettokentype() == 'DIV':
        return Div(left, right)
    elif p[1].gettokentype() == 'POW':
        return Pow(left,right)
    else:
        raise AssertionError('Oops, this should not be possible!')
@pg.production('expression : LOG OPEN_PARENS expression CLOSE_PARENS')
def expression_log(p):
    return Number(math.log10(p[2].value))

@pg.error
def error_handler(token):
    raise ValueError("Ran into  a %s where it is not expected" % token.gettokentype())
parser = pg.build()

def interpret ():
    while True:
        sent = input()
        if(sent != ''):
            print(parser.parse(lexer.lex(sent)).eval())
        else:
            break
        
def readFile ():
    file = open(argv[1],"r").read()
    file = file.split('\n')
    for line in file:
        if len(line) > 0 and line != '':
            print(line+" = "+str(parser.parse(lexer.lex(line)).eval()))
        else:
            continue
        
if __name__ == '__main__':
    print('Calculator Simple Language Interpreter\n')
    if len(argv) > 1:
        readFile()
    else:
        interpret()
