#Python program to create a text-based word guessing game
#Uses the vocab.txt file

import random 
import re
# Read the vocab file and create a list of words.
with open("vocab.txt", "r") as v:
    vocab=v.read().split("\n")
# Pick a random word on the vocab list as the answer.
answer_full = random.choice(vocab)
#split the answer into word and definition
answer_full = [answer_full.split(" ")[0].upper(), answer_full.split(".")[1]]
answer= answer_full[0]
answer_list = list(answer) # Change the answer into a list for easier processing.
#print "the secret answer is {0}".format(answer)
# Build the working answer:
working = ["_"]*len(answer)
print "The answer has {0} letters: {1}".format(len(answer)," ".join(working))
# Start guessing!
guessed = []
guess_count = 0
wrong_count = 0
while "".join(working) != answer:
    guess=raw_input("Guess a letter, any letter!\n")
    if len(guess) == 1 and guess.isalpha(): # make sure guess is a single letter
        guess=guess.upper()
        if guess in guessed: # make sure guess hasn't been guessed already
            print "You already guessed {0}, silly! Here are all the letters you've guessed: {1}".format(guess, ", ".join(sorted(guessed)))
        else:
            guess_count = guess_count + 1
            guessed.append(guess)
            if guess in answer:
                print "You guessed a correct letter!"
                replace_list = []
                for index, letter in enumerate(answer): # loop through the answer list to find the positions of the letter you guessed.                    
                    if letter==guess:
                        replace_list.append(index) # add the position of each letter to a list
                for position in replace_list: # fill in answers on working list
                    working[position] = guess
                if "".join(working) != answer:
                    print "Here's what you're working with: {0}\n".format(" ".join(working))
            else: # incorrect input
                print "Sorry, no {0}'s in the answer. Keep on guessing.".format(guess)
                wrong_count = wrong_count + 1
    else:
        print "That wasn't a single letter. Doh!"
if "".join(working) == answer: # solved
    print "You did it! The answer was {0}, and you got it in {1} guesses. You had {2} incorrect guesses".format(answer, guess_count, wrong_count)
    print "The definition of {0} is:{1}. You learned something!".format(answer, answer_full[1])
