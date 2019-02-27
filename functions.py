# -*- coding: utf-8 -*-
from variables import Vars, Variable

# Basic functions

# construction of basic: <name>[(<attr1>, <attr2>, ...)] <operand>/[<operand>, <operand>, ...]
def basic(name, dAttr={}, lVariables=[]):
    if name == 'int':
        for var in lVariables:
            var = Variable()

# construction of function: <name>[(<attr1>, <attr2>, ...)]
def function(name, dAttr={}):
    if name == 'int':
        None
