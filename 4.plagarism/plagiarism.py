#fingerprinting
#local similarity assesment
f = open('batmanVSsuperman1.txt','r')
g = open('batmanVSsuperman2.txt' , 'r')

file1 = f.read()
file2 = g.read()

tokens1 = file1.split()
tokens2 = file2.split()

# print (tokens1)
# print (tokens2)

trigram1 = list()
trigram2 = list()

# trigram1.append('test')

# print (trigram1)
for i in range(0,len(tokens1) - 2 ):
	trigram = tokens1[i] + " " + tokens1[i+1] + " " + tokens1[i+2]
	trigram1.append(trigram)
# print (trigram1)

# print (trigram2)
for i in range(0,len(tokens2) - 2 ):
	trigram = tokens2[i] + " " + tokens2[i+1] + " " + tokens2[i+2]
	trigram2.append(trigram)
# print (trigram2)


# self plagarasism
# two document plagarism
copied = list()
###Below we compute plagarism
for trigram in trigram1:
	if trigram in trigram2:
		copied.append(trigram)

# print(copied)
import demjson
datatoexport = demjson.encode(copied);
print(datatoexport)
total1 = len(trigram1)
total2 = len(trigram2)

#percentage
len_copy = len(copied)
plagarism_percentage1 = ( len_copy / total1) * 100
plagarism_percentage2 = ( len_copy / total2) * 100

print("length is",len_copy)

##find total number of trigrams in document1 and document2
print("total number of trigram in Document1" , total1);
print("total number of trigram in Document2" , total2);
#find how many are matching -> find out percentage
print("plagiarism in document1" , plagarism_percentage1)
print("plagiarism in document2" , plagarism_percentage2)

from collections import Counter
self_plag1 = [k for k,v in Counter(trigram1).items() if v > 1] 
self_plag_percent1 = (len(self_plag1) /  total1 ) * 100

self_plag2 = [k for k,v in Counter(trigram2).items() if v > 1] 
self_plag_percent2  = (len(self_plag2) / total2 ) * 100

print("self plagiarism in document1" , self_plag_percent1)
print("self plagiarism in document2" , self_plag_percent2)

# print(trigram2)
#print(len(test))
##find self plagarism
#set some base limit -> usually 8 percent
#give verdict in that json only..
#read in nodejs and display some dashboard system so that it looks cool
