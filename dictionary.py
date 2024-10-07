import copy
import nltk
from nltk.text import Text
from nltk.tokenize import word_tokenize


class DescriptionCompare:
    def __init__(self,*,descriptionstr=None,descriptionlst=None):

        self.hasdescriptionstr=False
        if isinstance(descriptionstr,str) and descriptionstr!=None:
            self.hasdescriptionstr=True

        self.hasdescriptionlst=False
        if isinstance(descriptionlst,list) and descriptionlst != None:
            self.hasdescriptionlst=True
            for  speechpartobj in descriptionlst:
                if not isinstance(speechpartobj,SpeechPart):
                    self.hasdescriptionlst=False
                    break

        #if no descriptionstr then create descriptionstr from descriptionlst
        if self.hasdescriptionstr:
            self.descriptionstr=descriptionstr
        elif self.hasdescriptionlst:
            #build descriptionstr from descriptionlst
            self.descriptionstr=str()
            for speechpartobj in descriptionlst:
                if isinstance(speechpartobj,Word):
                    if len(self.descriptionstr)>0:
                        self.descriptionstr+=' '
                    self.descriptionstr+=speechpartobj.wordstr

        #if no descriptionlst then create descriptionlst from descriptionstr
        if self.hasdescriptionlst:
            tempdescriptionlst=list()
            for speechpartobj in descriptionlst:
                tempdescriptionlst.append(speechpartobj)
        elif self.hasdescriptionstr:
            self.decriptionlst=list()
            for token in nltk.tokenize.word_tokenize(self.descriptionstr):
                self.decriptionlst.append(\
                    Word(wordstr=token,definitionstr=None,definitionlst=[],posstr=None,usageset=set()))    
    
    def descriptionMatches(self):
        stringfromlst=str()
        for speechpartobj in self.descriptionlst:
            if isinstance(speechpartobj,Word):
                if len(self.descriptionstr)>0:
                    self.descriptionstr+=' '
                stringfromlst+=speechpartobj.wordstr                
        return self.descriptionstr==stringfromlst



class DefinitionCompare:
    def __init__(self,*,definitionstr=None,definitionlst=None):

        self.hasdefinitionstr=False
        if isinstance(definitionstr,str) and definitionstr!=None:
            self.hasdefinitionstr=True

        self.hasdefinitionlst=False
        if isinstance(definitionlst,list) and definitionlst != None:
            self.hasdefinitionlst=True
            for  speechpartobj in definitionlst:
                if not isinstance(speechpartobj,SpeechPart):
                    self.hasdefinitionlst=False
                    break

        #if no definitionstr fill definitionstr with definitionlst
        if self.hasdefinitionstr:
            self.definitionstr=definitionstr
        elif self.hasdefinitionlst:
            #build definitionstr from desfinitionlst
            self.definitionstr=str()
            for speechpartobj in definitionlst:
                if isinstance(speechpartobj,Word):
                    if len(self.definitionstr)>0:
                        self.definitionstr+=' '
                    self.definitionstr+=speechpartobj.wordstr

        if self.hasdefinitionlst:
            tempdefinitionlst=list()
            for speechpartobj in definitionlst:
                tempdefinitionlst.append(speechpartobj)
        elif self.hasdefinitionstr:
            self.definitionlst=list()
            for token in nltk.tokenize.word_tokenize(self.definitionstr):
                self.definitionlst.append(\
                    Word(wordstr=token,definitionstr=None,definitionlst=[],posstr=None,usageset=set()))  
                
    def definitionMatches(self):
        stringfromlst=str()
        for speechpartobj in self.descriptionlst:
            if isinstance(speechpartobj,Word):
                if len(self.descriptionstr)>0:
                    self.descriptionstr+=' '
                stringfromlst+=speechpartobj.wordstr                
        return self.descriptionstr==stringfromlst


                
                
                
                  

        




class PhraseCompare:
    def __init__(self,*,phrasestr=None,phraselst=None):
        self.hasphrasestr=False
        if isinstance(phrasestr,str) and phrasestr != None:
            self.hasphrasestr=True
        
        self.hasphraselst=False
        if isinstance(phraselst,list) and phraselst != None:
            self.hasphraselst=True
            for  speechpartobj in phraselst:
                if not isinstance(speechpartobj,SpeechPart):
                    self.hasphraselst=False
                    break

        if self.hasphrasestr:
            self.phrasestr=phrasestr
        elif self.hasphraselst:
            #build phrasestr from phraselst
            self.phrasestr=str()
            for speechpartobj in phraselst:
                if isinstance(speechpartobj,Word):
                    if len(self.phrasestr)>0:
                        self.phrasestr+=' '
                    self.phrasestr+=speechpartobj.wordstr

        if self.hasphraselst:
            tempphraselst=list()
            for speechpartobj in phrasestr:
                tempphraselst.append(speechpartobj)
        elif self.hasphrasestr:
            tokenlist=[token in nltk.tokenize.word_tokenize(self.phrasestr)]
            for token in nltk.tokenize.word_tokenize(self.phrasestr):
                self.phraselst.append(\
                    Word(wordstr=token,definitionstr=None,definitionlst=[],posstr=None,usageset=set()))  
                
    def phraseMatches(self):
        stringfromlst=str()
        for speechpartobj in self.phraselst:
            if isinstance(speechpartobj,Word):
                if len(self.phrasestr)>0:
                    self.phrasestr+=' '
                stringfromlst+=speechpartobj.wordstr                
        return self.phrasestr==stringfromlst









class Grammar:
    """
    Store the Parts of Speech objects
    Store the Parts of Speech Phrases objects
    Store the equivalencies between Parts Of speech and Parts Of Speech Phrases
    """
    pass






class POSPhrases:
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
    """
    pass





class POS(DescriptionCompare):
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

    def __repr__(self):
        return f'PartOfSpeech:{self.posstr}\nDescription:{self.descriptionstr}'
            
    def __str__(self):
        return f'{self.posstr}'    

    def __init__(self,*,descriptionstr=None,descriptionlst=[],speechpartset=[],posstr=None):
        DescriptionCompare.__init__(self,descriptionstr=descriptionstr,descriptionlst=descriptionlst)
        if not DescriptionCompare.descriptionMatches:
            pass

        self.hasposstr=False
        if isinstance(posstr,str) and posstr != None:
            self.hasposstr=True


        self.hasspeechpartset=False
        if isinstance(speechpartset,set) and speechpartset != None:
            self.hasspeechpartset=True
            for speechpartobj in speechpartset:
                if not isinstance(speechpartobj,SpeechPart):
                    self.hasespeechpartset=False
                    break
            
        if self.hasposstr:
            self.posstr=posstr
        
                            
        if self.hasspeechpartset:
            self.speechpartset=set()
            for speechpartobj in speechpartset:
                self.speechpartset.add(speechpartobj)










class SpeechPartGroup(DescriptionCompare):
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

    def __repr__(self):
        return f'Description:{self.descriptionstr}'
            
    def __str__(self):
        return f'{self.descriptionstr}'    

    def __init__(self,*,descriptionstr= None,descriptionlst=[],\
            usageset=set(),speechpartset=set()):
        DescriptionCompare.__init__(self,descriptionstr=descriptionstr,descriptionlst=descriptionlst)
        
        self.hasspeechpartset=False
        if isinstance(speechpartset,set) and speechpartset != None:
            self.hasspeechpartset=True
            for speechpartobj in speechpartset:
                if not isinstance(speechpartobj,SpeechPart):
                    self.hasespeechpartset=False
                    break

        self.hasusageset=False
        if isinstance(usageset,set) and usageset != None:
            self.hasusageset=True
            for speechpartobj in usageset:
                if not isinstance(speechpartobj,SpeechPart):
                    self.hasusageset=False
                    break

        
        if self.hasspeechpartset:
            for speechpartobj in speechpartset:
                self.speechpartset.add(speechpartobj)

        if self.hasusageset:
            for speechpartobj in usageset:
                self.usageset.add(speechpartobj)










class SpeechPart(DefinitionCompare):
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
            posstr=None,usageset=set(),dictionary=None):
        DefinitionCompare.__init__(self,definitionstr=definitionstr,definitionlst=definitionlst)        

        self.hasposstr=False
        if isinstance(posstr,str) and posstr != None:
            self.hasposstr=True
        

        self.hasusageset=False
        if isinstance(usageset,set) and usageset != None:
            self.hasusageset=True
            for speechpartobj in usageset:
                if not isinstance(speechpartobj,SpeechPart):
                    self.hasusageset=False
                    break

        
        if self.hasposstr:
            self.posstr=posstr
        
        if self.hasusageset:
            for speechpartobj in usageset:
                self.usageset.add(speechpartobj)

            
         
                








class Phrase(SpeechPart,PhraseCompare):
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
        
    Constructor options:
        phrasestr, phaselst, definitionstr, definitionlst
        exists 
            False, False, False, False --> null
            False, False, False, True --> Create definitionstr from definitionlst
            False, False, True, False --> Create definitionlst from definitionstr
            False, False, True, True --> Check for difference beteween definitionstr and definitionlst
            False, True, False, False --> Create phrasestr from phraselst
            False, True, False, True --> Create phrasestr from phraselst Create definitionstr from definitionlst
            False, True, True, False --> Create phrasestr from phraselst Create definitionlst from definitionstr
            False, True, True, True --> Create phrasestr from phraselst Check for difference beteween definitionstr and definitionlst
            True, False, False, False --> Create phraselst from phrasestr
            True, False, False, True --> Create phraselst from phrasestr Create definitionstr from definitionlst
            True, False, True, False --> Create phraselst from phrasestr Create definitionlst from definitionstr
            True, False, True, True --> Create phraselst from phrasestr Check for difference beteween definitionstr and definitionlst
            True, True, False, False --> Check for difference beteween phrasestr and phraselst
            True, True, False, True --> Check for difference beteween phrasestr and phraselst Create definitionstr from definitionlst
            True, True, True, False --> Check for difference beteween phrasestr and phraselst Create definitionlst from definitionstr
            True, True, True, True --> Check for difference beteween phrasestr and phraselst Check for difference beteween definitionstr and definitionlst
        
    """

    def __repr__(self):
        return f'Phrase:{self.phrasestr}\
            \nPart Of Speech:{self.posstr}\
            \nDefiition:{self.definitionstr}'
            
    def __str__(self):
        return f'{self.phrasestr}'    

    def __init__(self,*,phrasestr=None,phraselst=[],\
            definitionstr=None,definitionlst=[],\
            usageset=set(),posstr=None,dictionary=None):
        SpeechPart.__init__(self,definitionstr=definitionstr,definitionlst=definitionlst,posstr=posstr,usageset=usageset,dictionary=dictionary)
        PhraseCompare.__init__(self,phrasestr=phrasestr,phraselst=phraselst)

        self.hasposstr=False
        if isinstance(posstr,str) and posstr != None:
            self.hasposstr=True

        self.hasusageset=False
        if isinstance(usageset,set) and usageset != None:
            self.hasusageset=True
            for speechpartobj in usageset:
                if not isinstance(speechpartobj,SpeechPart):
                    self.hasusageset=False
                    break

        if self.hasposstr:
            self.posstr=posstr
        
        if self.hasusageset:
            for speechpartobj in usageset:
                self.usageset.add(speechpartobj)




        









class Word(SpeechPart,DefinitionCompare):
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
    def __repr__(self):
        return f'Word:{self.wordstr}\
            \nPartOfSpeech:{self.posstr}\
            \nDefinition:{self.definitionstr}'
            
    def __str__(self):
        return f'{self.wordstr}'    

    def __init__(self,*,wordstr=None,\
            definitionstr=None,definitionlst=[],\
            posstr=None,usageset=set(),dictionary=None):
        SpeechPart.__init__(self,posstr=posstr,definitionstr=definitionstr,\
            definitionlst=definitionlst,usageset=usageset,dictionary=None)
        DefinitionCompare.__init__(self,definitionstr=definitionstr,definitionlst=definitionlst)

        self.haswordstr=False
        if isinstance(wordstr,str) and wordstr != None:
            self.haswordstr=True

        self.hasposstr=False
        if isinstance(posstr,str) and posstr != None:
            self.hasposstr=True

        self.hasusageset=False
        if isinstance(usageset,set) and usageset != None:
            self.hasusageset=True
            for speechpartobj in usageset:
                if not isinstance(speechpartobj,SpeechPart):
                    self.hasusageset=False
                    break

        self.hasdictionary=False
        if isinstance(dictionary,Dictionary):
            self.hasdictionary=True
            
        if self.hasposstr:
            self.posstr=posstr
        
        if self.hasusageset:
            for speechpartobj in usageset:
                self.usageset.add(speechpartobj)

        if self.haswordstr:
            self.wordstr=wordstr


        if self.hasdictionary:
            if posstr==None:
                if (self.wordstr,'unknown') in dictionary.entries():
                    print('word is in dictionay')
            else:
                if(self.wordstr,self.posstr) in dictionary.entries():
                    print('word is in dictionary')
                else:
                    print('word is not in dictionary')
            dictionary.speechpartset.add(self)
        else:
            print('no dictioary provided')
             











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
    def __repr__(self):
        #build pre part string
        prestring=str()
        for speechpartobj in self.prespeechpartlst:
            presrint+=str(speechpartobj)
        thisstring=str(self.thisspeechpartobj)
        poststring=str()
        for speechpartobj in self.postspeechpartlst:
            poststring+=str(speechpartobj)
        return f'Pre speech:{prestring}\
            \nThis speech:{thisstring}\
            \nPost speech:{poststring}'
            
    def __str__(self):
        return f'{self.sourcestr}'    

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
        










class Corpora(DescriptionCompare):
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

    def __repr__(self):
        return f'Corpora:{self.namestr}\
            \nDescription:{self.descriptionstr}\
            \nPost speech:{self.corporastr}'
            
    def __str__(self):
        return f'{self.namestr}'    

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
            










class Definition(DefinitionCompare):
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

    def __repr__(self):
        return f'Definition:{self.definitionstr}\
            \nPart Of Speech:{self.posstr}'
            
    def __str__(self):
        return f'{self.definitionstr}'    

    def __init__(self,*,definitionstr=None,definitionlst=[],\
            posstr=None,speechpartset=set()):
        DefinitionCompare.__init__(self,definitionstr=definitionstr,definitionlst=definitionlst)

        self.hasposstr=False
        if isinstance(posstr,str):
            self.hasposstr=True
        
        self.hasspeechpartset=False
        if isinstance(speechpartset,set):
            self.hasspeechpartset=True
            for speechpartobj in speechpartset:
                if not isinstance(speechpartobj,Word):
                    self.hasspeechpartlst=False
                    break
            
        if self.hasposstr:
            self.posstr=posstr

        if self.hasspeechpartset:
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
    def entries(self):
        #entry=set()
        #for speechpart in self.speechpartset:
        #    entry.add(speechpart.)
        wordentries=[(entry.wordstr,entry.posstr) for entry in self.speechpartset if isinstance(entry,Word)]
        phraseentries=[(entry.phrasestr,entry.posstr) for entry in self.speechpartset if isinstance(entry,Phrase)]
        return(sorted(wordentries+phraseentries))

    def addEntry(self,speechpart):
        """
        Add a speechpart to the dictionary.
        Args:
            speechpart (Speechpart): A word or phrase that can occupy a part of speech and has a meaning 
        """
        if isinstance(speechpart, SpeechPart):
            self.speechpartset.add(speechpart)
    
    def __init__(self,*,dictionaryfle=None,speechpartset=set()):
        
        self.dictioanryfle=dictionaryfle
        self.hasspeechpartset=False
        if isinstance(speechpartset,set):
            self.hasspeechpartset=True
            for speechpartobj in speechpartset:
                if not isinstance(speechpartobj,Word):
                    self.hasspeechpartset=False
                    break
        self.speechpartset=set()        
        if self.hasspeechpartset:
            for speechpartobj in speechpartset:
                self.speechpartset.add(speechpartobj)
    








def main():
    d=Dictionary(dictionaryfle=None,speechpartset=None)
    w=Word(wordstr='word',definitionstr='A word',definitionlst=[],posstr='noun',usageset=set(),dictionary=d)
    print('d',d.entries())
    #print('Word members\n',w.wordstr,w.definitionstr,w.posstr)
    #print('word string:',str(w))
    #print(f'word repr:\n{w!r}')
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
