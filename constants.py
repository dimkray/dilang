# -*- coding: utf-8 -*-
import string
print(string.ascii_letters)

commentChar = '#'
commentBlockStart = '#{'
commentBlockEnd = '}#'
stringChar = "'"
stringBlock = '"'

charsSeparator = [',', ';', '\n']
charsOperand = ['=', '>', '<', '+', '-', '&', '|', '^', '~', '%', '\\', '/', '*']
charsAction = ['@', '$', ':', '?', '!', '.']
charsSpecial = ['№', '`']
charsList = ['(', ')', '{', '}', '[', ']']
charsValueSeparator = charsSeparator + charsOperand + charsAction + charsSpecial
charsStartVariable = string.ascii_letters
charsVariable = string.ascii_letters + '_' + '0123456789'
