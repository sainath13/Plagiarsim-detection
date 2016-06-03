# dealing with just words here
# later downloading brown build a structure having all the similar wods from one file.
# then after analysing the second file see if those wods are present in the structure or not.

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
import nltk

skipcount = 0
# open a file here
f = open('readthis1.txt','r')
g = open('readthis2.txt','r')

	
file1 = f.read()
file2 = g.read()


text1 = word_tokenize(file1)
text2 = word_tokenize(file2)

# all tags and words
tagged1 = nltk.pos_tag(text1)
tagged2 = nltk.pos_tag(text2)
# for verb, sing. present, non-3d take

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# I don't really see the point of looking at the copied verbs
# look at the meaning
# if i look at cc like and or then and stuff.
# they wont have any meaining at all.
# plus they would have been found at TF-iDF
# but lets do this
# first find percentages of matched part_Of_speech
# then do the meaning wise
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
CC1 = list()
CC2 = list()

all_CC1 = [item for item in tagged1 if item[1] == 'CC']
all_CC2 = [item for item in tagged2 if item[1] == 'CC']

# print(all_CC1)
# print(all_CC2)

for x in all_CC1:
	# print(x[0])
	if(x[0] in CC1):
		++skipcount
		# print('skipped')
	else:
		CC1.append(x[0])

# print(CC1)

for x in all_CC2:
	# print(x[0])
	if(x[0] in CC2):
		++skipcount
		# print('skipped')
	else:
		CC2.append(x[0])

# print(CC2)

copiedCC = []
for x in all_CC1:
	if x in all_CC2:
		copiedCC.append(x[0])
		# print("copied",x)
# print("copied coordinating conjunction are :",copiedCC)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CD1 = list()
CD2 = list()

all_CD1 = [item for item in tagged1 if item[1] == 'CD']
all_CD2 = [item for item in tagged2 if item[1] == 'CD']

# print(all_CD1)
# print(all_CD2)

for x in all_CD1:
	# print(x[0])
	if(x[0] in CD1):
		++skipcount
		# print('skipped')
	else:
		CD1.append(x[0])

# print(CD1)

for x in all_CD2:
	# print(x[0])
	if(x[0] in CD2):
		++skipcount
		# print('skipped')
	else:
		CD2.append(x[0])

# print(CD2)

copiedCD = []
for x in all_CD1:
	if x in all_CD2:
		copiedCD.append(x[0])
		# print("copied",x)
# print("copied cardinal digit are :",copiedCD)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DT1 = list()
DT2 = list()

all_DT1 = [item for item in tagged1 if item[1] == 'DT']
all_DT2 = [item for item in tagged2 if item[1] == 'DT']

# print(all_DT1)
# print(all_DT2)

for x in all_DT1:
	# print(x[0])
	if(x[0] in DT1):
		++skipcount
		# print('skipped')
	else:
		DT1.append(x[0])

# print(DT1)

for x in all_DT2:
	# print(x[0])
	if(x[0] in DT2):
		++skipcount
		# print('skipped')
	else:
		DT2.append(x[0])

# print(DT2)

copiedDT = []
for x in all_DT1:
	if x in all_DT2:
		copiedDT.append(x[0])
		# print("copied",x)
# print("copied determiner are :",copiedDT)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EX1 = list()
EX2 = list()

all_EX1 = [item for item in tagged1 if item[1] == 'EX']
all_EX2 = [item for item in tagged2 if item[1] == 'EX']

# print(all_EX1)
# print(all_EX2)

for x in all_EX1:
	# print(x[0])
	if(x[0] in EX1):
		++skipcount
		# print('skipped')
	else:
		EX1.append(x[0])

# print(EX1)

for x in all_EX2:
	# print(x[0])
	if(x[0] in EX2):
		++skipcount
		# print('skipped')
	else:
		EX2.append(x[0])

# print(EX2)

copiedEX = []
for x in all_EX1:
	if x in all_EX2:
		copiedEX.append(x[0])
		# print("copied",x)
# print("copied existential there are :",copiedEX)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FW1 = list()
FW2 = list()

all_FW1 = [item for item in tagged1 if item[1] == 'FW']
all_FW2 = [item for item in tagged2 if item[1] == 'FW']

# print(all_FW1)
# print(all_FW2)

for x in all_FW1:
	# print(x[0])
	if(x[0] in FW1):
		++skipcount
		# print('skipped')
	else:
		FW1.append(x[0])

# print(FW1)

for x in all_FW2:
	# print(x[0])
	if(x[0] in FW2):
		++skipcount
		# print('skipped')
	else:
		FW2.append(x[0])

# print(FW2)

copiedFW = []
for x in all_FW1:
	if x in all_FW2:
		copiedFW.append(x[0])
		# print("copied",x)
# print("copied foreign word are :",copiedFW)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IN1 = list()
IN2 = list()

all_IN1 = [item for item in tagged1 if item[1] == 'IN']
all_IN2 = [item for item in tagged2 if item[1] == 'IN']

# print(all_IN1)
# print(all_IN2)

for x in all_IN1:
	# print(x[0])
	if(x[0] in IN1):
		++skipcount
		# print('skipped')
	else:
		IN1.append(x[0])

# print(IN1)

for x in all_IN2:
	# print(x[0])
	if(x[0] in IN2):
		++skipcount
		# print('skipped')
	else:
		IN2.append(x[0])

# print(IN2)

copiedIN = []
for x in all_IN1:
	if x in all_IN2:
		copiedIN.append(x[0])
		# print("copied",x)
# print("copied preposition/subordinating conjunction are :",copiedIN)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

JJ1 = list()
JJ2 = list()

all_JJ1 = [item for item in tagged1 if item[1] == 'JJ']
all_JJ2 = [item for item in tagged2 if item[1] == 'JJ']

# print(all_JJ1)
# print(all_JJ2)

for x in all_JJ1:
	# print(x[0])
	if(x[0] in JJ1):
		++skipcount
		# print('skipped')
	else:
		JJ1.append(x[0])

# print(JJ1)

for x in all_JJ2:
	# print(x[0])
	if(x[0] in JJ2):
		++skipcount
		# print('skipped')
	else:
		JJ2.append(x[0])

# print(JJ2)

copiedJJ = []
for x in all_JJ1:
	if x in all_JJ2:
		copiedJJ.append(x[0])
		# print("copied",x)
# print("copied adjective are :",copiedJJ)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

JJR1 = list()
JJR2 = list()

all_JJR1 = [item for item in tagged1 if item[1] == 'JJR']
all_JJR2 = [item for item in tagged2 if item[1] == 'JJR']

# print(all_JJR1)
# print(all_JJR2)

for x in all_JJR1:
	# print(x[0])
	if(x[0] in JJR1):
		++skipcount
		# print('skipped')
	else:
		JJR1.append(x[0])

# print(JJR1)

for x in all_JJR2:
	# print(x[0])
	if(x[0] in JJR2):
		++skipcount
		# print('skipped')
	else:
		JJR2.append(x[0])

# print(JJR2)

copiedJJR = []
for x in all_JJR1:
	if x in all_JJR2:
		copiedJJR.append(x[0])
		# print("copied",x)
# print("copied adjective, comparative are :",copiedJJR)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

JJS1 = list()
JJS2 = list()

all_JJS1 = [item for item in tagged1 if item[1] == 'JJS']
all_JJS2 = [item for item in tagged2 if item[1] == 'JJS']

# print(all_JJS1)
# print(all_JJS2)

for x in all_JJS1:
	# print(x[0])
	if(x[0] in JJS1):
		++skipcount
		# print('skipped')
	else:
		JJS1.append(x[0])

# print(JJS1)

for x in all_JJS2:
	# print(x[0])
	if(x[0] in JJS2):
		++skipcount
		# print('skipped')
	else:
		JJS2.append(x[0])

# print(JJS2)

copiedJJS = []
for x in all_JJS1:
	if x in all_JJS2:
		copiedJJS.append(x[0])
		# print("copied",x)
# print("copied adjective, superlative are :",copiedJJS)




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LS1 = list()
LS2 = list()

all_LS1 = [item for item in tagged1 if item[1] == 'LS']
all_LS2 = [item for item in tagged2 if item[1] == 'LS']

# print(all_LS1)
# print(all_LS2)

for x in all_LS1:
	# print(x[0])
	if(x[0] in LS1):
		++skipcount
		# print('skipped')
	else:
		LS1.append(x[0])

# print(LS1)

for x in all_LS2:
	# print(x[0])
	if(x[0] in LS2):
		++skipcount
		# print('skipped')
	else:
		LS2.append(x[0])

# print(LS2)

copiedLS = []
for x in all_LS1:
	if x in all_LS2:
		copiedLS.append(x[0])
		# print("copied",x)
# print("copied list marker are :",copiedLS)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MD1 = list()
MD2 = list()

all_MD1 = [item for item in tagged1 if item[1] == 'MD']
all_MD2 = [item for item in tagged2 if item[1] == 'MD']

# print(all_MD1)
# print(all_MD2)

for x in all_MD1:
	# print(x[0])
	if(x[0] in MD1):
		++skipcount
		# print('skipped')
	else:
		MD1.append(x[0])

# print(MD1)

for x in all_MD2:
	# print(x[0])
	if(x[0] in MD2):
		++skipcount
		# print('skipped')
	else:
		MD2.append(x[0])

# print(MD2)

copiedMD = []
for x in all_MD1:
	if x in all_MD2:
		copiedMD.append(x[0])
		# print("copied",x)
# print("copied modal are :",copiedMD)





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NN1 = list()
NN2 = list()

all_NN1 = [item for item in tagged1 if item[1] == 'NN']
all_NN2 = [item for item in tagged2 if item[1] == 'NN']

# print(all_NN1)
# print(all_NN2)

for x in all_NN1:
	# print(x[0])
	if(x[0] in NN1):
		++skipcount
		# print('skipped')
	else:
		NN1.append(x[0])

# print(NN1)

for x in all_NN2:
	# print(x[0])
	if(x[0] in NN2):
		++skipcount
		# print('skipped')
	else:
		NN2.append(x[0])

# print(NN2)

copiedNN = []
for x in all_NN1:
	if x in all_NN2:
		copiedNN.append(x[0])
		# print("copied",x)
# print("copied noun, singular are :",copiedNN)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NNS1 = list()
NNS2 = list()

all_NNS1 = [item for item in tagged1 if item[1] == 'NNS']
all_NNS2 = [item for item in tagged2 if item[1] == 'NNS']

# print(all_NNS1)
# print(all_NNS2)

for x in all_NNS1:
	# print(x[0])
	if(x[0] in NNS1):
		++skipcount
		# print('skipped')
	else:
		NNS1.append(x[0])

# print(NNS1)

for x in all_NNS2:
	# print(x[0])
	if(x[0] in NNS2):
		++skipcount
		# print('skipped')
	else:
		NNS2.append(x[0])

# print(NNS2)

copiedNNS = []
for x in all_NNS1:
	if x in all_NNS2:
		copiedNNS.append(x[0])
		# print("copied",x)
# print("copied noun plural are :",copiedNNS)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NNP1 = list()
NNP2 = list()

all_NNP1 = [item for item in tagged1 if item[1] == 'NNP']
all_NNP2 = [item for item in tagged2 if item[1] == 'NNP']

# print(all_NNP1)
# print(all_NNP2)

for x in all_NNP1:
	# print(x[0])
	if(x[0] in NNP1):
		++skipcount
		# print('skipped')
	else:
		NNP1.append(x[0])

# print(NNP1)

for x in all_NNP2:
	# print(x[0])
	if(x[0] in NNP2):
		++skipcount
		# print('skipped')
	else:
		NNP2.append(x[0])

# print(NNP2)

copiedNNP = []
for x in all_NNP1:
	if x in all_NNP2:
		copiedNNP.append(x[0])
		# print("copied",x)
# print("copied proper noun, singular are :",copiedNNP)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NNPS1 = list()
NNPS2 = list()

all_NNPS1 = [item for item in tagged1 if item[1] == 'NNPS']
all_NNPS2 = [item for item in tagged2 if item[1] == 'NNPS']

# print(all_NNPS1)
# print(all_NNPS2)

for x in all_NNPS1:
	# print(x[0])
	if(x[0] in NNPS1):
		++skipcount
		# print('skipped')
	else:
		NNPS1.append(x[0])

# print(NNPS1)

for x in all_NNPS2:
	# print(x[0])
	if(x[0] in NNPS2):
		++skipcount
		# print('skipped')
	else:
		NNPS2.append(x[0])

# print(NNPS2)

copiedNNPS = []
for x in all_NNPS1:
	if x in all_NNPS2:
		copiedNNPS.append(x[0])
		# print("copied",x)
# print("copied proper noun, plural are :",copiedNNPS)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PDT1 = list()
PDT2 = list()

all_PDT1 = [item for item in tagged1 if item[1] == 'PDT']
all_PDT2 = [item for item in tagged2 if item[1] == 'PDT']

# print(all_PDT1)
# print(all_PDT2)

for x in all_PDT1:
	# print(x[0])
	if(x[0] in PDT1):
		++skipcount
		# print('skipped')
	else:
		PDT1.append(x[0])

# print(PDT1)

for x in all_PDT2:
	# print(x[0])
	if(x[0] in PDT2):
		++skipcount
		# print('skipped')
	else:
		PDT2.append(x[0])

# print(PDT2)

copiedPDT = []
for x in all_PDT1:
	if x in all_PDT2:
		copiedPDT.append(x[0])
		# print("copied",x)
# print("copied predeterminer are :",copiedPDT)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

POS1 = list()
POS2 = list()

all_POS1 = [item for item in tagged1 if item[1] == 'POS']
all_POS2 = [item for item in tagged2 if item[1] == 'POS']

# print(all_POS1)
# print(all_POS2)

for x in all_POS1:
	# print(x[0])
	if(x[0] in POS1):
		++skipcount
		# print('skipped')
	else:
		POS1.append(x[0])

# print(POS1)

for x in all_POS2:
	# print(x[0])
	if(x[0] in POS2):
		++skipcount
		# print('skipped')
	else:
		POS2.append(x[0])

# print(POS2)

copiedPOS = []
for x in all_POS1:
	if x in all_POS2:
		copiedPOS.append(x[0])
		# print("copied",x)
# print("copied ossessive ending are :",copiedPOS)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PRP1 = list()
PRP2 = list()

all_PRP1 = [item for item in tagged1 if item[1] == 'PRP']
all_PRP2 = [item for item in tagged2 if item[1] == 'PRP']

# print(all_PRP1)
# print(all_PRP2)

for x in all_PRP1:
	# print(x[0])
	if(x[0] in PRP1):
		++skipcount
		# print('skipped')
	else:
		PRP1.append(x[0])

# print(PRP1)

for x in all_PRP2:
	# print(x[0])
	if(x[0] in PRP2):
		++skipcount
		# print('skipped')
	else:
		PRP2.append(x[0])

# print(POS2)

copiedPRP = []
for x in all_PRP1:
	if x in all_PRP2:
		copiedPRP.append(x[0])
		# print("copied",x)
# print("copied personal pronoun are :",copiedPRP)





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PRPD1 = list()
PRPD2 = list()

all_PRPD1 = [item for item in tagged1 if item[1] == 'PRP$']
all_PRPD2 = [item for item in tagged2 if item[1] == 'PRP$']

# print(all_PRPD1)
# print(all_PRPD2)

for x in all_PRPD1:
	# print(x[0])
	if(x[0] in PRPD1):
		++skipcount
		# print('skipped')
	else:
		PRPD1.append(x[0])

# print(PRPD1)

for x in all_PRPD2:
	# print(x[0])
	if(x[0] in PRPD2):
		++skipcount
		# print('skipped')
	else:
		PRPD2.append(x[0])

# print(PRPD2)

copiedPRPD = []
for x in all_PRPD1:
	if x in all_PRPD2:
		copiedPRPD.append(x[0])
		# print("copied",x)
# print("copied possessive pronoun are :",copiedPRPD)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RB1 = list()
RB2 = list()

all_RB1 = [item for item in tagged1 if item[1] == 'RB']
all_RB2 = [item for item in tagged2 if item[1] == 'RB']

# print(all_RB1)
# print(all_RB2)

for x in all_RB1:
	# print(x[0])
	if(x[0] in RB1):
		++skipcount
		# print('skipped')
	else:
		RB1.append(x[0])

# print(RB1)

for x in all_RB2:
	# print(x[0])
	if(x[0] in RB2):
		++skipcount
		# print('skipped')
	else:
		RB2.append(x[0])

# print(RB2)

copiedRB = []
for x in all_RB1:
	if x in all_RB2:
		copiedRB.append(x[0])
		# print("copied",x)
# print("copied adverb are :",copiedRB)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RBR1 = list()
RBR2 = list()

all_RBR1 = [item for item in tagged1 if item[1] == 'RBR']
all_RBR2 = [item for item in tagged2 if item[1] == 'RBR']

# print(all_RBR1)
# print(all_RBR2)

for x in all_RBR1:
	# print(x[0])
	if(x[0] in RBR1):
		++skipcount
		# print('skipped')
	else:
		RBR1.append(x[0])

# print(RBR1)

for x in all_RBR2:
	# print(x[0])
	if(x[0] in RBR2):
		++skipcount
		# print('skipped')
	else:
		RBR2.append(x[0])

# print(RBR2)

copiedRBR = []
for x in all_RBR1:
	if x in all_RBR2:
		copiedRBR.append(x[0])
		# print("copied",x)
# print("copied adverb comparative are :",copiedRBR)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RBS1 = list()
RBS2 = list()

all_RBS1 = [item for item in tagged1 if item[1] == 'RBS']
all_RBS2 = [item for item in tagged2 if item[1] == 'RBS']

# print(all_RBR1)
# print(all_RBR2)

for x in all_RBS1:
	# print(x[0])
	if(x[0] in RBS1):
		++skipcount
		# print('skipped')
	else:
		RBS1.append(x[0])

# print(RBS1)

for x in all_RBS2:
	# print(x[0])
	if(x[0] in RBS2):
		++skipcount
		# print('skipped')
	else:
		RBS2.append(x[0])

# print(RBS2)

copiedRBS = []
for x in all_RBS1:
	if x in all_RBS2:
		copiedRBS.append(x[0])
		# print("copied",x)
# print("copied adverb, superlative are :",copiedRBS)





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RP1 = list()
RP2 = list()

all_RP1 = [item for item in tagged1 if item[1] == 'RP']
all_RP2 = [item for item in tagged2 if item[1] == 'RP']

# print(all_RP1)
# print(all_RP2)

for x in all_RP1:
	# print(x[0])
	if(x[0] in RP1):
		++skipcount
		# print('skipped')
	else:
		RP1.append(x[0])

# print(RP1)

for x in all_RP2:
	# print(x[0])
	if(x[0] in RP2):
		++skipcount
		# print('skipped')
	else:
		RP2.append(x[0])

# print(RP2)

copiedRP = []
for x in all_RP1:
	if x in all_RP2:
		copiedRP.append(x[0])
		# print("copied",x)
# print("copied particle are :",copiedRP)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TO1 = list()
TO2 = list()

all_TO1 = [item for item in tagged1 if item[1] == 'TO']
all_TO2 = [item for item in tagged2 if item[1] == 'TO']

# print(all_TO1)
# print(all_TO2)

for x in all_TO1:
	# print(x[0])
	if(x[0] in TO1):
		++skipcount
		# print('skipped')
	else:
		TO1.append(x[0])

# print(TO1)

for x in all_TO2:
	# print(x[0])
	if(x[0] in TO2):
		++skipcount
		# print('skipped')
	else:
		TO2.append(x[0])

# print(TO2)

copiedTO = []
for x in all_TO1:
	if x in all_TO2:
		copiedTO.append(x[0])
		# print("copied",x)
# print("copied to go 'to' the store. are :",copiedTO)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

UH1 = list()
UH2 = list()

all_UH1 = [item for item in tagged1 if item[1] == 'UH']
all_UH2 = [item for item in tagged2 if item[1] == 'UH']

# print(all_UH1)
# print(all_UH2)

for x in all_UH1:
	# print(x[0])
	if(x[0] in UH1):
		++skipcount
		# print('skipped')
	else:
		UH1.append(x[0])

# print(TO1)

for x in all_UH2:
	# print(x[0])
	if(x[0] in UH2):
		++skipcount
		# print('skipped')
	else:
		UH2.append(x[0])

# print(TO2)

copiedUH = []
for x in all_UH1:
	if x in all_UH2:
		copiedUH.append(x[0])
		# print("copied",x)
# print("copied interjection are :",copiedUH)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VB1 = list()
VB2 = list()

all_VB1 = [item for item in tagged1 if item[1] == 'VB']
all_VB2 = [item for item in tagged2 if item[1] == 'VB']

# print(all_VB1)
# print(all_VB2)

for x in all_VB1:
	# print(x[0])
	if(x[0] in VB1):
		++skipcount
		# print('skipped')
	else:
		VB1.append(x[0])

# print(VB1)

for x in all_VB2:
	# print(x[0])
	if(x[0] in VB2):
		++skipcount
		# print('skipped')
	else:
		VB2.append(x[0])

# print(VB2)

copiedVB = []
for x in all_VB1:
	if x in all_VB2:
		copiedVB.append(x[0])
		# print("copied",x)
# print("copied verb, base form	 are :",copiedVB)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VBD1 = list()
VBD2 = list()

all_VBD1 = [item for item in tagged1 if item[1] == 'VBD']
all_VBD2 = [item for item in tagged2 if item[1] == 'VBD']

# print(all_VBD1)
# print(all_VBD2)

for x in all_VBD1:
	# print(x[0])
	if(x[0] in VBD1):
		++skipcount
		# print('skipped')
	else:
		VBD1.append(x[0])

# print(VBD1)

for x in all_VBD2:
	# print(x[0])
	if(x[0] in VBD2):
		++skipcount
		# print('skipped')
	else:
		VBD2.append(x[0])

# print(VBD2)

copiedVBD = []
for x in all_VBD1:
	if x in all_VBD2:
		copiedVBD.append(x[0])
		# print("copied",x)
# print("copied verb, past tense are :",copiedVBD)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VBG1 = list()
VBG2 = list()

all_VBG1 = [item for item in tagged1 if item[1] == 'VBG']
all_VBG2 = [item for item in tagged2 if item[1] == 'VBG']

# print(all_VBG1)
# print(all_VBG2)

for x in all_VBG1:
	# print(x[0])
	if(x[0] in VBG1):
		++skipcount
		# print('skipped')
	else:
		VBG1.append(x[0])

# print(VBG1)

for x in all_VBG2:
	# print(x[0])
	if(x[0] in VBG2):
		++skipcount
		# print('skipped')
	else:
		VBG2.append(x[0])

# print(VBG2)

copiedVBG = []
for x in all_VBG1:
	if x in all_VBG2:
		copiedVBG.append(x[0])
		# print("copied",x)
# print("copied verb, gerund/present participle are :",copiedVBG)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VBN1 = list()
VBN2 = list()

all_VBN1 = [item for item in tagged1 if item[1] == 'VBN']
all_VBN2 = [item for item in tagged2 if item[1] == 'VBN']

# print(all_VBN1)
# print(all_VBN2)

for x in all_VBN1:
	# print(x[0])
	if(x[0] in VBN1):
		++skipcount
		# print('skipped')
	else:
		VBN1.append(x[0])

# print(VBN1)

for x in all_VBN2:
	# print(x[0])
	if(x[0] in VBN2):
		++skipcount
		# print('skipped')
	else:
		VBN2.append(x[0])

# print(VBN2)

copiedVBN = []
for x in all_VBN1:
	if x in all_VBN2:
		copiedVBN.append(x[0])
		# print("copied",x)
# print("copied verb, past participle	 are :",copiedVBN)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VBP1 = list()
VBP2 = list()

all_VBP1 = [item for item in tagged1 if item[1] == 'VBP']
all_VBP2 = [item for item in tagged2 if item[1] == 'VBP']

# print(all_VBP1)
# print(all_VBP2)

for x in all_VBP1:
	# print(x[0])
	if(x[0] in VBP1):
		++skipcount
		# print('skipped')
	else:
		VBP1.append(x[0])

# print(VBP1)

for x in all_VBP2:
	# print(x[0])
	if(x[0] in VBP2):
		++skipcount
		# print('skipped')
	else:
		VBP2.append(x[0])

# print(VBP2)

copiedVBP = []
for x in all_VBP1:
	if x in all_VBP2:
		copiedVBP.append(x[0])
		# print("copied",x)
# print("copied verb, sing. present, non-3d are :",copiedVBP)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VBZ1 = list()
VBZ2 = list()

all_VBZ1 = [item for item in tagged1 if item[1] == 'VBZ']
all_VBZ2 = [item for item in tagged2 if item[1] == 'VBZ']

# print(all_VBZ1)
# print(all_VBZ2)

for x in all_VBZ1:
	# print(x[0])
	if(x[0] in VBZ1):
		++skipcount
		# print('skipped')
	else:
		VBZ1.append(x[0])

# print(VBZ1)

for x in all_VBZ2:
	# print(x[0])
	if(x[0] in VBZ2):
		++skipcount
		# print('skipped')
	else:
		VBZ2.append(x[0])

# print(VBN2)

copiedVBZ = []
for x in all_VBZ1:
	if x in all_VBZ2:
		copiedVBZ.append(x[0])
		# print("copied",x)
# print("copied verb, 3rd person are :",copiedVBZ)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WDT1 = list()
WDT2 = list()

all_WDT1 = [item for item in tagged1 if item[1] == 'WDT']
all_WDT2 = [item for item in tagged2 if item[1] == 'WDT']

# print(all_WDT1)
# print(all_WDT2)

for x in all_WDT1:
	# print(x[0])
	if(x[0] in WDT1):
		++skipcount
		# print('skipped')
	else:
		WDT1.append(x[0])

# print(WDT1)

for x in all_WDT2:
	# print(x[0])
	if(x[0] in WDT2):
		++skipcount
		# print('skipped')
	else:
		WDT2.append(x[0])

# print(WDT2)

copiedWDT = []
for x in all_WDT1:
	if x in all_WDT2:
		copiedWDT.append(x[0])
		# print("copied",x)
# print("copied wh-determiner are :",copiedWDT)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WP1 = list()
WP2 = list()

all_WP1 = [item for item in tagged1 if item[1] == 'WP']
all_WP2 = [item for item in tagged2 if item[1] == 'WP']

# print(all_WP1)
# print(all_WP2)

for x in all_WP1:
	# print(x[0])
	if(x[0] in WP1):
		++skipcount
		# print('skipped')
	else:
		WP1.append(x[0])

# print(WP1)

for x in all_WP2:
	# print(x[0])
	if(x[0] in WP2):
		++skipcount
		# print('skipped')
	else:
		WP2.append(x[0])

# print(WP2)

copiedWP = []
for x in all_WP1:
	if x in all_WP2:
		copiedWP.append(x[0])
		# print("copied",x)
# print("copied wh-pronoun are :",copiedWP)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WPD1 = list()
WPD2 = list()

all_WPD1 = [item for item in tagged1 if item[1] == 'WP$']
all_WPD2 = [item for item in tagged2 if item[1] == 'WP$']

# print(all_WPD1)
# print(all_WPD2)

for x in all_WPD1:
	# print(x[0])
	if(x[0] in WPD1):
		++skipcount
		# print('skipped')
	else:
		WPD1.append(x[0])

# print(WPD1)

for x in all_WPD2:
	# print(x[0])
	if(x[0] in WPD2):
		++skipcount
		# print('skipped')
	else:
		WPD2.append(x[0])

# print(WPD2)

copiedWPD = []
for x in all_WPD1:
	if x in all_WPD2:
		copiedWPD.append(x[0])
		# print("copied",x)
# print("copied possessive wh-pronoun are :",copiedWPD)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

WRB1 = list()
WRB2 = list()

all_WRB1 = [item for item in tagged1 if item[1] == 'WRB']
all_WRB2 = [item for item in tagged2 if item[1] == 'WRB']

# print(all_WRB1)
# print(all_WRB2)

for x in all_WRB1:
	# print(x[0])
	if(x[0] in WRB1):
		++skipcount
		# print('skipped')
	else:
		WRB1.append(x[0])

# print(WRB1)

for x in all_WRB2:
	# print(x[0])
	if(x[0] in WRB2):
		++skipcount
		# print('skipped')
	else:
		WRB2.append(x[0])

# print(WRB2)

copiedWRB = []
for x in all_WRB1:
	if x in all_WRB2:
		copiedWRB.append(x[0])
		# print("copied",x)
# print("copied wh-abverb are :",copiedWRB)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print(VB1)
list1 = VB1
# print(list1)
list2 = VB2
newlist = []


for word1 in list1:
    for word2 in list2:
        wordFromList1 = wordnet.synsets(word1)
        wordFromList2 = wordnet.synsets(word2)
        # print(wordFromList1)
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
 
print(len(thelist))
print(thelist)
addition = 0
maximum = list()
for element in thelist:
	addition = addition + element
	if element > 0.5:
		maximum.append(element)
print("The score ",addition / 12)
print("The values above 0.5 are:")
print(maximum)