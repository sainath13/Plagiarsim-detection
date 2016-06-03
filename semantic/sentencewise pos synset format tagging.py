# open a file
# tokenize in sentences
# for each sentence 
# tokenize into words
# for each word 
# find the synset format 
# append it in the list

# import codecs
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize


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


# mytest = allSentences[0]
# print(mytest)
# sentence = mytest
# print(sentence)
# tagged = pos_tag(word_tokenize(sentence))
# print(tagged)

setSynset = []
lemmatzr = WordNetLemmatizer()
for sentence in allSentences:
    # print(sentence)
    tagged = pos_tag(word_tokenize(sentence))
    # print(tagged)
    for token in tagged:
        # print(token)
        wn_tag = penn_to_wn(token[1])
        if not wn_tag:
            continue
        # print(lemma)
        # print(wn.synsets(lemma, pos=wn_tag)[0])
        synset = wn.synsets(token[0])
        if len(synset) == 0:
            test = 0
            # print("skipped")
        else :
            try:
                lemma = lemmatzr.lemmatize(token[0], pos=wn_tag)
                if(wn.synsets(lemma, pos=wn_tag)[0] in setSynset):
                    test = 0
                    # print("already in setSynset")
                else:
                    setSynset.append(wn.synsets(lemma, pos=wn_tag)[0])
                # print("appended", setSynset)
            except:
                test = 0
                # print("skipped")
print (setSynset[0])
