import copy
import nltk
from nltk.text import Text
from nltk.tokenize import word_tokenize
class POS:
    """
    Load,create,edit,save Parts of Speech
    A Part of Speech is the gramatical purpose of a word or phrase in a sentence
    members:
        descriptionstr: a string describing the part of speech
        descriptionlst: an ordered list of SpeechParts objects, 
            which can be either Word objects or 
            Phrase objects that make up the description
        speechpartlst: a list of speechpart objects that are this 
            part of speech observed in corpora
        posstr: a string identifying the part of speech
        
    """
    def isValid(self):
        descriptionlstUnpacked=str()
        for speechpartobj in self.descriptionlst:
            descriptionUnpacked+=str(speechpartobj)
        return self.descriptionstr==descriptionlstUnpacked

    def __init__(self,*,descriptionstr=None,descriptionlst=[],speechpartset=[],posstr=None):
        self.posstr=posstr
        self.descriptionstr=descriptionstr
        self.wordlst=list()
        for speechpartobj in speechpartset:
            self.speechpartlst.append(speechpartobj)
        for speechpartobj in descriptionlst:
            self.descriptionset.append(speechpartobj)

class SpeechPartGroup:
    """
    Load,create,edit,save wordgroups
    A SpeechPartGroup is a group of words or phrases that are interchangeable in some way within a text
    They might be different things that can replace each other and result in a
    gramatical and/or a sensible sentence
    Members:
        descriptionstr: description of the words and phrases that make up this group
        descriptionlst: The list of SpeechPart objects that make up the 
            descriptionstr 
        contextset: the set of context objects where these word objects and phrase 
            objects can be found
        speechpartset: the set of SpeechPart objects in this SpeechPartGroup
    """
    def isValid(self):
        descriptionlstUnpacked=str()
        for speechpartobj in self.descriptionlst:
            descriptionUnpacked+=str(speechpartobj)
        return self.descriptionstr==descriptionlstUnpacked

    def __init__(self,*,descriptionstr= None,descriptionlst=[],\
            contextset=set(),speechpartset=set()):
        self.descriptionstr=descriptionstr
        self.contextset=set()
        for contextobj in contextset:
            self.contextset.add(contextobj)
        self.speechpartset=set()
        for speechpartobj in speechpartset:
            self.speechpartset.add(speechpartobj)
        self.descriptionlst=list()
        for speechpartobj in descriptionlst:
            self.descriptionlst.append(speechpartobj)

class SpeechPart:
    """
    Load,create,edit,save SpeechPart objects
    A SpeechPart is a superclass of Word and Phrase classes
    Senteces are made up of Words and Phrases that each have a specific POS
    Each SpeechPart has a particular meaning and the combinations of meanings 
    related to each other by their Part Of Speech creates the meaning of the 
    sentence
    Members:
        definitionstr The string of its definition
        definitionlst The list of SpeechPart objects making up the definition.
        posstr the string identifying its part of speech
        usageset the set of usage objects that describe where this SpeechPart shows in corpora
    """    
    def isValid(self):
        definitionlstUnpacked=str()
        for speechpartobj in self.definitionlst:
            definitionlstUnpacked+=str(speechpartobj)
        return self.definitionstr==definitionlstUnpacked

    def __init__(self,*,definitionstr=None,definitionlst=[], \
            posstr=None,usageset=set()):
        
        
        self.posstr=posstr
        self.definitionstr=definitionstr
        self.definitionlst=list()
        for speechpartobj in definitionlst:
            definitionlst.append(speechpartobj)
        self.usageset=set()
        for usageobj in usageset:
            self.usageset.add(usageobj)
            
         
                
class Phrase(SpeechPart):
    """
    Load,create,edit,save phrases
    A Part Of speech can be occupied by a series of words or other phrases. 
    Members:
        phrasestr the string representation of the phrase
        phraselst the list of speechpart objects that make up the phrase
        definitionstr the string with the definition of the phrase
        definitionlst the list of speechpart objects that make up the definition.
        posstr the string identifying the part of speech
        usagelist the list of usage objects that describe where this phrase shows up in corpora
    """
    def isValid(self):
        definitionlstUnpacked=str()
        for speechpartobj in self.definitionlst:
            definitionlstUnpacked+=str(speechpartobj)
        phraselstUnpacked=str()
        for speechpartobj in self.phraselst:
            phraselstUnpacked+=str(speechpartobj)
        return self.definitionstr==definitionlstUnpacked and \
            self.phrasestr==phraselstUnpacked

    def __init__(self,*,phrasestr=None,phraselst=[],\
            definitionstr=None,definitionlst=[],\
            usageset=set(),posstr=None):
        self.phrasestr=phrasestr
        self.phraselst=list()
        for speechpartobj in phraselst:
            self.phraselst.append(speechpartobj)
        SpeechPart.__init__(self,posstr=posstr,definitionstr=definitionstr,definitionlst=definitionlst,usageset=usageset)
        
class Word(SpeechPart):
    """
    Load,create,edit,save words
    A Part Of speech can be occupied by a word. 
    Members:
        wordstr the string representation of the phrase
        definitionstr the string with the definition of the phrase
        defiitionlst the list of speechpart objects that make up the definition.
        posstr the string identifying the part of speech
        usageset the set of usage objects that describe where this phrase shows up in corpora
    """
    def __init__(self,*,wordstr=None,\
            definitionstr=None,definitionlst=[],\
            posstr=None,usageset=set()):
        self.wordstr=wordstr
        SpeechPart.__init__(self,posstr=posstr,definitionstr=definitionstr,definitionlst=definitionlst,usageset=usageset)
        
    def __str__(self):
        return f'{self.wordstr}'    
            
class Usage:
    """
    Load,create,edit,save usages
    A usage of a word or phrase describes its context observed in corpora
    A Usage is made up of words, phrases and wordgroups that have particular parts of speech surrounding
    a word or phrase that identify the contexts where the word or phrase occurs and can be used to identify its pos 
    Members:
        corporaobj an object describing the source of the usage of the speechpart for which this is a usage of
        prespeechpartlst the list of speechparts before the speechpart for which this is a usage of
        speechpart the speechpart for which this is a usage of
        postspeechpartlst the list of speechparts after the speechpart for which this is a usage of
        sourcestr the string from the corpora that is the source of this usage
    """
    def isValid(self):
        sourcestrUnpacked=str()
        for speechpartobj in self.prespeechpartlst:
            sourcestrUnpacked+=str(speechpartobj)
        sourcestrUnpacked+=str(self.thisspeechpartobj)
        for speechpartobj in self.postspeechpartlst:
            sourcestrUnpacked+=str(speechpartobj)
        return sourcestrUnpacked==self.sourcestr

    def __init__(self,*,corporaobj=None,prespeechpartlst=[],\
            thisspeechpartobj=None,postspeechpartlst=[],sourcestr=None):
        self.corpora=corporaobj
        self.prespechpartlst=list()
        for speechpartobj in prespeechpartlst:
            self.prespeechpartlst.append(speechpartobj)
        self.thisspeechpartobj=thisspeechpartobj
        for speechpartobj in postspeechpartlst:
            self.postpeechpartlst.append(speechpartobj)
        self.sourcestr=sourcestr
        
class Corpora:
    """
    Load,create,edit,save Corpora 
    A Corpora is a source of text that contain usages of words or phrases within contexts that indicate their POS
    A Corpora usually has a title, author and a host of other metadata
    A Corpora can be represented as a list of SpeechParts
    A Corpora can be represented as a string of text, a list of strings of text.
    A corpora can be stored in a file
    Members:
    corporastr a string representation of the corpora
    corporalst a list of speechparts representing the corpora
    descriptionstr a string describing the corpora
    descriptionlst a list of speechparts that describe the corpora
    namestr a string that identifies the corpora
    metadatastr a string that contains the mettadata for the corpora
    filespec the specitifation of the file containing the corpora
    """        
    def isValid(self):
        descriptionlstUnpacked=str()
        for speechpartobj in self.descriptionlst:
            descriptionlstUnpacked+=str(speechpartobj)
        corporalstUnpacked=str()
        for speechpartobj in self.corporalst:
            phraselstUnpacked+=str(speechpartobj)
        return self.descriptionstr==descriptionlstUnpacked and \
            self.corporastr==corporalstUnpacked

    def __init__(self,*,corporastr=None,corporalst=[],\
            descriptionstr=None,descriptionlst=[],\
            namestr=None,metadatastr=None,filespec=None):
        self.corporastr=corporastr
        self.corporalst=list()
        for speechpartobj in corporalst:
            self.corporalst.append(speechpartobj)
        self.descriptionstr=descriptionstr
        self.descriptionlst=list()
        for speechpartobj in descriptionlst:
            self.descriptionlst.append(speechpartobj)
        self.namestr=namestr
        self.metadatastr=metadatastr
        self.filespec=filespec
            
class Definition:
    """
    Load,create,edit,save definitions
    A definition describes a speechpart which can be a word or phrase.
    A definition would always have a singular part of speech
    Definitions would be related to each other and so the definitions are made up of speechparts
    The speechparts that definitions are made up of can be used to link definitions to other definitions.
    Members:
        definitionstr a string that is the definition
        posstr a string that identifies the part of speech
        posobj a POS object
        definitionlst a list of speechparts that make up the definition
        speechpartset the set of speechparts that have this definition
    """
    def isValid(self):
        definitionlstUnpacked=str()
        for speechpartobj in self.definitionlst:
            definitionlstUnpacked+=str(speechpartobj)
        return self.definitionstr==definitionlstUnpacked

    def __init__(self,*,definitionstr=None,definitionlst=[],\
            posstr=None,speechpartset=set()):
        self.definitionstr=definitionstr
        if definitionlst==[]:
            self.definitionlst=list()
            for token in nltk.tokenize.word_tokenize(self.definitionstr):
                self.definitionlst.append(Word(wordstr=token,definitionstr=None,definitionlst=[],posstr=None,usageset=set()))    
        self.posstr=posstr
        self.speechpartset=set()
        for speechpartobj in speechpartset:
            self.speechpartset.add(speechpartobj)

            
class Dictionary:
    """
    Load, create, update save a dictionary
    A dictionary contains a list of speechpart Objects
    A Dictionary can be loaded from a dictionary file or from a dictionary object or a set
        of speechpart objects
    Members:
        dictionaryfle a file containing a dictionary in JSON format
        dictionaryobj a dictionary object
        speechpartset a set of speechparts that make up a dictionary
    """
    
    def __init__(self,dictionaryfle=None,dictionaryobj=None,speechpartset=set()):
        self.dictioanryfle=dictionaryfle
        self.dictionaryobj=dictionaryobj
        self.speechpartset=set()
        for speechpartobj in speechpartset:
            speechpartset.addspeechpartobj
    
def main():
    w=Word(wordstr='word',definitionstr='A word',definitionlst=[],posstr='noun',usageset=set())
    print(w.wordstr,w.definitionstr,w.posstr)
    p=Phrase(phrasestr='long word',definitionstr='A long word',definitionlst=[],posstr='noun',usageset=set())
    print(p.phrasestr,p.definitionstr,p.posstr)
    d=Definition(definitionstr='A string of text that has no spaces and has a meaning',definitionlst=[],posstr='noun',speechpartset=set())
    print(d.definitionstr)
    print(1)
    w=Word(wordstr=w.wordstr,definitionstr=d.definitionstr,definitionlst=[],posstr='noun',usageset=set())
    print(2)
    print(w.wordstr,w.definitionstr,w.posstr)
    for word in d.definitionlst:
        print(word)
    print(3)
if __name__ == '__main__':
    main()
