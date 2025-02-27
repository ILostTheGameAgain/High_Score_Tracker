#Alec George Memory Game

#will create a random string of letters and numbers and let the user rewrite it when they no longer see it. If they get it correct, it gets longer


import random
import time

#import functions and variables to check highscore
from file_functions import *


#function to add a random character to answer
def add_letter(string):
    #variable for all possible characters to add
    possible_figures = "1234567890qwertyuiopasdfghjklzcvbnm"
    #add a random letter
    string += possible_figures [random.randint(0,len(possible_figures)-1)]
    return string


#main function
def main():
    #make variables for score and the string to guess
    score = 1
    answer = ""

    #while loop to run until the user fails
    while True:
        #add one character to answer
        answer = add_letter(answer)
        #show the answer for 5 seconds
        print(f"\n{answer}")
        time.sleep(3)
        print("\033c")

        #variable for the user's guess to what the string is
        guess = input("what was the string? ")
        if guess == answer:
            #if guess and answer are the same, increase score by 1 and add a letter
            score += 1
            print("\ncorrect!")
            time.sleep(1)
            print("\033c")
        else:
            #if they are not the same, quit
            print(f"\nincorrect. The string was {answer}")
            print(f"score: {score}")
            time.sleep(1)
            break
        
    check_highscore(score,"memory",highscores)


main()