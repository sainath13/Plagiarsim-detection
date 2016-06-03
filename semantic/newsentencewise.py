# open a file
# tokenize in sentences
# import codecs
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize

f = open('sent_test_pos_tag.txt','r')
readData = f.read()

allSentences = sent_tokenize(readData)

# print(allSentences[0])

def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None

from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize

mytest = "Again it seems that cocoa delivered earlier on consignment was included in the arrivals figures."
print(mytest)
sentence = mytest
print(sentence)
tagged = pos_tag(word_tokenize(sentence))
print(tagged)

synsetsainath = []
lemmatzr = WordNetLemmatizer()
# for sentence in allSentences:
#     # print(sentence)
#     tagged = pos_tag(word_tokenize(sentence))
#     # print(tagged)
for token in tagged:
    print(token)
    wn_tag = penn_to_wn(token[1])
    if not wn_tag:
        continue
    # print(lemma)
    # print(wn.synsets(lemma, pos=wn_tag)[0])
    synset = wn.synsets(token[0])
    if len(synset) == 0:
        print("skipped")
    else :
        try:
            lemma = lemmatzr.lemmatize(token[0], pos=wn_tag)
            synsetsainath.append(wn.synsets(lemma, pos=wn_tag)[0])
            print("appended", synsetsainath)
        except:
            print("skipped")
        
print (synsetsainath)