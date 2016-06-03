# In this code two files are not compared 
# a new file with the existing database is compare
# database consits of set of trigrams
# Non repeating

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# step 1 : read pkl									 #
# step 2 : read file 								 #
# step 3 : compare 									 #
# ster 4 : if ! plagiarism : then update pkl		 #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import pprint, pickle

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
# pprint.pprint(data1)

pkl_file.close()
#fingerprinting
#local similarity assesment
# f = open('batmanVSsuperman1.txt','r')
filename ='test.txt' 
f = open(filename, 'r')

file1 = f.read()
# file2 = g.read()

tokens1 = file1.split()
# tokens2 = file2.split()

# print (tokens1)
# print (tokens2)

trigram1 = list()
# trigram2 = list()

# trigram1.append('test')

# print (trigram1)
for i in range(0,len(tokens1) - 2 ):
	trigram = tokens1[i] + " " + tokens1[i+1] + " " + tokens1[i+2]
	trigram1.append(trigram)
# print (trigram1)

# print (trigram2)
# for i in range(0,len(tokens2) - 2 ):
# 	trigram = tokens2[i] + " " + tokens2[i+1] + " " + tokens2[i+2]
# 	trigram2.append(trigram)
# print (trigram2)


# self plagarasism
# two document plagarism
copied = list()
###Below we compute plagarism
for trigram in trigram1:
	if trigram in data1:
		copied.append(trigram)

# print(copied)
# import demjson
# datatoexport = demjson.encode(copied);
# print(datatoexport)
total1 = len(trigram1)
# total2 = len(trigram2)

#percentage
len_copy = len(copied)
plagarism_percentage1 = ( len_copy / total1) * 100
# plagarism_percentage2 = ( len_copy / total2) * 100

print("Total number of copied trigram document submitted is : ",len_copy)

##find total number of trigrams in document1 and document2
print("Total number of trigram in document submitted " , total1);
# print("total number of trigram in Document2" , total2);
#find how many are matching -> find out percentage
#find which trigrams are matching -> to show them in red color
#output in some nice json to read in node and show graph and some shit
print("Plagiarism observed in document submitted :" , plagarism_percentage1)
# print("plagarism in document2" , plagarism_percentage2)

from collections import Counter
self_plag1 = [k for k,v in Counter(trigram1).items() if v > 1] 
self_plag_percent1 = (len(self_plag1) /  total1 ) * 100

# self_plag2 = [k for k,v in Counter(trigram2).items() if v > 1] 
# self_plag_percent2  = (len(self_plag2) / total2 ) * 100

print("Self plagiarism in document submitted" , self_plag_percent1)
# print("self plagarism in document2" , self_plag_percent2)


if(plagarism_percentage1 < 20.00):
	output = open('data.pkl', 'wb')
	for trigram in trigram1:
		if trigram in data1:
			# skip
			print("skipped", trigram)
		else:
			print("appending",trigram)
			data1.append(trigram)			
	pickle.dump(data1, output)
	output.close()
	print("No plagiarism found")

# filename =  "file4"
# plag = plagarism_percentage1
# self = self_plag_percent1
# import json
# json.dumps('{"number" : '+filename+'}')
# # print(stringyfy(v))
# data = {}
import json
# data['batvsup'] = plagarism_percentage1
# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)
# json_data = json.dumps(data)
# print(json_data)


from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)

data[filename] = self_plag_percent1
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

# print(trigram2)
#print(len(test))
##find self plagarism
#set some base limit -> usually 8 percent
#give verdict in that json only..
#read in nodejs and display some dashboard system so that it looks cool