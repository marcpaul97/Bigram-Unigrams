from unigramModel import Unigram
from BigramModel import Bigram
import re

def readFiles(files):
    realList = []
    with open(files, "r") as f:   
        temp = [re.split(r'\s+', line.rstrip('\n')) for line in f]
    for i in range(len(temp[0])):
        temp[0][i] = re.sub('([.,!?-])', r' \1 ', temp[0][i])
        temp[0][i] = re.sub('\s{2,}', ' ', temp[0][i])
        temp[0][i] = temp[0][i].split()
    for i in range(len(temp[0])):
        for x in range(len(temp[0][i])):
            realList.append(temp[0][i][x])
    return realList

def main():
    file = readFiles("book.txt")
    number = 0
    while(number != 5):
        print("Pick an option:")
        print("1. Search for unigram")
        print("2. Search for bigram")
        print("3. Search for trigram")
        print("4. Sentence Probability")
        print("5. Exit")
        number = input()
        number = int(number)
        if(number == 1):
            word = input("Please give me a word.")
            obj = Unigram(file)
            obj.getNumberAppeared(word)
            obj.getBegining(file, word)
            obj.getNextWord(file, word)
            obj.getLastWord(file, word)
            print('\n')
            
        if(number == 2):
            obj = Unigram(file)
            wordOne = input("Please give me the first word.")
            wordTwo = input("Please give me the second word.")
            obj.bigram(file, wordOne, wordTwo)
            print('\n')
            
        if(number == 3):
            obj = Unigram(file)
            wordOne = input("Please give me the first word.")
            wordTwo = input("Please give me the second word.")
            wordThree = input("Please give me the third word.")
            obj.trigram(file, wordOne, wordTwo, wordThree)
            print('\n')
            
        if(number == 4):
            obj = Bigram(file)
            sentence = input("Please give me a sentence.")
            obj.calculateBProbability(sentence)
            print('\n')
            
        if(number > 5):
            print("Please pick a number between 1-5.")
            print('\n')
            
main()