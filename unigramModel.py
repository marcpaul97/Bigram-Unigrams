import re

def readFiles(files):
    realList = []
    with open(files, "r") as f:   
        temp = [re.split(r'\s+', line.rstrip('\n')) for line in f]
    for i in range(len(temp[0])):
        temp[0][i] = re.sub('([.,!?])', r' \1 ', temp[0][i])
        temp[0][i] = re.sub('\s{2,}', ' ', temp[0][i])
        temp[0][i] = temp[0][i].split()
    for i in range(len(temp[0])):
        for x in range(len(temp[0][i])):
            realList.append(temp[0][i][x])
    return realList
                

class Unigram:    
    
    def __init__(self, sentence, normalProb = True):
        self.unigramFrequency = dict()
        self.length = 0
        for s in sentence:
            self.unigramFrequency[s] = self.unigramFrequency.get(s, 0) + 1
            self.length = self.length + 1
        self.differentGrams = len(self.unigramFrequency)
        self.normalProb = normalProb
                
    
    def calculateProbability(self, word):
        top = self.unigramFrequency.get(word,0)
        bottom = self.length
        print(top)
        print(bottom)
        probability = float(top) / float(bottom)
        return probability
        
        
    def getNumberAppeared(self, word):
        print(word + " appears " + str(self.unigramFrequency.get(word, 0)) + " times")
        return
    
    def getBegining(self, sentence, word):
        count = 0
        for i in range(len(sentence) - 1):
            if(sentence[i + 1] == word and (sentence[i] == '.' or sentence[i] == '?' or sentence[i] == '!')):
                count = count + 1
        print(word + " at beginning " + str(count) + " time(s)")
        return
    
    def getNextWord(self, sentence, word):
        matching = []
        for i in range(len(sentence)):
            temp = sentence[i]
            if(temp == word and (i + 1) < len(sentence)):
                if(sentence[i + 1] not in matching):
                    matching.append([sentence[i + 1], 1])
                else:
                    matching[i][1] = matching[i][1] + 1
        for x in matching:
            print(word + " "+ x[0] + " " + str(x[1]) + " time(s)")
        return
    
    def getLastWord(self, sentence, word):
        endCount = 0
        for i in range(len(sentence) - 1):
            if((sentence[i + 1] == '.' or sentence[i + 1] == '?' or sentence[i + 1] == '!') and sentence[i] == word):
                endCount = endCount + 1
        print(word + " at the end " + str(endCount) + " time(s)")
        return
    
    def bigram(self, sentence, wordOne, wordTwo):
        count = 0
        oneCount = 0
        for i in range(len(sentence)):
            if(sentence[i] == wordOne):
                oneCount = oneCount + 1
            if((i + 1) < len(sentence) and sentence[i] == wordOne and sentence[i + 1] == wordTwo):
                count = count + 1
        print(wordOne + " " + wordTwo + " appear(s) " + str(count) + " time(s)")
        answer = float(count) / float(oneCount)
        print("The Probability of " + wordOne + " " + wordTwo + " is " + str(answer))
        return
        
    def trigram(self, sentence, wordOne, wordTwo, wordThree):
        oneCount = 0
        twoCount = 0
        threeCount = 0
        twotwocount = 0
        twothreecount = 0
        for i in range(len(sentence)):
            if(sentence[i] == wordOne):
                oneCount = oneCount + 1
            if(sentence[i] == wordTwo):
                twotwocount = twotwocount + 1
            if(sentence[i] == wordThree):
                twothreecount = twothreecount + 1
            if((i + 1) < len(sentence) and sentence[i] == wordOne and sentence[i + 1] == wordTwo):
                twoCount = twoCount + 1
            if((i + 2) < len(sentence) and sentence[i] == wordOne and sentence[i + 1] == wordTwo and sentence[i + 2] == wordThree):
                threeCount = threeCount + 1
        bAnswer = float(twoCount) / float(oneCount)
        tAnswer = float(threeCount) / float(twoCount)
        finalAnswer = float(bAnswer * tAnswer) / float(twothreecount)
        print(wordOne + " " + wordTwo + " " + wordThree + " appear(s) " + str(threeCount) + " time(s)")
        print("The Probability of " + wordOne + " " + wordTwo + " " + wordThree + " is " + str(finalAnswer))
