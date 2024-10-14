import nltk
from nltk.tokenize import word_tokenize
from textwrap import dedent

class POS():

    def __repr__(self):
        return f'''
            'POSstr:{self.POSstr}\n'+\
            'Definition:{self.descriptionlst}\n'+\n'''

    def __init__(self, *, POSstr=None, descriptionlst=[]):
        self.POSstr = POSstr if isinstance(POSstr, str) and POSstr != None else ''
        self.hasPOSstr = isinstance(self.POSstr, str) and self.POSstr != ''

        self.descriptionlst = descriptionlst if isinstance(descriptionlst, list) and descriptionlst != set() else set()
        self.hasdescriptionlst = isinstance(self.descriptionlst, set) and self.descriptionlst != list() and all(isinstance(obj, Word) for obj in self.descriptionlst)

class Definition():
    def __repr__(self):
        return f'''
            'definitionstr:{self.definitionlst}\n'+\
            'POSobj:{self.POSobj.__repr__()}\n'+\n'''

    def __init__(self, *, efinitionstr=None, POSobj=None):
        self.POSstr = definitionlst if isinstance(definitionstr, str) and POSstr != None else ''
        self.hasPOSstr = isinstance(self.POSstr, str) and self.POSstr != ''

        self.descriptionlst = descriptionlst if isinstance(descriptionlst, list) and descriptionlst != set() else set()
        self.hasdescriptionlst = isinstance(self.descriptionlst, set) and self.descriptionlst != list() and all(isinstance(obj, Word) for obj in self.descriptionlst)

class Word():
    def __repr__(self):
        return f'''
            'Word:{self.wordstr}\n'+\
            'Definition:{self.definitionobj}\n'+\
            'Definition string:{self.definitionstr}\n'+\
            'Definition List:{self.definitionlst}\n'''

    def __str__(self):
        return f'{self.wordstr}'

    def __init__(self, *, wordstr=None, definitionstr=None, definitionlst=[],posstr=None):
        Compare.__init__(self,sstr=definitionstr, llst=definitionlst)
        self.wordstr = wordstr if isinstance(wordstr, str) else ''
        self.definitionstr = self.sstr
        self.definitionlst = self.llst
        self.posstr = posstr


def main():
    w = Word(wordstr='word', definitionstr='A word', definitionlst=[],posstr='Noun')
    print('Word members\n', w.wordstr, w.definitionstr, w.posstr,'\n')
    print('word string:', str(w),'\n')
    print(f'word repr:\n{w!r}\n')
    p = Phrase(phrasestr='A word', definitionstr='A phrase', definitionlst=[],posstr='Noun')
    print('Phrase members\n', p.phrasestr, p.definitionstr, p.posstr,'\n')
    print('Phrase string:', str(p),'\n')
    print(f'Phrase repr:\n{p!r}\n')


if __name__ == '__main__':
    main()
