# -*- coding: utf-8 -*-
from variables import Variable
from operands import clearProcess

if __name__ == '__main__':
    #a = Variable('sr')
    #print(a.dVarSettings)

    while True:
        s = input('Введите код: ')
        print(clearProcess(s))
        print()
