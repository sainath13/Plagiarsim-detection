#basic structure
#{'key': [value1 , value2]}

f = open('1.1','r')
g = open('2.1' , 'r')
h = open('3.1' , 'r')

file1 = f.read()
file2 = g.read()
file3 = h.read()

tokens1 = file1.split()
tokens2 = file2.split()
tokens3 = file3.split()
# print tokens1
# print tokens2

value1 = 1
value2 = 1
value3 = 1
stuff = {'key': [value1, value2,value3]}

val1 = [1,0,0]
val2 = [0,1,0]
val3 = [0,0,1]

first = [1,0,0]
second = [0,1,0]
third = [0,0,1]

j = 0

for index in range(len(tokens1)):
	if tokens1[j] in stuff:
		stuff[tokens1[j]] = [x + y for x , y in zip(stuff[tokens1[j]], first )] 
		
	else :
		stuff.update({tokens1[j] : val1})
	j = j+ 1;

#stuff['import'] = [x + y for x ,y in zip( [1,2],[100,2])]
# print stuff
j = 0 
for index in range(len(tokens2)):
	if tokens2[j] in stuff:
		stuff[tokens2[j]] = [x + y for x , y in zip (stuff[tokens2[j]] , second)]
	else:
		stuff.update({tokens2[j]:val2})
	j = j + 1;
# print stuff
j = 0
for index in range(len(tokens3)):
	if tokens3[j] in stuff:
		stuff[tokens3[j]] = [x + y for x , y in zip (stuff[tokens3[j]] , third)]
	else:
		stuff.update({tokens3[j]:val3})
	j = j + 1;

# for key, value in stuff.iteritems():
# 	print '| {0:20s} : {1:7} |' . format(key, stuff[key])
	

#term frequency completed

#now tf-idf remains and other things

#refer to the ppt
#implement the log 2 base functionality 
#for values in stuff:
#	print stuff[values]

print "\n"
stopwords = "a's a the it  able about above according accordingly across actually after afterwards again against ain't all allow allows almost alone along already also although always am among amongst an and another any anybody anyhow anyone anything anyway anyways anywhere apart appear appreciate appropriate are aren't around as aside ask asking associated at available away awfully be became because become becomes becoming been before beforehand behind being believe below beside besides best better between beyond both brief but by c'mon c's came can can't cannot cant cause causes certain certainly changes clearly co com come comes concerning consequently consider considering contain containing contains corresponding could couldn't course currently definitely described despite did didn't different do does doesn't doing don't done down downwards during each edu eg eight either else elsewhere enough entirely especially et etc even ever every everybody everyone everything everywhere ex exactly example except far few fifth first five followed following follows for former formerly forth four from further furthermore get gets getting given gives go goes going gone got gotten greetings had hadn't happens hardly has hasn't have haven't having he he's hello help hence her here here's hereafter hereby herein hereupon hers herself hi him himself his hither hopefully how howbeit however i'd i'll i'm i've ie if ignored immediate in inasmuch inc indeed indicate indicated indicates inner insofar instead into inward is isn't it it'd it'll it's its itself just keep keeps kept know known knows last lately later latter latterly least less lest let let's like liked likely little look looking looks ltd mainly many may maybe me mean meanwhile merely might more moreover most mostly much must my myself name namely nd near nearly necessary need needs neither never nevertheless new next nine no nobody non none noone nor normally not nothing novel now nowhere obviously of off often oh ok okay old on once one ones only onto or other others otherwise ought our ours ourselves out outside over overall own particular particularly per perhaps placed please plus possible presumably probably provides que quite qv rather rd re really reasonably regarding regardless regards relatively respectively right said same saw say saying says second secondly see seeing seem seemed seeming seems seen self selves sensible sent serious seriously seven several shall she should shouldn't since six so some somebody somehow someone something sometime sometimes somewhat somewhere soon sorry specified specify specifying still sub such sup sure t's take taken tell tends th than thank thanks thanx that that's thats the their theirs them themselves then thence there there's thereafter thereby therefore therein theres thereupon these they they'd they'll they're they've think third this thorough thoroughly those though three through throughout thru thus to together too took toward towards tried tries truly try trying twice two un under unfortunately unless unlikely until unto up upon us use used useful uses using usually value various very via viz vs want wants was wasn't way we we'd we'll we're we've welcome well went were weren't what what's whatever when whence whenever where where's whereafter whereas whereby wherein whereupon wherever whether which while whither who who's whoever whole whom whose why will willing wish with within without won't wonder would wouldn't yes yet you you'd you'll you're you've your yours yourself yourselves zero If The All It etc. There"
stoped = stopwords.split()

w1 = open('output1', 'w')
w2 = open('output2', 'w')
w3 = open('output3', 'w')

import re

def stem(word):
        if len(word) >= 3 :
		word = re.sub(r'ies$', 'i', word)
                word = re.sub(r'ing$', '', word)
                word = re.sub(r's$', '', word)     
		word = re.sub(r'sses$', 'ss', word)
                word = re.sub(r'tional$', 'tion', word)                                                           
        return word


def stop_stem(value,m):
	for ind in value:
		if ind == ',':
			continue
		if ind == '.':
			continue
		if ind in stoped:
			continue
		else:
			ind = stem(ind)			
			if(m == 1):			
				w1.write(ind)
				w1.write(" ")
			if(m == 2):
				w2.write(ind)
				w2.write(" ")
			if(m == 3):
				w3.write(ind)
				w3.write(" ")

	print "\n"
	print "collocation found"
	for ind in finput:
		if '-' in ind:
			print ind
	


finput = file1.split()
stop_stem(finput,1)
finput = file2.split()
stop_stem(finput,2)
w1.close()
w2.close()

del stuff['.']
del stuff[',']
for ind in stoped:
	if ind in stuff:
		del stuff[ind]
#i = 0
dic = []
for key, value in stuff.iteritems():	
#	print i 
#	i = i +1
	# print '| {0:20s} : {1:7} |' . format(key, stuff[key])
	dic.append(key)
# print dic
c1 = []
c2 = []
c3 = []
for values in stuff:
	l1 = stuff[values]
	c1.append(l1[0])
	c2.append(l1[1])
	c3.append(l1[2])
#print c1
#print c2
#print c3


# print c2[100]
############finding tf-idf##############

# print len(c2)
idf = []
ni = 0
charman = "for index :"
import math
for index in range(len(c1)):
	if c1[index] == 0:
		if c2[index] == 0:
			ni = 1
		elif c3[index] == 0: 
			ni = 1
		else:
			ni = 2
	elif c2[index] == 0:
			if c3[index] == 0:
				ni =1
			else:
				ni = 2
	else:
		ni = 3

	print charman,  index 
	N = 3.0 
	temp = math.log( (N/ni) , 2)
	print temp
	idf.append(temp)
	#print idf[index]

#now create a tf.idf table
#0   1   2   3   4   5
#c1 c2  c3  c1  c2  c3
#0  1   1   2   2
# index = 1
# ind1 = 0
# ind2 = 0
# ind3 = 0
print '_____________________________________________________________'

#word = stuff[]
#print word
# One = "file1"
# Two = "file2"
# Three = "file3"
# for index in range(len(c1)):
# #	print "index is"
# #	print index 
# 	if index % 3 == 1 :
# 		val = c2[ind2] * idf[index]
# 		print dic[index] , val		
# 		ind2 = ind2 + 1
# 	if index % 3 == 2 :
# 		val = c3[ind3]* idf[index]
# 		dic[index] , val
# 		ind3 = ind3 + 1		
	
# 	if index %3 == 0:	
# 		val = c1[ind1] * idf[index]
# 		dic[index] , val
# 		ind1 = ind1 + 1

space = " "
index = 0
for key, value in stuff.iteritems():
#	print i
#	i = i +1
	# print charman,index
	# print '| {0:20s} : {1:7} |' . format(key, stuff[key])
	# print key ,"\t\t\t\t",'||', stuff[key][0]*idf[index] ,space,'||', stuff[key][1]*idf[index] ,space ,'||',  stuff[key][2]*idf[index] 
	index = index + 1
	# dic.append(key)

print "______________________________________________________________________________________________________________________"
index = 0
for key, value in stuff.iteritems():
#	print i
#	i = i +1
	# print charman,index
	# print '| {0:20s} : {1:7} |' . format(key, stuff[key])
	Sum =  stuff[key][0] + stuff[key][1] + stuff[key][2]

	prob1 = " "+  str(stuff[key][0])+ "/" + str(Sum) 
	prob2 = " "+  str(stuff[key][1])+ "/" + str(Sum) 
	prob3 = " "+  str(stuff[key][2])+ "/" + str(Sum) 
	# print len(key)
	while (len(key) < 10):
		key = key + " "

	print key ,"\t\t\t\t",'||', prob1,'||', prob2,'||', prob3

	index = index + 1
	# dic.append(key)
print "______________________________________________________________________________________________________________________"
index = 0
allwordsin1 = 0
allwordsin2 = 0
allwordsin3 = 0
for key, value in stuff.iteritems():
	
	temp1 = stuff[key][0]
	allwordsin1 = allwordsin1  + temp1
	

	
	temp2 = stuff[key][1]
	allwordsin2 = allwordsin2  + temp2



	
	temp3 = stuff[key][2]
	allwordsin3 = allwordsin3  + temp3


print "______________________________________________________________________________________________________________________"
print "______________________________________________________________________________________________________________________"
print allwordsin3, allwordsin2 , allwordsin1

print "for file 1"
print "______________________________________________________________________________________________________________________"
for key, value in stuff.iteritems():
	# Sum =  stuff[key][0] + stuff[key][1] + stuff[key][2]
	# a = stuff[key][0]
	# for 
	# prob1 = " "+  str(stuff[key][0])+ "/" + str(Sum) 
	# prob2 = " "+  str(stuff[key][1])+ "/" + str(Sum) 
	# prob3 = " "+  str(stuff[key][2])+ "/" + str(Sum) 
	# print key ,"\t\t\t\t",'||', prob1,'||', prob2,'||', prob3
	a = stuff[key][0]
	c = allwordsin1 - a
	b = stuff[key][1] + stuff[key][2]
	d = allwordsin3 + allwordsin2 - b
	
	N = a + b + c + d

	E11 =	(a+b) * (a+c) * 1.0 / N
	E12 = 	(a+b) * (b+d) * 1.0 / N
	E21 =	(a+c) * (c+d) * 1.0 / N 
	E22 =   (b+d) * (c+d) * 1.0 / N
	arr1 = [ E11, E12, E21, E22 ]
	arr2 = [ a,b,c,d ]
	chi = 0
	chi = chi + ((arr1[0]-arr2[0])* ( arr1[0]- arr2[ 0 ] ) ) / arr1[ 0 ]
	chi = chi + ((arr1[1]-arr2[1])* ( arr1[1]- arr2[ 1 ] ) ) / arr1[ 1 ]
	chi = chi + ((arr1[2]-arr2[2])* ( arr1[2]- arr2[ 2 ] ) ) / arr1[ 2 ]
	chi = chi + ((arr1[3]-arr2[3])* ( arr1[3]- arr2[ 3 ] ) ) / arr1[ 3 ]
	
	# print key , chi
	index = index + 1



print "______________________________________________________________________________________________________________________"
print "for file 2"
print "______________________________________________________________________________________________________________________"
for key, value in stuff.iteritems():
	# Sum =  stuff[key][0] + stuff[key][1] + stuff[key][2]
	# a = stuff[key][0]
	# for 
	# prob1 = " "+  str(stuff[key][0])+ "/" + str(Sum) 
	# prob2 = " "+  str(stuff[key][1])+ "/" + str(Sum) 
	# prob3 = " "+  str(stuff[key][2])+ "/" + str(Sum) 
	# print key ,"\t\t\t\t",'||', prob1,'||', prob2,'||', prob3
	a = stuff[key][1]
	c= allwordsin2 - a
	b = stuff[key][0] + stuff[key][2]
	d = allwordsin3 + allwordsin1 - b
	
	N = a + b + c + d

	E11 =	( a + b ) * ( a + c ) * 1.0 / N
	E12 = 	( a + b ) * ( b + d ) * 1.0 / N
	E21 =	( a + c ) * ( c + d ) * 1.0 / N 
	E22 =   ( b + d ) * ( c + d ) * 1.0 / N
	arr1 = [ E11, E12, E21, E22 ]
	arr2 = [ a,b,c,d ]
	chi = 0
	chi = chi + ( ( arr1[ 0 ] - arr2[ 0 ] ) * ( arr1[ 0 ] - arr2[ 0 ] ) ) / arr1[ 0 ]
	chi = chi + ( ( arr1[ 1 ] - arr2[ 1 ] ) * ( arr1[ 1 ] - arr2[ 1 ] ) ) / arr1[ 1 ]
	chi = chi + ( ( arr1[ 2 ] - arr2[ 2 ] ) * ( arr1[ 2 ] - arr2[ 2 ] ) ) / arr1[ 2 ]
	chi = chi + ( ( arr1[ 3 ] - arr2[ 3 ] ) * ( arr1[ 3 ] - arr2[ 3 ] ) ) / arr1[ 3 ]
	
	# print key , chi
	index = index + 1


print "______________________________________________________________________________________________________________________"
print "for file 3"
print "______________________________________________________________________________________________________________________"
for key, value in stuff.iteritems():
	# Sum =  stuff[key][0] + stuff[key][1] + stuff[key][2]
	# a = stuff[key][0]
	# for 
	# prob1 = " "+  str(stuff[key][0])+ "/" + str(Sum) 
	# prob2 = " "+  str(stuff[key][1])+ "/" + str(Sum) 
	# prob3 = " "+  str(stuff[key][2])+ "/" + str(Sum) 
	# print key ,"\t\t\t\t",'||', prob1,'||', prob2,'||', prob3
	a = stuff[key][2]
	c= allwordsin3 - a
	b = stuff[key][0] + stuff[key][1]
	d = allwordsin1 + allwordsin2 - b
	
	N = a + b + c + d

	E11 =	( a + b ) * ( a + c ) * 1.0 / N
	E12 = 	( a + b ) * ( b + d ) * 1.0 / N
	E21 =	( a + c ) * ( c + d ) * 1.0 / N 
	E22 =   ( b + d ) * ( c + d ) * 1.0 / N
	arr1 = [ E11, E12, E21, E22 ]
	arr2 = [ a,b,c,d ]
	chi = 0
	chi = chi + ( ( arr1[ 0 ] - arr2[ 0 ] ) * ( arr1[ 0 ] - arr2[ 0 ] ) ) / arr1[ 0 ]
	chi = chi + ( ( arr1[ 1 ] - arr2[ 1 ] ) * ( arr1[ 1 ] - arr2[ 1 ] ) ) / arr1[ 1 ]
	chi = chi + ( ( arr1[ 2 ] - arr2[ 2 ] ) * ( arr1[ 2 ] - arr2[ 2 ] ) ) / arr1[ 2 ]
	chi = chi + ( ( arr1[ 3 ] - arr2[ 3 ] ) * ( arr1[ 3 ] - arr2[ 3 ] ) ) / arr1[ 3 ]
	
	# print key , chi
	index = index + 1



