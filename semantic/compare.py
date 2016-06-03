from nltk.corpus import wordnet

list1 = ['Compare', 'require']
list2 = ['choose', 'copy','need']
newlist = []

for word1 in list1:
    for word2 in list2:
        wordFromList1 = wordnet.synsets(word1)
        wordFromList2 = wordnet.synsets(word2)
        if wordFromList1 and wordFromList2:
            s = wordFromList1[0].wup_similarity(wordFromList2[0])
            newlist.append(s)

# print(max(list))
thelist = []
for x in newlist:
	# print (i)
	# print (x)
	try :
		test = int(x)
		print("added",x)
		thelist.append(x)
	except:
		print("exception")
# print(max(newlist))

