# -*- coding: utf-8 -*-
from strings import clearStringByChar, getPositions, getCharPosition, checkChar
from variables import Values
from constants import commentChar, commentBlockStart, commentBlockEnd, stringChar, stringBlock
from constants import charsStartVariable, charsVariable
from variables import Variable, Vars


# def typeDetect(value):
#     if value


def variableProcess(code: str):
    posVar = 0
    clearCode = code
    while posVar >= 0:
        posVar = getCharPosition(code, charsStartVariable, posVar)
        if posVar < 0:
            break
        sVar = code[posVar]
        posVar += posVar + 1
        while checkChar(code, posVar, charsVariable):
            sVar += code[posVar]
            posVar += 1
        Variable(sVar, None)
        clearCode = clearCode.replace(sVar, '_'+sVar)
    return clearCode

def stringProcess(code: str):
    posStart = 0
    posEnd = 0
    clearCode = code
    while posStart >= 0:
        posStringChar = code.find(stringChar, posStart)
        posStringBlock = code.find(stringBlock, posStart)
        if posStringChar < posStringBlock or posStringBlock < 0:
            posStart, posEnd = getPositions(code, posEnd, stringChar)
            bStringChar = True
        else:
            posStart, posEnd = getPositions(code, posEnd, stringBlock)
            bStringChar = False
        if posStart < 0:
            break
        else:
            sValue = code[posStart:posEnd]
            if '\n' in sValue and bStringChar:
                sValue = code[posStart:sValue.find('\n', posStart+1)]
            kValue = '_' + str(len(Values))
            Values[kValue] = sValue
            clearCode = clearCode.replace(sValue, kValue)
    return clearCode


def spaceProcess(code: str):
    code = code.replace('\n', ';')  # заменить все ENTER
    # code = re.sub(r'\s+', '', code, flags=re.UNICODE)  # удалить все пробелы
    code = ''.join(code.split())
    return code


def commentProcess(code: str):
    code = clearStringByChar(code, commentBlockStart, commentBlockEnd)
    clearCode = ''
    for sString in code.split('\n'):
        if commentChar in sString:
            clearCode += sString[:sString.find(commentChar)]
        else:
            clearCode += sString
        clearCode + '\n'
    return clearCode


def clearProcess(code: str):
    clearCode = commentProcess(code)
    clearCode = stringProcess(clearCode)
    clearCode = variableProcess(clearCode)
    clearCode = spaceProcess(clearCode)
    return clearCode

# def getOperands(code):
#     clearCode = commentProcess(code)
#     return