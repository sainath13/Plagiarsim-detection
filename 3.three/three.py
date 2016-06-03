#basic structure
#{'key': [value1 , value2]}
f = open('1.3','r')
g = open('2.3' , 'r')

file1 = f.read()
file2 = g.read()

tokens1 = file1.split()
tokens2 = file2.split()

# print tokens1
# print tokens2

value1 = 1
value2 = 1
stuff = {'key': [value1, value2]}
j = 0
val1 = [1,0]
val2 = [0,1]
first = [1,0]
second = [0,1]
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

for key, value in stuff.iteritems():
	print '| {0:20s} : {1:7} |' . format(key, stuff[key])

#term frequency completed

#now tf-idf remains and other things

#refer to the ppt
#implement the log 2 base functionality 
#for values in stuff:
#	print stuff[values]
c1 = []
c2 = []
for values in stuff:
	l1 = stuff[values]
	c1.append(l1[0])
	c2.append(l1[1])
#print c1
#print c2

from math import*
 
def euclidean_distance(x,y):
 
  return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

print "euclidian distance is :"
print euclidean_distance(c1,c2)
 
def square_rooted(x):
 
   return round(sqrt(sum([a*a for a in x])),3)
 
def cosine_similarity(x,y):
 
 numerator = sum(a*b for a,b in zip(x,y))
 denominator = square_rooted(x)*square_rooted(y)
 return round(numerator/float(denominator),3)
print "cosine similarity is:"
print cosine_similarity(c1, c2)