# -*- coding: utf-8 -*-
from variables import Values

#charVar = charValue + ['']
#print charVar


def clearStringByChar(text: str, charStart: int, charEnd=None):
    if charStart not in text:
        return text
    clearText = ''
    if charEnd is None:
        charEnd = charStart
    posStart = 0
    posEnd = 0
    while posStart >= 0:
        posStart = text.find(charStart, posEnd)
        if posStart < 0:
            break
        clearText += text[posEnd:posStart]
        posEnd = text.find(charEnd, posStart + 1)
        if posEnd < 0:
            break
        else:
            posEnd += len(charEnd)
    if posEnd > 0:
        clearText += text[posEnd:]
    return clearText


def getPositions(code: str, startPosition, charStart, charEnd=None):
    posStart = startPosition
    posEnd = startPosition
    if charEnd is None:
        charEnd = charStart
    posStart = code.find(charStart, posStart)
    if posStart < 0:
        return -1, -1
    posEnd = code.find(charEnd, posStart + 1)
    if posEnd < 0:
        return posStart, len(code)
    else:
        posEnd += len(charEnd)
    return posStart, posEnd


def getCharPosition(code: str, strList: str, startPosition=0):
    position = len(code)
    for char in strList:
        posChar = code.find(char, startPosition)
        if posChar < position and posChar >= 0:
            position = code.find(char, startPosition)
    if position == len(code):
        position = -1
    return position


def checkChar(code: str, position: int, strList: str):
    if position >= len(code):
        return False
    sChar = code[position]
    for char in strList:
        if char == sChar:
            return True
    return False
