# -*- coding: utf-8 -*-
Syntons = []

class Synton(object):
    sType = None
    sName = None
    mVars = []
    mVals = []
    mOpers = []
    mSyntons = []

    def __init__(self, sTyp, sNam):
        self.sType = sTyp
        self.sName = sNam

    def addVal(self, new):
        self.mVals.append(new)

    def addSynton(self, new):
        self.mSyntons.append(new)

    def printSyn(self):
        print(self.sName, self.sType, self.mVars, self.mVals, self.mSyntons)

print("dima, dim2 = person('Дмитрий', 'Анатольевич', 'Поварницын', age=37, sex=MAN)")
syn2 = Synton('fun', 'person')
#syn2.sType = 'fun'
#syn2.mName = 'person'
syn = Synton('simple', None)
#syn.sType = 'simple'
syn.mVars = ['dima', 'dim2']
syn.mVals.append(syn2)
syn.printSyn()

Syntons.append(syn)
