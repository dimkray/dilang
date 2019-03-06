# -*- coding: utf-8 -*-
from strings import  getPositions
Syntons = []


class Object:
    sType = None  ##  var, int, float, str, list, coll, dict, method, ... new
    mKey = []
    mObject = []

    def __init__(self, sTyp, mVal = []):
        self.sType = sTyp
        self.mObject = mVal


class Operand:
    sType = None  ##  obj, obj:?, fun, block, obj, method, item, enum
    sVarName = None
    cObject = None
    sFilter = None ## 2, >1
    mAttr = []
    mOperand = []
    mOperation = []
    sSpecial = None  ## @, !, \, :
    sSuffix = None     ## !

    def __init__(self, sTyp, sName = None):
        self.sType = sTyp
        self.sVarName = sName


class Operation:
    sType = None  ##  +, -, *, /, %, ^, ~, &, |, >, <, ++, --, &&, ||, <>, ><, ->, ... new
    iPriority = None

    def __init__(self, sTyp, iPrior):
        self.sType = sTyp
        self.iPriority = iPrior


class Item:
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

    def __init__(self, sTyp, sNam, mAttrs=[], mItems=[]):
        self.sType = sTyp
        self.sName = sNam
        self.mAttr = mAttrs
        self.mItem = mItems

    def printSyn(self):
        print(self.sName, self.sType, self.mVars, self.mVals, self.mSyntons)


class ItemOperand:
    #sType = None
    mVar = []
    mOperand = []
    mOperation = []

    def __init__(self, mVars=[], mOperands=[], mOperations=[]):
        self.mVar = mVars
        self.mOperand = mOperands
        self.mOperation = mOperations
        #self.sType = sTyp


def findChar(char: str, code: str, mLevel, iLevel=0):
    positions = []
    iPos = 0
    for iChar in code:
        if iChar == char and mLevel == iLevel:
            positions.append(iPos)
        iPos += 1
    return positions

def checkAreas(code: str):
    def addLevel(level, value):
        if level >= len(mType):
            mType.append(value)
        else:
            mType[level] = value

    iLevel = 0
    mType = [0]
    mLevel = []
    sLevel = ''
    position = 0
    for char in code:
        if char == '(':
            iLevel += 1
            addLevel(iLevel, 1)
            #mType[iLevel] = 1
        elif char == ')':
            if mType[iLevel] != 1:
                print('ERROR_AREA_END: ) on position ' + str(position+1))
                break
            iLevel -= 1
        elif char == '[':
            iLevel += 1
            addLevel(iLevel, 2)
            #mType[iLevel] = 2
        elif char == ']':
            if mType[iLevel] != 2:
                print('ERROR_AREA_END: ] on position ' + str(position+1))
                break
            iLevel -= 1
        elif char == '{':
            iLevel += 1
            addLevel(iLevel, 3)
            #mType[iLevel] = 3
        elif char == '}':
            if mType[iLevel] != 3:
                print('ERROR_AREA_END: } on position ' + str(position+1))
                break
            iLevel -= 1
        position += 1
        mLevel.append(iLevel)
        sLevel += str(iLevel)
    if iLevel != 0:
        if mType[iLevel] == 1: sType = ')'
        elif mType(iLevel) == 2: sType = ']'
        else: sType = '}'
        print('ERROR_AREA_END: expect %s on position %i' % (sType, position+1))
    print(sLevel)
    return mLevel


def separate(code: str, mLevel, iLevel, sSep = ';'):
    startPos = position = 0
    mItems = []
    mItemLevels = []
    for char in code:
        if char == sSep and mLevel[position] == iLevel:
            mItems.append(code[startPos:position])
            mItemLevels.append(mLevel[startPos:position])
            startPos = position + 1
        position += 1
    mItems.append(code[startPos:])
    mItemLevels.append(mLevel[startPos:])
    return mItems, mItemLevels


def createSyntax(code: str):
    mLevel = checkAreas(code)
    # Level 0
    mItem, mItemLevel = separate(code, mLevel, 0)
    iItem = 0
    for item in mItem:
        mPos = findChar('=', item, mItemLevel, 0)
        if len(mPos) > 1:
            print('ERROR_SINTAX: it is more then one symbol "=" on position ' + mPos[1])



st = " ();([(){}()]); int: [dima, [dim2]] = 500 * {[],[],[[(323;6)]], (6)} - 7*(5+9 - (854/2))"
print(st)
mLev = checkAreas(st)
print(separate(st, mLev, 0))

# itm = Item('basic', 'code', mItems=[ItemOperand(mVars=[])])
# Syntons.append()
#
# syn2 = ItemSynt('basic', 'code')
#
# syn = Synton('simple', None)
# #syn.sType = 'simple'
# syn.mVars = ['dima', 'dim2']
# syn.mVals.append(syn2)
# syn.printSyn()

#Syntons.append(syn)
