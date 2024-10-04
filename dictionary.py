import copy
class POS:
    """
    Load,create,edit,save Parts of Speech
    A Part of Speech is the gramatical purpose of a word or phrase in a sentence
    members:
        posstr: a string identifying the part of speech
        posobj: a instance of a POS class
        descriptionstr: a string describing the part of speech
        descriptionlst: an ordered list of SpeechParts objects, which can be either Word objects of Phrase objects 
            that make up the description
        speechpartlst: a list of speechpart objects that are this part of speech observed in corpora
        
    """
    def isValid(self):
        descriptionlstUnpacked=str()
        for speechpartobj in self.descriptionlst:
            descriptionUnpacked+=str(speechpartobj)
        return self.descriptionstr==descriptionlstUnpacked

    def __init__(self,*,posstr=None,descriptionstr=None,speechpartset=[],descriptionlst=[]):
        def signature():
            """
            generates a constructor signature that is used to select a function for creating the object.
                Parameters:
                    The parameters of the __init__ function
                Returns:
                    For each parameter in the __init__ function
                        assign a unique power of 2 value
                        if the type of the parameter in None or empty set,dict,list set the value to 0 
                        else set the value to the power of 2
                        Sum all the values
                        return the sum for the signature
            """
            
            
            
        
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
        posobj: POS object identifying a part of speech
        descriptionstr: description of the words and phrases that make up this group
        contextset: the set of context objects where these word objects and phrase 
            objects can be found
        speechpartset: the set of SpeechPart objects in this SpeechPartGroup
        descriptionlst: The list of SpeechPart objects that make up the 
            descriptionstr 
    """
    def isValid(self):
        descriptionlstUnpacked=str()
        for speechpartobj in self.descriptionlst:
            descriptionUnpacked+=str(speechpartobj)
        return self.descriptionstr==descriptionlstUnpacked

    def __init__(self,descriptionstr= None,contextset=set(),speechpartset=set(),descriptionlst=[]):
        self.posobj=posobj
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
        posstr the string identifying its part of speech
        posobj The POS object describing its part of speech
        definitionstr The string of its definition
        definitionlst The list of SpeechPart objects making up the definition.
        usageset the set of usage objects that describe where this SpeechPart shows in corpora
    """    
    def isValid(self):
        descriptionlstUnpacked=str()
        for speechpartobj in self.definitionlst:
            definitionlstUnpacked+=str(speechpartobj)
        return self.desfinitionstr==definitionlstUnpacked

    def __init__(self, posstr=None,definitionstr=None,definitionlst=[],usageset=set()):
        
        
        self.posstr=posstr
        self.posobj=posobj
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
        phraseobj a phrase object
        posstr the string identifying the part of speech
        posobj the POS object describing the part of speech
        definitionstr the string with the definition of the phrase
        speechpartlst the list of speechpart objects that make up the phrase
        definitionlst the list of speechpart objects that make up the definition.
        usagelist the list of usage objects that describe where this phrase shows up in corpora
    """
    def __init__(self,phrasestr=None,phraseobj=None,posstr=None,posobj=None,definitionstr=None,speechpartlst=[],definitionlst=[],usageset=set()):
        self.phrasestr=phrasestr
        self.phaseobj=phraseobj
        SpeechPart.__init__(posstr,posobj,definitionstr,definitionlst,usageset)
        self.phraselst=list()
        for speechpartobj in speechpartlst:
            self.phraselst.append(speechpartobj)
        
class Word(SpeechPart):
    """
    Load,create,edit,save words
    A Part Of speech can be occupied by a word. 
    Members:
        wordstr the string representation of the phrase
        wordobj a phrase object
        posstr the string identifying the part of speech
        posobj the POS object describing the part of speech
        definitionstr the string with the definition of the phrase
        speechpartlst the list of speechpart objects that make up the phrase
        defiitionlst the list of speechpart objects that make up the definition.
        usagelist the list of usage objects that describe where this phrase shows up in corpora
    """
    def __init__(self,wordstr=None,wordobj=None,posstr=None,posobj=None,definitionstr=None,usagestr=None,usageset=set(),definitionlst=[]):
        self.wortstr=wordstr
        self.wordobj=wordobj
        SpeechPart.__init__(posstr,posobj,definitionstr,definitionlst,usageset)
        
    
            
class Usage:
    """
    Load,create,edit,save usages
    A usage of a word or phrase describes its context observed in corpora
    A Usage is made up of words, phrases and wordgroups that have particular parts of speech surrounding
    a word or phrase that identify the contexts where the word or phrase occurs and can be used to identify its pos 
    Members:
        corpora an object describing the source of the usage of the speechpart for which this is a usage of
        prespeechpartlst the list of speechparts before the speechpart for which this is a usage of
        speechpart the speechpart for which this is a usage of
        postspeechpartlst the list of speechparts after the speechpart for which this is a usage of
        sourcestr the string from the corpora that is the source of this usage
    """
    def __init__(self,corpora=None,prespeechpartlst=[],thisspeechpartobj=None,postspeechpartlst=[],sourcestr=None):
        self.corpora=corpora
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
    namestr a string that identifies the corpora
    metadatastr a string that contains the mettadata for the corpora
    corporastr a string representation of the corpora
    speechpartlst a list of speechparts representing the corpora
    descriptionstr a string describing the corpora
    descriptionlst a list of speechparts that describe the corpora
    filespec the specitifation of the file containing the corpora
    """        
    def __init__(self,namestr=None,metadatastr=None,corporastr=None,speechpartlst=[],descriptionstr=None,descriptionlst=[],filespec=None):
        self.namestr=namestr
        self.metadatastr=metadatastr
        self.corporastr=corporastr
        self.speechpartlst=list()
        for speechpartobj in speechpartlst:
            self.speechpartlst.append(speechpartobj)
        self.descriptionstr=descriptionstr
        self.descriptionlst=list()
        for speechpartobj in descriptionlst:
            self.descriptionlst.append(speechpartobj)
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
    def __init__(self,definitionstr=None,posstr=None,posobj=None,definitionlst=[],speechpartset=set()):
        self.definitionstr-definitionstr
        self.posstr=posstr
        self.posobj=posobj
        self.definitionlst=list()
        for speechpartobj in definitionlst:
            self.definitionlst.append(speechpartobj)
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
    
