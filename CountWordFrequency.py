def countFreq(words):
    if words[-1] == '.':
        words = words[0:len(words)-1]
        
    if words in dictWord:
        dictWord[words] +=-1
    else:
        dictWord.update({words:1})
    
input = " which one is better Python 2 or Python 3"

dictWord = {}
listWords = input.split()

for words in listWords:
    countFreq(words)
    
for allwords in dictWord:
    print(allwords, " : ", dictWord[allwords] )