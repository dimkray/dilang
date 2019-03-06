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

basicWords = {'function':  {'type': 'basic', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'class':     {'type': 'basic', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'operation': {'type': 'basic', 'main': [], 'in': ['basic'], 'proc': True, 'fun': False, 'method': False },
              'type':      {'type': 'basic', 'main': [], 'in': ['basic'], 'proc': True, 'fun': False, 'method': True },
              'process':   {'type': 'basic', 'main': [], 'in': ['basic'], 'proc': True, 'fun': False, 'method': False },
              'method':    {'type': 'sub', 'main': [], 'in': ['class'], 'proc': True, 'fun': False, 'method': False },
              'if':        {'type': 'stream', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'elsif':     {'type': 'stream', 'main': ['if'], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'case':      {'type': 'case', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'when':      {'type': 'case', 'main': ['case'], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'for':       {'type': 'cycle', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'each':      {'type': 'cycle', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'do':        {'type': 'cycle', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'while':     {'type': 'cycle', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'settings':  {'type': 'settings', 'main': [], 'in': ['basic'], 'proc': True, 'fun': False, 'method': False },
              'trying':    {'type': 'settings', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'try':       {'type': 'trying', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'except':    {'type': 'trying', 'main': ['try'], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'else':      {'type': 'else', 'main': ['if', 'case', 'try'], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'goto':      {'type': 'stream', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'reference': {'type': 'stream', 'main': [], 'in': ['basic'], 'proc': True, 'fun': False, 'method': False },
              'variable':  {'type': 'var', 'main': [], 'in': ['basic'], 'proc': True, 'fun': False, 'method': False },
              'unknown':   {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': False, 'method': False },
              'boolean':   {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': True, 'method': True },
              'integer':   {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': True, 'method': True },
              'float':     {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': True, 'method': True },
              'string':    {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': True, 'method': True },
              'listing':   {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': True, 'method': True },
              'dictionary':  {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': True, 'method': True },
              'collection':  {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': True, 'method': True },
              'enumeration': {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': True, 'method': False },
              'datetime':    {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': True, 'method': False },
              'constant':    {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': False, 'method': False },
              'block':     {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': False, 'method': False },
              'object':    {'type': 'type', 'main': [], 'in': ['variable', '*'], 'proc': True, 'fun': False, 'method': False },
              'global':    {'type': 'area', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'private':   {'type': 'area', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'lock':      {'type': 'area', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'everywhere':  {'type': 'area', 'main': [], 'in': ['basic'], 'proc': True, 'fun': False, 'method': False },
              'super':       {'type': 'method', 'main': [], 'in': ['class'], 'proc': True, 'fun': False, 'method': False },
              'setting':     {'type': 'setget', 'main': [], 'in': ['class'], 'proc': True, 'fun': False, 'method': False },
              'getting':     {'type': 'setget', 'main': [], 'in': ['class'], 'proc': True, 'fun': False, 'method': False },
              'start':       {'type': 'stream', 'main': [], 'in': ['basic'], 'proc': True, 'fun': False, 'method': False },
              'end':        {'type': 'stream', 'main': [], 'in': ['basic'], 'proc': True, 'fun': False, 'method': False },
              'print':      {'type': 'process', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False },
              'delete':     {'type': 'process', 'main': [], 'in': [], 'proc': True, 'fun': True, 'method': True },
              'input':      {'type': 'process', 'main': [], 'in': [], 'proc': True, 'fun': True, 'method': False },
              'equal':      {'type': 'condition', 'main': [], 'in': [], 'proc': True, 'fun': True, 'method': True },
              'history':    {'type': 'valuation', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': True},
              'random':     {'type': 'valuation', 'main': [], 'in': [], 'proc': False, 'fun': True, 'method': True},
              'abstract':   {'type': 'valuation', 'main': [], 'in': [], 'proc': True, 'fun': True, 'method': True},
              'break':      {'type': 'cycle', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False},
              'next':       {'type': 'cycle', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False},
              'repeat':     {'type': 'cycle', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False},
              'replay':     {'type': 'cycle', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False},
              'default':    {'type': 'program', 'main': [], 'in': [], 'proc': False, 'fun': True, 'method': True},
              'import':     {'type': 'program', 'main': [], 'in': [], 'proc': True, 'fun': True, 'method': False},
              'with':       {'type': 'basic', 'main': [], 'in': [], 'proc': True, 'fun': False, 'method': False},
              'round':      {'type': 'valuation', 'main': [], 'in': [], 'proc': True, 'fun': True, 'method': True},

 }
keyWords = {'code': {'type': 'basic', 'basic': None, 'proc': True, 'fun': False, 'method': False},
            'fun': {'type': 'basic', 'basic': 'function', 'proc': True, 'fun': False, 'method': False},
            'cls': {'type': 'basic', 'basic': 'class', 'proc': True, 'fun': False, 'method': False},
            'oper': {'type': 'basic', 'basic': 'operation', 'proc': True, 'fun': False, 'method': False},
            'proc': {'type': 'basic', 'basic': 'process', 'proc': True, 'fun': False, 'method': False},
            'ref':  {'type': 'stream', 'basic': 'reference', 'proc': True, 'fun': False, 'method': False},
            'var': {'type': 'var', 'basic': 'variable', 'proc': True, 'fun': False, 'method': False},
            'unk': {'type': 'type', 'basic': 'unknown', 'proc': True, 'fun': False, 'method': False},
            'bool': {'type': 'type', 'basic': 'boolean', 'proc': True, 'fun': True, 'method': True},
            'int': {'type': 'type', 'basic': 'integer', 'proc': True, 'fun': True, 'method': True},
            'str': {'type': 'type', 'basic': 'string', 'proc': True, 'fun': True, 'method': True},
            'list': {'type': 'type', 'basic': 'listing', 'proc': True, 'fun': True, 'method': True},
            'dict': {'type': 'type', 'basic': 'dictionary', 'proc': True, 'fun': True, 'method': True},
            'coll': {'type': 'type', 'basic': 'collection', 'proc': True, 'fun': True, 'method': True},
            'enum': {'type': 'type', 'basic': 'enumeration', 'proc': True, 'fun': True, 'method': True},
            'date': {'type': 'type', 'basic': 'datetime', 'proc': True, 'fun': True, 'method': True},
            'const': {'type': 'type', 'basic': 'constant', 'proc': True, 'fun': False, 'method': False},
            'obj': {'type': 'type', 'basic': 'object', 'proc': True, 'fun': False, 'method': False},
            'set': {'type': 'type', 'basic': 'setting', 'proc': True, 'fun': False, 'method': False},
            'get': {'type': 'type', 'basic': 'getting', 'proc': True, 'fun': False, 'method': False},
            'put': {'type': 'type', 'basic': None, 'proc': True, 'fun': True, 'method': False},
            'puts': {'type': 'type', 'basic': None, 'proc': True, 'fun': True, 'method': False},
            'len': {'type': 'listing', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'find': {'type': 'listing', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'sort': {'type': 'listing', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'index': {'type': 'listing', 'basic': None, 'proc': False, 'fun': False, 'method': True},
            'join': {'type': 'listing', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'replace': {'type': 'listing', 'basic': None, 'proc': False, 'fun': True, 'method': True},
            'range': {'type': 'listing', 'basic': None, 'proc': True, 'fun': True, 'method': False},
            'add': {'type': 'listing', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'revert': {'type': 'valuation', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'not': {'type': 'valuation', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'times': {'type': 'valuation', 'basic': None, 'proc': False, 'fun': True, 'method': True},
            'notnull': {'type': 'valuation', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'isnull': {'type': 'valuation', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'hist': {'type': 'valuation', 'basic': None, 'proc': True, 'fun': False, 'method': True},
            'trim': {'type': 'string', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'split': {'type': 'string', 'basic': None, 'proc': False, 'fun': True, 'method': True},
            'upper': {'type': 'string', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'lower': {'type': 'string', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'getwords': {'type': 'string', 'basic': None, 'proc': False, 'fun': True, 'method': True},
            'getstrings': {'type': 'string', 'basic': None, 'proc': False, 'fun': True, 'method': True},
            'format': {'type': 'string', 'basic': None, 'proc': False, 'fun': True, 'method': True},
            'eql': {'type': 'equal', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'rnd': {'type': 'random', 'basic': None, 'proc': False, 'fun': True, 'method': True},
            'abs': {'type': 'valuation', 'basic': 'abstract', 'proc': True, 'fun': True, 'method': True},
            'def': {'type': 'program', 'basic': None, 'proc': False, 'fun': True, 'method': True},
            'pass': {'type': 'action', 'basic': None, 'proc': True, 'fun': False, 'method': False},
            'max': {'type': 'math', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'min': {'type': 'math', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            'sum': {'type': 'math', 'basic': None, 'proc': True, 'fun': True, 'method': True},
            }

basicValue = {'true', 'false', 'null', 'infinity'}

basicVariable = {'none', 'self'}

reservedWords = [ 'struct', 'char', 'double', 'short', 'auto', 'continue', 'void', 'sizeof', 'typedef',
                  'union', 'unsigned', 'and', 'as', 'assert', 'in', 'is', 'or', 'finally', 'lambda',
                  'from', 'which', 'interface', 'static', 'id', 'delete', 'cast', 'dynamic',
                  'friend', 'operator', 'procedure', 'program', 'library', 'destructor', 'constructor', 'to', 'downto',
                  'database', 'table', 'flow', 'thread', 'do', 'finally', 'append',
                  'new', 'copy', 'setup', 'install', 'export', 'this', 'exception' ]