# -*- coding: utf-8 -*-
from strings import clearStringByChar

commentChar = '#'
commentBlockStart = '#{'
commentBlockEnd = '}#'

def commentProcess(code: str):
    code = clearStringByChar(code, commentBlockStart, commentBlockEnd)
    clearCode = ''
    for str in code.split('\n'):
        if commentChar in str:
            clearCode += str[:str.find(commentChar)]
        else:
            clearCode += str
        clearCode + '\n'
    return clearCode

def clearProcess(code: str):
    clearCode = commentProcess(code)
    return clearCode

# def getOperands(code):
#     clearCode = commentProcess(code)
#     return