'''
Created on Nov 17, 2015

@author: M-Hadad
'''

import random

## functions
def readFile(fileName):
    
    lis = [line.rstrip('\n') for line in open(fileName)]
    return list(map(lambda word:word.upper(),lis))

def printWord(w):
    for i in range(len(w)):
        print w[i]," ",
    print ""

def isComplete(w):
    for i in range(len(w)):
        if w[i] == '-':
            return False
    return True;    


def replaceChar(word1, word2, c):
    indx = 0
    indx = word1.find(c, indx)
    
    while indx != -1:
        word2 = word2[:indx] + word1[indx] + word2[indx+1:]
        
        indx +=1
        indx = word1.find(c, indx)                
            
    return word2
  
#### Code
fileName = "test.txt";
words = readFile(fileName)


while True: 
    
    wordNumber =  random.randrange(0, len(words))
    
    word = words[wordNumber]
    size = len(word)
    print "word " + word
    guessingWord = ''

    for i in range(size):
        guessingWord+= "-"


    print "Welcome in Hangman Game \n"
    print "Hangman is a paper and pencil guessing game for two or more players.\n\
     One player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters or numbers, \n\
     within a certain number of guesses."
     
    print "try to save a life.\n"
    print "Guess a word of ", size , " caharcters" 
    
    wrongChars = ""    
    numberOfTrials = 6;
    
    while numberOfTrials > 0:
        print "_________________________________________________________________"
        print "You have %s trials" % numberOfTrials
        print "Previous wrong characters: " + wrongChars
        
        print ""
        printWord(guessingWord) 
        print ""
        
        c = raw_input("Enter your guessing character ")            
        while len(c) !=1 or not c.isalpha() :
            print "Please enter one alphabetic character at a time"
            c = raw_input("Enter your guessing character ")
            
            
        c = c[0]
        c = c.upper()    
        
        #print "c: " + c 
        if word.find(c) != -1:
            
            if guessingWord.find(c) == -1:
                print "Good Job"
                guessingWord = replaceChar(word, guessingWord, c)
            
            else:
                print "You guessed this letter before, enter another one."
                continue
                
        else:
            if wrongChars.find(c) != -1:
                print "This is a wrong character you entered before, please enter another one."
                continue
            
            print "Too bad you lost a trial"
            numberOfTrials -=1
            wrongChars += " " + c
         
        if numberOfTrials == 0 :
            print "You killed the man \n***Game Over ***"  
            print "The correct word is: " + word
            break         
         
                
        if guessingWord.find("-") == -1:
            print "** Congratulation **  You saved the man's life"
            print "*******************************************"
            break   
            
            
        
        
    choice = raw_input("Play again? N(o), Y(es) ")   
    choice = choice.upper()
                
    while choice != "N" and choice != "Y":
        print "Please enter N or Y"
        choice = raw_input("Play again? N(o), Y(es) ")
                
    if choice == "N":
        break
print "Bye Bye"        
    