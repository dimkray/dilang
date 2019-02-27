# -*- coding: utf-8 -*-

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