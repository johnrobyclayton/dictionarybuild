import copy
import nltk
from nltk.text import Text
from nltk.tokenize import word_tokenize
import csv
import pickle
import os

class Compare:
    """
    Class for comparing lists of SpeechPart object and Strings
    Inherrited by any class that includes a list of SpeechParts and a string that need to match
    PartsOfSpeech include words and phrases. phrases can include words and phrases. Recursion.
    """
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
            self.sstr = ' '.join([wordobj.wordstr for wordobj in self.llst])

        # If no list provided, tokenize the string and create Word objects
        if not self.haslst and self.hasstr:
            self.llst = [Word(wordstr=token) for token in word_tokenize(self.sstr)]

    
    def Matches(self):
        stringfromlst=str()
        for wordobj in self.llst:
            if isinstance(wordobj,Word):
                if len(stringfromlst)>0:
                    stringfromlst+=' '
                stringfromlst+=wordobj.wordstr                
        return self.sstr==stringfromlst

class ComparePOS:
    def __init__(self, *, sstr=None, llst=[]):
        # Initialize self.sstr and self.llst early
        self.sstr = sstr if isinstance(sstr, str) and sstr != None else ''
        self.llst = llst if isinstance(llst, list) and llst != [] else []

        # Check if sstr is a valid string
        self.hasstr = isinstance(self.sstr, str) and self.sstr != ''
        # Check if llst is a valid list and contains only Word objects
        self.haslst = isinstance(self.llst, list) and self.llst != [] and all(isinstance(obj, POS) for obj in self.llst)
        # If no string provided, create it from the list
        if not self.hasstr and self.haslst:
            self.sstr = ' '.join([posobj.posstr for posobj in self.llst])

        # If no list provided, tokenize the string and create Word objects
        if not self.haslst and self.hasstr:
            self.llst = [POS(posstr=token) for token in word_tokenize(self.sstr)]

    
    def Matches(self):
        stringfromlst=str()
        for posobj in self.llst:
            if isinstance(posobj,POS):
                if len(stringfromlst)>0:
                    stringfromlst+=' '
                stringfromlst+=posobj.posstr                
        return self.sstr==stringfromlst




class Grammar:
    """
    Store the equivalencies between Parts Of speech and Parts Of Speech Phrases
    Adjective Noun can be replaced with Noun and if the string containing Adjective Noun is grammatical then the string with Noun is also grammatical
    A list of such replacements can be observed in Corpora
    This is anologous su synonym and synonym phrases. Example dog <=> canis familiaris <=> thing that is commonly known to chase cats
    Members:
        POSPhrase a POSPhrase observed in corpora
        PartOfGrammarlst a list of POS and POSPhrases that can replace this POSPhrase
        
    """
    pass

class PartOfGrammar:
    """
    Superclass for POS and POSPhrase.
    Anologous to PartOfSpeech being a superclass of Word and Phrase
    Members:
        posstr the string identifying its part of speech
        usageset the set of usage objects that describe where this grammar object shows in corpora
    """    
    
            
    def __init__(self,*,definitionstr=None,definitionlst=[], \
            usageset=set(),dictionary=None):
        Compare.__init__(self,sstr=definitionstr,llst=definitionlst)
        self.definitionstr=self.sstr
        self.definitionlst=self.llst
        self.definitionMatches=Compare.Matches(self)

        self.partofgrammarstr=str()

        self.usageset = usageset if isinstance(usageset, set) and usageset != set() else set()
        self.hasusageset = isinstance(self.usageset, set) and self.usageset != set() and all(isinstance(obj, Usage) for obj in self.usageset)



class POSPhrase(PartOfGrammar,ComparePOS,Compare):
    """
    Store sequences of Parts Of Speech observed in Corpora
    For example: "The cat sat on the mat" woul becoem:
    "article noun verb positional article noun"
    "article noun" would be very common
    Examples:
    The cat
    a dog
    this house
    that car
    your hat
    our home
    his shirt
    her shoes
    their ball
    Members:
        posphrasestr a string of the POS strings that make up the POSPhrase
            Examples: 'Article Noun Verb Preposition Article Noun" which is the POSPhrase for 
            "The cat sat on the mat" 
        posphraselst a list of POS objects that make up the posphrase
        descriptionstr: a string describing the part of speech phrase
        descriptionlst: an ordered list of Word objects that make up the description,         
        speechpartset the set of speechparts that demonstrates this POSPhrase in Corpora 
        usageset the set of examples in corpora, each usage would point to the appropriate corpora
    """
    def __repr__(self,depth):
        if depth>0:
            depth-=1
            return f"POSPhrase:{{"+\
                f"posphrasestr:'{self.posphrasestr}',"+\
                f"posphraselst:["+", ".join([word.__repr__(depth) for word in self.definitionlst])+"],"+\
                f"descriptionstr:'{self.definitionstr}',"+\
                f"descriptionlst:["+", ".join([word.__repr__(depth) for word in self.descriptionlst])+"],"+\
                f"usageset:("+", ".join([usage.__repr__(depth) for usage in self.usageset])+")"+\
                f"}}"
        else:
            return f"POSPhrase:{{"+\
                f"posphrasestr:'{self.posphrasestr}',"+\
                f"descriptionstr:'{self.descrptionstr}',"+\
                f"}}"
            
            
            
    def __str__(self):
        return f'{self.posphrasestr}'    

    def __init__(self,*,posphrasestr=None,posphraselst=[],descriptionstr=None,descriptionlst=[],speechpartset=set(),usageset=set()):


        ComparePOS.__init__(self,sstr=posphrasestr,llst=posphraselst)
        self.posphrasestr=self.sstr
        self.posphraselst=self.llst
        self.posphraseMatches=ComparePOS.Matches(self)

        self.hasposphrasestr = isinstance(self.posphrasestr, str) and self.posphrasestr != ''
        if self.posphrasestr:
            super().partofgrammarstr=self.posphrasestr
        
        Compare.__init__(self,sstr=descriptionstr,llst=descriptionlst)
        self.descritionstr=self.sstr
        self.descriptionlst=self.llst
        self.descritionMatches=Compare.Matches(self)

        self.usageset = usageset if isinstance(usageset, set) and usageset != set() else set()
        self.hasusageset = isinstance(self.usageset, set) and self.usageset != set() and all(isinstance(obj, Usage) for obj in self.usageset)

        self.speechpartset = speechpartset if isinstance(speechpartset, set) and speechpartset != set() else set()
        self.hasspeechpartset = isinstance(self.speechpartset, set) and self.speechpartset != set() and all(isinstance(obj, SpeechPart) for obj in self.speechpartset)




class POS(Compare):
    """
    Load,create,edit,save Parts of Speech
    A Part of Speech is the gramatical purpose of a word or phrase in a sentence
    members:
        descriptionstr: a string describing the part of speech
        descriptionlst: an ordered list of SpeechParts objects, 
            which can be either Word objects or 
            Phrase objects that make up the description
        speechpartset: a set of speechpart objects that are this 
            part of speech observed in corpora
        posstr: a string identifying the part of speech
        
    """

    def __repr__(self,depth):
        if depth>0:
            depth-=1
            return f"POS:{{"+\
                f"posstr:'{self.posstr}',"+\
                f"descriptionstr:'{self.definitionstr}',"+\
                f"descriptionlst:["+", ".join([word.__repr__(depth) for word in self.descriptionlst])+"],"+\
                f"speechpartset:("+", ".join([speechpart.__repr__(depth) for speechpart in self.speechpartset])+")"+\
                f"usageset:("+", ".join([usage.__repr__(depth) for usage in self.usageset])+")"+\
                f"}}"
        else:
            return f"POS:{{"+\
                f"posstr:'{self.posstr}',"+\
                f"descriptionstr:'{self.descrptionstr}',"+\
                f"}}"
            
            
            
    def __str__(self):
        return f'{self.posstr}'    

    def __init__(self,*,descriptionstr=None,descriptionlst=[],speechpartset=set(),posstr=None):

        Compare.__init__(self,sstr=descriptionstr,llst=descriptionlst)
        self.descriptionstr=self.sstr
        self.descriptionlst=self.llst
        self.descriptionMatches=Compare.Matches(self)

        self.posstr = posstr if isinstance(posstr, str) and posstr != None else ''
        self.hasposstr = isinstance(self.posstr, str) and self.posstr != ''
        if self.hasposstr:
            super().partofgrammarstr=self.posstr


        self.speechpartset = speechpartset if isinstance(speechpartset, set) and speechpartset != set() else set()
        self.hasspeechpartset = isinstance(self.speechpartset, set) and self.speechpartset != set() and all(isinstance(obj, SpeechPart) for obj in self.speechpartset)



class SpeechPartGroup(Compare):
    """
    Load,create,edit,save wordgroups
    A SpeechPartGroup is a group of words or phrases that are interchangeable in some way within a text
    They might be different things that can replace each other and result in a
    gramatical and/or a sensible sentence
    Members:
        descriptionstr: description of the words and phrases that make up this group
        descriptionlst: The list of SpeechPart objects that make up the 
            descriptionstr 
        usageset: the set of context objects where these word objects and phrase 
            objects can be found
        speechpartset: the set of SpeechPart objects in this SpeechPartGroup
    """

    def __repr__(self,depth):
        if depth>0:
            depth-=1
            return f"SpeechPartGroup:{{"+\
                f"descriptionstr:'{self.descriptionstr}',"+\
                f"descriptionlst:["+", ".join([word.__repr__(depth) for word in self.descriptionlst])+"],"+\
                f"usageset:("+", ".join([usage.__repr__(depth) for usage in self.usageset])+")"+\
                f"speechpartset:("+", ".join([speechpart.__repr__(depth) for speechpart in self.speechpartset])+")"+\
                f"}}"
        else:
            return f"SpeechPartGroup:{{"+\
                f"descriptionstr:'{self.descriptionstr}',"+\
                f"}}"
                        
    def __str__(self):
        return f'{self.descriptionstr}'    

    def __init__(self,*,descriptionstr= None,descriptionlst=[],\
            usageset=set(),speechpartset=set()):
        Compare.__init__(self,sstr=descriptionstr,llst=descriptionlst)
        self.descriptionstr=self.sstr
        self.descriptionlst=self.llst
        self.descriptionMatches=Compare.Matches(self)
        
        self.speechpartset = speechpartset if isinstance(speechpartset, set) and speechpartset != set() else set()
        self.hasspeechpartset = isinstance(self.speechpartset, set) and self.speechpartset != set() and all(isinstance(obj, SpeechPart) for obj in self.speechpartset)

        self.usageset = usageset if isinstance(usageset, set) and usageset != set() else set()
        self.hasusageset = isinstance(self.usageset, set) and self.usageset != set() and all(isinstance(obj, Usage) for obj in self.usageset)



class SpeechPart(Compare):
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
    
            
    def __init__(self,*,definitionstr=None,definitionlst=[], \
            partofgrammarstr=None,usageset=set(),dictionary=None):
        Compare.__init__(self,sstr=definitionstr,llst=definitionlst)
        self.definitionstr=self.sstr
        self.definitionlst=self.llst
        self.definitionMatches=Compare.Matches(self)

        self.partofgrammarstr = partofgrammarstr if isinstance(partofgrammarstr, str) and partofgrammarstr != None else ''
        self.haspartofgrammarstr = isinstance(self.partofgrammarstr, str) and self.partofgrammarstr != ''

        self.usageset = usageset if isinstance(usageset, set) and usageset != set() else set()
        self.hasusageset = isinstance(self.usageset, set) and self.usageset != set() and all(isinstance(obj, Usage) for obj in self.usageset)

        self.dictionary = dictionary if isinstance(dictionary, Dictionary) and dictionary != None else None
        self.hasdictionary = isinstance(self.dictionary, Dictionary) and self.dictionary != None


class Phrase(SpeechPart,Compare):
    """
    Load,create,edit,save phrases
    A Part Of speech can be occupied by a series of words or other phrases. 
    Members:
        phrasestr the string representation of the phrase
        phraselst the list of word objects that make up the phrase
        definitionstr the string with the definition of the phrase
        definitionlst the list of speechpart objects that make up the definition.
        posstr the string identifying the part of speech
        usagelist the list of usage objects that describe where this phrase shows up in corpora
        
    """

    def __repr__(self,*,depth=0):
        if depth>0:
            depth-=1
            return f"Phrase:{{"+\
                f"phrasestr:'{self.phrasestr}',"+\
                f"phraselst:"+", [[".join([word.__repr__(depth) for word in self.phraselst])+f"]]"+\
                f"definitionstr:'{self.definitionstr}',"+\
                f"definitionlst:["+", ".join([word.__repr__(depth) for word in self.definitionlst])+"],"+\
                f"posstr:'{self.partofgrammarstr}',"+\
                f"usageset:("+", ".join([usage.__repr__(depth) for usage in self.usageset])+")"+\
                f"}}"
        else:
            return f"Phrase:{{"+\
                f"phrasestr:'{self.phrasestr}',"+\
                f"definitionstr:'{self.definitionstr}',"+\
                f"partofgrammarstr:'{self.partofgrammarstr}'"+\
                f"}}"
            
    def __str__(self):
        return f'{self.phrasestr}'    

    def __init__(self,*,phrasestr=None,phraselst=[],definitionstr=None,definitionlst=[],usageset=set(),partofgrammarstr=None,dictionary=None):
        SpeechPart.__init__(self,definitionstr=definitionstr,definitionlst=definitionlst,partofgrammarstr=partofgrammarstr,usageset=usageset,dictionary=dictionary)
        Compare.__init__(self,sstr=phrasestr,llst=phraselst)
        self.phrasestr=self.sstr
        self.phraselst=self.llst
        self.phraseMatches =Compare.Matches(self)

        Compare.__init__(self,sstr=definitionstr,llst=definitionlst)
        self.definitionstr=self.sstr
        self.definitionlst=self.llst
        self.definitionMatches =Compare.Matches(self)
        
        




class Word(SpeechPart,Compare):
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
    def __repr__(self,depth=0):
        if depth>0:
            depth-=1
            return f"Word:{{"+\
                f"wordstr:'{self.wordstr}',"+\
                f"definitionstr:'{self.definitionstr}',"+\
                f"definitionlst:["+", ".join([word.__repr__(depth) for word in self.definitionlst])+"],"+\
                f"partofgrammarstr:'{self.partofgrammarstr}',"+\
                f"usageset:("+", ".join([usage.__repr__(depth) for usage in self.usageset])+")"+\
                f"}}"
        else:
            return f"Word:{{"+\
                f"wordstr:'{self.wordstr}',"+\
                f"definitionstr:'{self.definitionstr}',"+\
                f"partofgrammarstr:'{self.partofgrammarstr}'"+\
                f"}}"
            
    def __str__(self):
        return f'{self.wordstr}'    

    def __init__(self,*,wordstr=None,definitionstr=None,definitionlst=[],partofgrammarstr=None,usageset=set(),dictionary=None):
        SpeechPart.__init__(self,partofgrammarstr=partofgrammarstr,definitionstr=definitionstr,definitionlst=definitionlst,usageset=usageset,dictionary=None)
        Compare.__init__(self,sstr=definitionstr,llst=definitionlst)
        self.definitionstr=self.sstr
        self.definitionlst=self.llst
        self.definitionMatches =Compare.Matches(self)
        

        self.wordstr = wordstr if isinstance(wordstr, str) and wordstr != None else ''
        self.haswordstr = isinstance(self.wordstr, str) and self.wordstr != ''
        
        self.dictionary = dictionary if isinstance(dictionary, Dictionary) and dictionary != None else None
        self.hasdictionary = isinstance(self.dictionary, Dictionary) and self.dictionary != None

        if self.hasdictionary:
            if self not in dictionary.speechpartset:
                dictionary.speechpartset.add(self)
            



class Usage:
    """
    Load,create,edit,save usages
    A usage of a word or phrase describes its context observed in corpora
    A Usage is made up of words, phrases and wordgroups that have particular parts of speech surrounding
    a word or phrase that identify the contexts where the word or phrase occurs and can be used to identify its pos 
    Members:
        corporaobj an object describing the source of the usage of the word object for which this is a usage of
        prewordlst the list of word objects before the word object for which this is a usage of
        wordobj the word object for which this is a usage of
        postwordlst the list of word objects after the word object for which this is a usage of
        sourcestr the string from the corpora that is the source of this usage
    """

    def __repr__(self,depth):
        if depth>0:
            depth-=1
            return f"Usage:{{"+\
                f"corporaobj:'{self.corporaobj.__repr__()}',"+\
                f"prespeechpartlst:["+", ".join([word.__repr__(depth) for word in self.prespeechpartlst])+"],"+\
                f"thisspeechpartobj:'{self.thisspeechpartobj.__repr__(depth)}',"+\
                f"postspeechpartlst:["+", ".join([word.__repr__(depth) for word in self.postspeechpartlst])+"],"+\
                f"sourcestr:'{self.sourcestr}',"+\
                f"}}"
        else:
            return f"Usage:{{"+\
                f"corporaobj:'{self.corporaobj.__repr__()}',"+\
                f"sourcestr:'{self.sourcestr}',"+\
                f"}}"
            
    def __str__(self):
        return f'{self.sourcestr}'    

    def __init__(self,*,corporaobj=None,prewordlst=[],thiswordobj=None,postwordlst=[],sourcestr=None):

        self.corporaobj = corporaobj if isinstance(corporaobj, Corpora) and corporaobj != None else None
        self.hascorporaobj = isinstance(self.corporaobj, Corpora) and self.corporaobj != None


        self.prewordlst=list()
        for wordobj in prewordlst:
            self.prewordlst.append(wordobj)

        self.thiswordobj=thiswordobj

        for wordobj in postwordlst:
            self.postwordlst.append(wordobj)
        self.sourcestr=sourcestr
        




class Corpora(Compare):
    """
    Load,create,edit,save Corpora 
    A Corpora is a source of text that contain usages of words or phrases within contexts that indicate their POS
    A Corpora usually has a title, author and a host of other metadata
    A Corpora can be represented as a list of SpeechParts
    A Corpora can be represented as a string of text, a list of strings of text.
    A corpora can be stored in a file
    A Corpora would not be a large size. Maximum 100kB. A book made up of Chapters. A Chapter would be a single Corpora.
        A Corpora only needs to be large enough to provide enough information to unambibuously identify the meaning of each word or phrase. 
    Members:
    corporastr a string representation of the corpora
    corporalst a list of speechparts representing the corpora
    descriptionstr a string describing the corpora
    descriptionlst a list of speechparts that describe the corpora
    namestr a string that identifies the corpora
    metadatastr a string that contains the mettadata for the corpora
    filespec the specitifation of the file containing the corpora
    """        

    def __repr__(self,depth):
        if depth>0:
            depth-=1
            return f"Corpora:{{"+\
                f"namestr:'{self.namestr}',"+\
                f"metadatastr:'{self.metadatastr}',"+\
                f"descriptionstr:'{self.descriptionstr}',"+\
                f"descriptionlst:["+", ".join([word.__repr__(depth) for word in self.descriptionlst])+"],"+\
                f"corporastr:'{self.corporastr}',"+\
                f"corporalst:["+", ".join([word.__repr__(depth) for word in self.corporalst])+"],"+\
                f"filespec:'{self.filespec.__repr__()}',"+\
                f"}}"
        else:
            return f"Corpora:{{"+\
                f"namestr:'{self.namestr}',"+\
                f"metadatastr:'{self.metadatastr}',"+\
                f"descriptionstr:'{self.descriptionstr}',"+\
                f"corporastr:'{self.corporastr}',"+\
                f"filespec:'{self.filespec.__repr__()}',"+\
                f"}}"
            


            
    def __str__(self):
        return f'{self.namestr}'    

    def __init__(self,*,corporastr=None,corporalst=[],descriptionstr=None,descriptionlst=[],namestr=None,metadatastr=None,filespec=None):


        Compare.__init__(self,sstr=descriptionstr,llst=descriptionlst)
        self.descriptionstr=self.sstr
        self.descriptionlst=self.llst
        self.descriptionMatches =Compare.Matches(self)



        Compare.__init__(self,sstr=corporastr,llst=corporalst)
        self.corporastr=self.sstr
        self.corporalst=self.llst
        self.corporaMatches =Compare.Matches(self)

        self.namestr = namestr if isinstance(namestr, str) and namestr != None else ''
        self.hasnamestr = isinstance(self.namestr, str) and self.namestr != ''

        self.matadatastr = metadatastr if isinstance(metadatastr, str) and metadatastr != None else ''
        self.hasmetadatastr = isinstance(self.metadatastr, str) and self.metadatastr != ''
        
        #self.filespec = filespec if isinstance(filespec, Filespec) and filespec != None else None
        #self.hasfilespec = isinstance(self.filespec, Filespec) and self.filespec != None

            




class Definition(Compare):
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
    def __repr__(self,depth):
        if depth>0:
            depth-=1
            return f"Word:{{"+\
                f"definitionstr:'{self.definitionstr}',"+\
                f"definitionlst:["+", ".join([word.__repr__(depth) for word in self.definitionlst])+"],"+\
                f"partofgrammarstr:'{self.partofgrammarstr}',"+\
                f"speechpartset:("+", ".join([usage.__repr__(depth) for usage in self.speechpartset])+")"+\
                f"}}"
        else:
            return f"Word:{{"+\
                f"definitionstr:'{self.definitionstr}',"+\
                f"partofgrammarstr:'{self.partofgrammarstr}'"+\
                f"}}"
            

    def __repr__(self):
        return f'Definition:{self.definitionstr}\
            \nPart Of Speech:{self.partofgrammarstr}'
            
    def __str__(self):
        return f'{self.definitionstr}'    

    def __init__(self,*,definitionstr=None,definitionlst=[],\
            partofgrammarstr=None,speechpartset=set()):
        Compare.__init__(self,sstr=definitionstr,llst=definitionlst)
        self.definitionstr=self.sstr
        self.definitionlst=self.llst
        self.definitionMatches =Compare.Matches(self)
        
        self.partofgrammarstr = partofgrammarstr if isinstance(partofgrammarstr, str) and partofgrammarstr != None else ''
        self.haspartofgrammarstr = isinstance(self.partofgrammarstr, str) and self.partofgrammarstr != ''

        self.speechpartset = speechpartset if isinstance(speechpartset, set) and speechpartset != set() else set()
        self.hasspeechpartset = isinstance(self.speechpartset, set) and self.speechpartset != set() and all(isinstance(obj, SpeechPart) for obj in self.speechpartset)

        self.defindint=int()
        
    def definitionContains(self,str):
        return str in self.definitionstr 

                
                
            



class Dictionary:
    """
    Load, create, update save a dictionary
    A dictionary contains a list of definition Objects
    Each definition object contains its POS object and a set of Word Objects.
    From this a ditionary of Word Objects linked to Definition object-POS object pairs can be generated
    A Grammar object contains a POSPhrase objects and a list of POSPhrase or POS objects it can be replaced with
    Each POSPhrase is a string of POS objects observed in Corpora
    Each Corpora is made up of a list of Word objects that link to the Dictionary Definition-POS pairs
    A Dictionary can be loaded from a dictionary file or from a dictionary object or a set
        of speechpart objects
    Members:
        dictionaryfle a file containing a dictionary in JSON format
        dictionaryobj a dictionary object
        definitionsset a set of definitions
        speechpartset a set of speechparts that make up a dictionary
    """
    def __repr___(self,depth=0):
        if depth>0:
            depth-=1
            return f"Word:{{"+\
                f"dictionaryfle:'{self.dictionaryfle}',"+\
                f"speechpartset:("+", ".join([speechpart.__repr__(depth) for speechpart in self.speechpartset])+")"+\
                f"posset:("+", ".join([POS.__repr__(depth) for POS in self.posset])+")"+\
                f"posphraseset:("+", ".join([POSPhrase.__repr__(depth) for POSPhrase in self.posphraseset])+")"+\
                f"gammarset:("+", ".join([Grammar.__repr__(depth) for Grammar in self.grammarset])+")"+\
                f"definitionstr:'{self.definitionstr}',"+\
                f"definitionlst:["+", ".join([word.__repr__(depth) for word in self.definitionlst])+"],"+\
                f"posstr:'{self.posstr}',"+\
                f"}}"
        else:
            return f"Word:{{"+\
                f"wordstr:'{self.wordstr}',"+\
                f"definitionstr:'{self.definitionstr}',"+\
                f"posset:("+", ".join([POS.__repr__(depth) for POS in self.posset])+")"+\
                f"posstr:'{self.posstr}'"+\
                f"speechpartset:("+", ".join([speechpart.__repr__(depth) for speechpart in self.speechpartset])+")"+\
                f"}}"
                
    def listSpeechPartEntries(self):
        #entry=set()
        #for speechpart in self.speechpartset:
        #    entry.add(speechpart.)
        wordentries=[(entry.wordstr,entry.posstr) for entry in self.speechpartset if isinstance(entry,Word)]
        phraseentries=[(entry.phrasestr,entry.posstr) for entry in self.speechpartset if isinstance(entry,Phrase)]
        return(sorted(wordentries+phraseentries))

    def addSpeechPartEntry(self,speechpart):
        """
        Add a speechpart to the dictionary.
        Args:
            speechpart (Speechpart): A word or phrase that can occupy a part of speech and has a meaning 
        """
        if isinstance(speechpart, SpeechPart):
            self.speechpartset.add(speechpart)
    
    def __init__(self,*,dictionaryfle=None,definitionset=set(),posset=set(),posphraseset=set(),grammarset=set(),speechpartset=set()):
        
        self.dictioanryfle=dictionaryfle
        
        self.speechpartset = speechpartset if isinstance(speechpartset, set) and speechpartset != set() else set()
        self.hasspeechpartset = isinstance(self.speechpartset, set) and self.speechpartset != set() and all(isinstance(obj, SpeechPart) for obj in self.speechpartset)

        self.definitionset = definitionset if isinstance(definitionset, set) and definitionset != set() else set()
        self.hasdefinitionset = isinstance(self.definitionset, set) and self.definitionset != set() and all(isinstance(obj, Definition) for obj in self.definitionset)


        self.posset = posset if isinstance(posset, set) and posset != set() else set()
        self.hasposset = isinstance(self.posset, set) and self.posset != set() and all(isinstance(obj, POS) for obj in self.posset)

        self.posphraseset = posphraseset if isinstance(posphraseset, set) and posphraseset != set() else set()
        self.hasposphraseset = isinstance(self.posphraseset, set) and self.posphraseset != set() and all(isinstance(obj, POSPhrase) for obj in self.usageset)

    def loadDefinitions_csv(self):
        with open('dictionary/OPTED-dictionary.csv',newline='\n') as csvfile:
            definitionreader = csv.reader(csvfile, dialect="excel",delimiter=',',quotechar='"')
            #for word,count,pos,definition in definitionreader:
            for line in definitionreader:
                if len(line)==4:
                    #create a speechpartset to hold the words or phrases that head the dictionary entries
                    speechpartset=set()
                    #for each entry in the dictionary add the word, part of speech and definition to the speechpartset full of Word objects 
                    speechpartset.add(Word(wordstr=line[0],partofgrammarstr=line[2],definitionstr=line[3]))
                    #for each entry in the dictionary add a definition along with the part of speech and the word or phrase connected to the entry
                    self.definitionset.add(Definition(definitionstr=line[3],partofgrammarstr=line[2],speechpartset=speechpartset))
                    #add the speechpartset generated from an entry to the accumulating speechpartset in the dictionary
                    self.speechpartset=self.speechpartset.union(speechpartset)
                    
    def saveDefinitions_pickle(self):
        filehandler=open("dictionary/dictionaryobj.pkl","wb")
        pickle.dump(self,filehandler)
    
    def loadDefinition_pickle():
        filehandler=open("dictionary/dictionaryobj.pkl","rb")
        return pickle.load(filehandler)
        
    def selectADefinition(self,*,definitionlst=[]):
        for definition in definitionlst:
            if isinstance(definition,Definition):
                print(f''+\
                      f'Definition ident: {definition.defindint} \n'+\
                      f'Definition POS: {definition.partofgrammarstr} \n'+\
                      f'Definition string: {definition.definitionstr} \n'
                    )
        print('Enter an Definitioin ident to edit:')
        ident=input()
        editDefinition=Definition()
        for definition in definitionlst:
            if isinstance(definition, Definition):
                if definition.defindint==ident:
                    editDefinition=definition
        return editDefinition
        
    def investigate(self):
        cont=True
        while cont:
            print('Enter selection')
            print('Enter a word to find a dictionary entry for that word 1')
            print('Enter a word to find dictionary entries with the word in the definition 2')
            print('Enter a number to find a dictionary entry with that index 3')
            print('quit q')
            command = input()
            definitioneditlist=list()
            if command == '1':
                print('Enter a word')
                inputstr= input()
                for definition in self.definitionset:
                    if isinstance(definition,Definition):
                        if inputstr in definition.definitionstr:
                            definitioneditlist.append(definition)
                selecteddefinitioin=self.selectADefinition(definitionlst=definitioneditlist)
                print(selecteddefinitioin.definitionstr)
            elif command == '2':
                inputstr= input()
            elif command == '3':
                inputint= int(input())
            elif command == 'q':
                cont=False
            else:
                print('invalid selection, q to quit')







def main():
    #c=Compare(sstr='a aa aaa b bb bbb',llst=['a','aa','aaa','b','bb','bbb'])
    #print
    d=Dictionary(dictionaryfle=None,speechpartset=None)
    #w=Word(wordstr='word',definitionstr='A word',definitionlst=[],partofgrammarstr='Noun',usageset=set(),dictionary=d)
    #print('d',d.entries())
    #print('Word members\n',w.wordstr,w.definitionstr,w.partofgrammarstr)
    #print('word string:',str(w))
    #print(f'word repr:\n{w.__repr__(1)}')
    #print(w.definitionMatches)
    #print(d.__repr__())
    d.loadDefinitions_csv()
    #print(len(d.definitionset))
    #d.saveDefinitions_pickle()
    #1del(d)
    #d=Dictionary()
    #d=Dictionary.loadDefinition_pickle()
    #d.investigate()
    index=0
    if isinstance(d,Dictionary):
        print(len(d.definitionset))
        for definition in d.definitionset:
            if isinstance(definition,Definition):
                index+=1
                definition.defindint=index
    d.saveDefinitions_pickle()
    #d=Dictionary.loadDefinition_pickle()
    #d.investigate()
    #d.saveDefinitions_pickle()
                    
    #print(len(d.speechpartset))
    #p=Phrase(phrasestr='long word',definitionstr='A long word',definitionlst=[],posstr='noun',usageset=set())
    #print(p.phrasestr,p.definitionstr,p.posstr)
    #d=Definition(definitionstr='A string of text that has no spaces and has a meaning',definitionlst=[],posstr='noun',speechpartset=set())
    #print(d.definitionstr)
    #w=Word(wordstr=w.wordstr,definitionstr=d.definitionstr,definitionlst=[],posstr='noun',usageset=set())
    #print(w.wordstr,w.definitionstr,w.posstr)
    #for word in d.definitionlst:
    #    pass
        #print(word)
if __name__ == '__main__':
    main()
