import re
import math
from unigramModel import Unigram


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
        
class Bigram(Unigram):
        
    
    def __init__(self, sentences, rightNumber = False):
        self.sentences = sentences
        Unigram.__init__(self, self.sentences)
        self.bfreq = dict()
        self.differentWords = set()
        prev = None
        for s in sentences:
            if(prev != None):
                self.bfreq[(prev, s)] = self.bfreq.get((prev, s), 0) + 1
                self.differentWords.add((prev, s))
            prev = s
        self.differentWords = len(self.bfreq)

        
    def calculateProbability(self, previ, word):
        top = self.bfreq.get((previ, word), 0)
        bottom = self.unigramFrequency.get(word, 0)
        if(top == 0 or bottom == 0):
            return (1/self.differentWords)
        else:
            probability = float(top) / float(bottom)
            return probability
        
    def calculateBProbability(self, sentence, normal = True):
        pSum = 0
        prev = None
        realSentence = []
        sentence = sentence.split()
        for i in range(len(sentence)):
           sentence[i] = re.sub('([.,!?])', r' \1 ', sentence[i])
           sentence[i] = re.sub('\s{2,}', ' ', sentence[i])
           sentence[i] = sentence[i].split()
        for i in range(len(sentence)):
            if(len(sentence[i]) > 1):
                for x in range(len(sentence[i])):
                    realSentence.append(sentence[i][x])
            else:
                realSentence.append(sentence[i][0])
        for word in realSentence:
           if(prev != None):
                bprob = self.calculateProbability(prev, word)
                pSum = pSum + math.log(bprob, 2)
           prev = word
        answer = math.pow(2, pSum)
        print("The Probability of the sentence is " + str(answer))
        return
