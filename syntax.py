# -*- coding: utf-8 -*-
Syntons = []

class OperSynt():
    sType = None  ##  obj, obj:?, fun, block, obj, method, item, enum
    sVarName = None
    mAttr = []
    sFilter = None ## 2, >1
    mOperand = []
    sSpecial = None  ## @, !, \, :
    sSuff = None     ## !
    mOperation = []
    mItem = []
    cValue = None

    def __init__(self, sTyp, sName = None):
        self.sType = sTyp
        self.sVarName = sName


class Operation():
    sType = None  ##  +, -, *, /, %, ^, ~, &, |, >, <, ++, --, &&, ||, <>, ><, ->, ... new
    iPriority = None

    def __init__(self, sTyp, iPrior):
        self.sType = sTyp
        self.iPriority = iPrior


class ItemSynt():
    sType = None  ##  basic: (code, fun:function, class, operand, type, proc:procedure)
                  ##  stream: (if, else, eisif, case, ifcase, flow, do, while, try, except, for, each)
                  ##  sub: (code, method, fun:function, class)
                  ##  type: (unk, bool, int, str, list, dict, coll, enum, date, db, const, block, new...)
                  ##  subtype: (unk, bool, int, str, list, dict, coll, enum, date, db, const, block, new...)
                  ##  area: (global, private, ...)
                  ##  setget: (set, get)
                  ##  process: (print, del, ...)
                  ##  proc: (new, ...)
    sName = None  # (code, fun, method, operand, ...
    mItem = []
    mAttr = []
    mVar = []
    mOperand = []
    mOperation = []

    def __init__(self, sTyp, sNam):
        self.sType = sTyp
        self.sName = sNam

    def printSyn(self):
        print(self.sName, self.sType, self.mVars, self.mVals, self.mSyntons)

class ValueSynt():
    sType = None  ##  int, float, str, list, coll, dict, method, ... new
    mVar = []
    mVarKey = []
    mKey = []
    mValue = []

    def __init__(self, sTyp, mVal = []):
        self.sType = sTyp
        self.mValue = mVal


print("[dima, dim2] = person('Дмитрий', 'Анатольевич', 'Поварницын', age=37, sex=MAN)")
syn2 = ItemSynt('basic', 'code')

syn = Synton('simple', None)
#syn.sType = 'simple'
syn.mVars = ['dima', 'dim2']
syn.mVals.append(syn2)
syn.printSyn()

Syntons.append(syn)
