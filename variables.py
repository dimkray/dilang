# -*- coding: utf-8 -*-

# Dictionary of global variables
Vars = {}
# Группы переменных и значений
Groups = []

def getTypeByValue(value):
    if value is None:
        return None
    if type(value) == bool:
        return 'bool'
    if type(value) == int:
        return 'int'
    if type(value) == float:
        return 'float'
    #if type(value) == str and value[0] == '"':
    #    return 'char'
    if type(value) == str:
        return 'str'
    if type(value) == list:
        return 'list'
    if type(value) == dict:
        return 'dict'
    if type(value) == set:
        return 'coll'

def setValueByType(value, typevar):
    if typevar == 'null':
        return None
    elif typevar == 'bool':
        if value == 0 or value == False or len(value) == 0:
            return False
        else:
            return True
    elif typevar == 'int':
        return len(value)
    elif typevar == 'float':
        return len(value)
    else:
        return Exception

class Variable:
    dVarSettings = {'value': None,    # значение
                    'type': None,     # тип: bool, integer, float, char, str, list, dict, coll, obj
                    'subtype': None,  # подтип для: list, dict, coll
                    'dec': False,     # declaration - признак объявления
                    'exp': False,     # явно заданный тип
                    'const': False    # признак константы
                    }
    def __init__(self, value, typevar=None, subtype=None, declaration=False, explicit=False, const=False):
        if typevar == None:
            self.dVarSettings['type'] = getTypeByValue(value)
        else:
            self.dVarSettings['type'] = typevar
        self.dVarSettings['subtype'] = subtype
        self.dVarSettings['dec'] = declaration
        self.dVarSettings['exp'] = explicit
        self.dVarSettings['const'] = const
        if getTypeByValue(value) != self.dVarSettings['type']:  # если тип и значения заданы разными
            self.dVarSettings['value'] = setValueByType(value, self.dVarSettings['type'])
        else:
            self.dVarSettings['value'] = value

#    def setType(self, typevar, subtype=None, declaration=False, explicit=False, const=False):