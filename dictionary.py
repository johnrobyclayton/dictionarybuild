class POS:
    """
    Load,create,edit,save Parts of Speech
    A Part of Speech is the gramatical purpose of a word or phrase in a sentence
    """
    def __init__(self,posstr,descriptionstr,wordlst=[],descriptionlst=[]):
        self.posstr=posstr
        self.descriptionstr=descriptionstr
        self.wordlst=list()
        for wordstr in wordlst:
            self.wordlst.append(wordstr)
        for descriptiontkn in descriptionlst:
            self.descriptionlst.append(descriptiontkn)

class Wordgroup:
    """
    Load,create,edit,save wordgroups
    A Wordgroup is a group of words that are interchangeable in some way within a text
    They might be different things that can replace each other and result in a
    gramatical and/or a sensible sentence
    """
    def __init__(self,posstr,descriptionstr,wordlst=[],descriptionlst=[]):
        self.posstr=posstr
        self.descriptionstr=descriptionstr
        self.wordlst=list()
        for wordstr in wordlst:
            self.wordlst.append(wordstr)
        for descriptiontkn in descriptionlst:
            self.descriptionlst.append(descriptiontkn)
            
class Phrase:
    """
    Load,create,edit,save phrases
    A Part Of speech can be occupied by a series of words or other phrases. 
    """
    def __init__(self,phrasestr,posstr,definitionstr,phraselst=[],definitionlst=[],usagelst=[]):
        self.phrasestr=phrasestr
        self.posstr=posstr
        self.definitionstr=definitionstr
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
    
