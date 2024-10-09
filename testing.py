import nltk
from nltk.tokenize import word_tokenize
from textwrap import dedent

class Compare:
    def __init__(self, *, sstr=None, llst=[]):
        # Initialize self.sstr and self.llst early
        self.sstr = sstr if isinstance(sstr, str) and sstr != None else ''
        self.llst = llst if isinstance(llst, list) and llst != [] else []

        # Check if sstr is a valid string
        self.hasstr = isinstance(self.sstr, str) and self.sstr != ''
        # Check if llst is a valid list and contains only Word objects
        self.haslst = isinstance(self.llst, list) and self.llst != [] and all(isinstance(obj, Word) for obj in self.llst)
        # If no string provided, create it from the list
        if not self.hasstr and self.haslst:
            self.sstr = ' '.join([speechpartobj.wordstr for speechpartobj in self.llst])

        # If no list provided, tokenize the string and create Word objects
        if not self.haslst and self.hasstr:
            self.llst = [Word(wordstr=token) for token in word_tokenize(self.sstr)]


class Phrase(Compare):
    def __repr__(self):
        return f''+\
            'Phrase:{self.phrasestr}\n'+\
            'Part Of Speech:{self.posstr}\n'+\
            'Definition String:{self.definitionstr}\n'+\
            'Definition List:{self.definitionlst}\n'

    def __str__(self):
        return f'{self.phrasestr}'    

    def __init__(self, *, phrasestr=None, phraselst=[], definitionstr=None, definitionlst=[],posstr=None):
        Compare.__init__(self,sstr=phrasestr, llst=phraselst)
        self.phrasestr = self.sstr
        self.phraselst = self.llst
        Compare.__init__(self,sstr=definitionstr, llst=definitionlst)
        self.definitionstr = self.sstr
        self.definitionlst = self.llst
        self.posstr = posstr


class Word(Compare):
    def __repr__(self):
        return f'''
            'Word:{self.wordstr}\n'+\
            'PartOfSpeech:{self.posstr}\n'+\
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
