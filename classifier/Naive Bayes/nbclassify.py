import os,string,json,math,sys

stopwords=[]
vocab=set()
def readModel():
    with open('nbmodel.txt', 'rb') as handle:
        data = json.loads(handle.read())
    return data

def fileRead(file):
        
    filename=file
    with open(filename) as f:
    	content = f.readlines()
    return content

def NBtest(content,f1,f2):
    output= open(f1,"w")
    output2= open(f2,"w")
    score1=math.log(0.44)
    score2=math.log(0.56)
    for s in content:
	score1=math.log(0.44)
	score2=math.log(0.56)
    	output.write(s)
	tweet=s.split()
	for word in tweet:
		word = unicode(word, "utf-8")		
		if word in model:
			#print 'found: ',word
        		score1+=math.log(model[word][0])
                        score2+=math.log(model[word][1])
        if score1> score2:
		print 'inside'
		#print s,'SARCASTIC'
        	output.write('/SARCASTIC')
		output2.write('1')
        else:
		#print 'NON_SARCASTIC'
    		output.write('/NON_SARCASTIC')
		output2.write('0')
        output.write('\n')
	output2.write('\n')
    output.close()
    output2.close()
    return 

data=readModel()
model=data['MODEL']
content=fileRead('/home/swanand/nlpProject/Naive Bayes/data/dev_sarcastic_proc.txt')
f1="/home/swanand/nlpProject/Naive Bayes/data/outputs/nboutput_sarcastic.txt"
f2="/home/swanand/nlpProject/Naive Bayes/data/outputs/nbtags_sarcastic.txt"
NBtest(content,f1,f2)
content=fileRead('/home/swanand/nlpProject/Naive Bayes/data/dev_nonsarcastic_proc.txt')
f1="/home/swanand/nlpProject/Naive Bayes/data/outputs/nboutput_nonsarcastic.txt"
f2="/home/swanand/nlpProject/Naive Bayes/data/outputs/nbtags_nonsarcastic.txt"
NBtest(content,f1,f2)
