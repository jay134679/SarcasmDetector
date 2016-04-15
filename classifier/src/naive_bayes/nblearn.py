import os,string,json,codecs

vocab=set()
sarcasmDict={}
nonSarcasmDict={}
content=[]


def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content
sarcasm=0
nonSarcasm=0
    
def trainNB(content,classFlag):
    global sarcasm
    global nonSarcasm
    exclude=set(string.punctuation)
    for s in content:	
	s = ''.join(ch for ch in s if ch not in exclude)
    	tweet=s.split()
	for word in tweet:
		vocab.add(word)
                if classFlag==1:
                	sarcasm+=1
                        if word in sarcasmDict:
                                sarcasmDict[word]=sarcasmDict[word]+1
                        else:
                                sarcasmDict[word]=1
                else:
                        nonSarcasm+=1
                        if word in nonSarcasmDict:
                                 nonSarcasmDict[word]=nonSarcasmDict[word]+1
                        else:
                                 nonSarcasmDict[word]=1
    return
    
def writeModel():
    global sarcasm
    global nonSarcasm
    vocabList=list(vocab)
    model={}
    for word in vocab:
        classList=[]
        if word in sarcasmDict:
            prob=1.0*(sarcasmDict[word]+1)/(sarcasm+len(vocab))
        else:
            prob=1.0/(sarcasm+len(vocab))
        classList.append(prob)
        if word in nonSarcasmDict:
            prob=1.0*(nonSarcasmDict[word]+1)/(nonSarcasm+len(vocab))
	else:
            prob=1.0/(nonSarcasm+len(vocab))
	classList.append(prob)        
	model[word]=classList
    #print model    
    with codecs.open('nbmodel.txt','w',encoding='utf8') as handle:
	s1=len(sarcasmDict)
	s2=len(nonSarcasmDict)
	data={'MODEL':model,'SARCASM_LENGTH':s1,'NONSARCASM_LENGTH':s2}
	json.dump(data, handle)

    return

content=fileRead('/home/swanand/nlpProject/Naive Bayes/data/nonsarcastic_proc.txt')
trainNB(content,0)
content=fileRead('/home/swanand/nlpProject/Naive Bayes/data/sarcastic_proc.txt')
trainNB(content,1)
print 'Vocab Length:'+ str(len(vocab))
print 'Sarcasm Vocab Length:' +str(len(sarcasmDict))
print 'Non Sarcasm Length:' +str(len(nonSarcasmDict))
print str(sarcasm)
print str(nonSarcasm)
writeModel()

