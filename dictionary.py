class POS:
    """
    Load,create,edit,save Parts of Speech
    A Part of Speech is the gramatical purpose of a word or phrase in a sentence
    members:
        posstr: a string identifying the part of speech
        descriptionstr: a string describing the part of speech
        descriptionlst: a list of Word objects and Phrase objects that make up the description
        wordlst: a list of Word objects that are this part of speech observed in corpora
        phraselst: a likst of Phrase objects that are this part of speech observed in corpora
    """
    def __init__(self,posstr,descriptionstr,wordlst=[],phraselst=[],descriptionlst=[]):
        self.posstr=posstr
        self.descriptionstr=descriptionstr
        self.wordlst=list()
        for wordobj in wordlst:
            self.wordlst.append(wordobj)
        for phraseobj in phraselst:
            self.phraselst.append(phraseobj)
        for descriptionobj in descriptionlst:
            self.descriptionlst.append(descriptionobj)

class WordPhraseGroup:
    """
    Load,create,edit,save wordgroups
    A Wordgroup is a group of words that are interchangeable in some way within a text
    They might be different things that can replace each other and result in a
    gramatical and/or a sensible sentence
    Members:
        posobj: POS object identifying a part of speech
        descriptionstr: description of the words and phrases that make up this group
        contextlst: the list of context objects where these word objects and phrase 
            objects can be found
        wordlst: the list of Word objects in this WordPhraseGroup
        phraselst: the list of Phrase objects in this WordPhraseGroup
        descriptionlst: The list of Word objects and Phrase objects that make up the 
            descriptionstr 
    """
    def __init__(self,posobj,descriptionstr,contextlst=[],wordlst=[],phraselst=[],descriptionlst=[]):
        self.posobj=posobj
        self.descriptionstr=descriptionstr
        self.wordlst=list()
        for wordobj in wordlst:
            self.wordlst.append(wordobj)
        for phraseobj in phraselst:
            self.wordlst.append(phraseobj)
        for descriptionobj in descriptionlst:
            self.descriptionlst.append(descriptionobj)

class SpeechPart:
    """
    Load,create,edit,save SpeechPart objects
    A SpeechPart is a superclass of Word and Phrase classes
    Senteces are made up of Words and Phrases that each have a specific POS
    Each SpeechPart has a particular meaning and the combinations of meanings 
    related to each other by their Part Of Speech creates the meaning of the 
    sentence
    """    
    def __init__(self, posstr=None,posobj=None,definitionstr=None,definitionlst=[],usagelst=[]):
        
        self.posstr=posstr
        self.posobj=posobj
        self.definitionstr=definitionstr
        self.definitionlst=list()
         
                
class Phrase:
    """
    Load,create,edit,save phrases
    A Part Of speech can be occupied by a series of words or other phrases. 
    """
    def __init__(self,phrasestr,posstr,definitionstr,phraselst=[],definitionlst=[],usagelst=[]):
        self.phraselst=list()
        for phrasetkn in phraselst:
            self.phraselst.append(phrasetkn)
        self.definitionlst=list()
        for definitiontkn in definitionlst:
            self.definitionlst.append(definitiontkn)
        
        
    
            
class Usage:
    """
    Load,create,edit,save usages
    A usage of a word describes its context observed in corpora
    A Usage is made up of words, phrases and wordgroups that have particular parts of speech surrounding
    a word that identify the contexts where the word occurs and can be used to identify its pos 
    """
    def __init__(self,usagelst,sourcestr,sourcedescriptionstr):
        self.usagelst=list()
        
        
        
        
            
class Definition:
    """Load,create,edit,save definitions"""
    def __init__(self,definitionstr,posstr,wordlst=[]):
        self.definitionstr-definitionstr
        self.posstr=posstr
        self.wordlst=list()
        for wordstr in wordlst:
            self.wordlst.append(wordstr)

class Word:
    """Load,create,edit,save a word"""
    def __init__(self,wordstr,posstr,definitionstr,usagestr,usagelst=[],definitionlst=[]):
        self.wortstr=wordstr
        self.posstr=posstr
        self.definition=definitionstr
        self.usagelst=list()
        for usagestr in usagelst:
            self.usagelst.append(usagestr)
        self.definitionlst=list()
        for definitiontkn in definitionlst:
            self.definitionlst.append(definitiontkn)
            
class Dictionary:
    """Load, create, update save a dictionary"""
    
    def __init__(self,dictfile):
        """Constructor"""
        self.
    
