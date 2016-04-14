import sys
import os
import codecs

sarcasticpath = "/Users/sidhesh/Documents/Github/Team-MissionNLP/tweet-fetcher/Sarcastic"
targetFileNamenonsarcastic = '/Users/sidhesh/Documents/Github/Team-MissionNLP/tweet-fetcher/Non-Sarcastic/nonSarcasticTweets.txt'
targetFileNamedev = '/Users/sidhesh/Documents/Github/Team-MissionNLP/tweet-fetcher/Non-Sarcastic/dev.txt'
nonsarcassticsourcepath = '/Users/sidhesh/Documents/Github/Team-MissionNLP/tweet-fetcher/Non-Sarcastic/hi-search-1.txt'
f1 = codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/tweet-fetcher/Sarcastic/sarcasticTweets.txt", "w+", "utf-8")     

for root, dirs, files in os.walk(sarcasticpath):
    for file in files:
        if file.endswith(".txt"):
            with codecs.open(os.path.join(root, file), "r","utf-8") as sourceFile:
                lines=sourceFile.readlines()
                for line in lines: 
                    f1.write(line)
sourceFile.close()
f1.close() 
                   

with codecs.open(nonsarcassticsourcepath, "r","utf-8") as sourceFile:
    with codecs.open(targetFileNamenonsarcastic, "w", "utf-8") as targetFile:
        for i in xrange(13500):
            line=sourceFile.readline()
            targetFile.write(line)
    targetFile.close() 
sourceFile.close()

with codecs.open(nonsarcassticsourcepath, "r","utf-8") as sourceFile:      
    with codecs.open(targetFileNamedev, "w", "utf-8") as targetFile:
        for i in xrange(13501,18500,1):
            line=sourceFile.readline()
            targetFile.write(line)               
sourceFile.close()
targetFile.close()

with codecs.open("/Users/sidhesh/Documents/Github/Team-MissionNLP/tweet-fetcher/Sarcastic/sarcasticTweets.txt", "r","utf-8") as sourceFile: 
    with codecs.open(targetFileNamedev, "a", "utf-8") as targetFile:     
        for i in xrange(5000):
            line=sourceFile.readline()
            targetFile.write(line)
        targetFile.close()               
sourceFile.close()          
          
            
                