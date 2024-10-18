import nltk, re, pprint
from nltk import word_tokenize

f=open('corpus/threebears.txt', 'r')
raw=f.read()
tokens=word_tokenize(raw)
#words=[w.lower() for w in tokens]
#fdist=nltk.FreqDist(words)
#for word,count in fdist.most_common():
#    print(word,count)
postagged=nltk.pos_tag(tokens)
for tagged in postagged:
    print(tagged)

newtagged=list()   
for tagged in postagged:
    if postagged[1]=='NN' and postagged.next()[1] =='CC' and postagged.next().next()[1]=='NN':
        print