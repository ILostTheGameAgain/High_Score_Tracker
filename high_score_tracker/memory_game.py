#Alec George Memory Game

#will create a random string of letters and numbers and let the user rewrite it when they no longer see it. If they get it correct, it gets longer


import random
import time

#import functions and variables to check highscore
from file_functions import *


#function to add a random character to answer
def add_letter(string):
    #variable for all possible characters to add
    possible_figures = "1234567890QWERTYIOPASDFGHJKLZXCVBNM"
    #add a random letter
    string += possible_figures [random.randint(0,len(possible_figures)-1)]
    return string


#main function
def memory():
    #introduction to the game
    print("\nWelcome to the memory game!\nA string of letters/numbers will appear for about 3 seconds.\nYour goal is to type the string of letters again after it disappears.\nAs you get more and more correct, the string will get longer and longer.\npress enter to start")
    input()
    #allow the user to play again using a while loop
    while True:
        #make variables for score and the string to guess
        score = 1
        answer = ""
        playing = True
        #while loop to run until the user fails
        while playing:
            #add one character to answer
            answer = add_letter(answer)
            #show the answer for 5 seconds
            print(f"\nstring:\n{answer}")
            time.sleep(3)
            print("\033c")

            #variable for the user's guess to what the string is
            guess = input("what was the string? ").strip().lower()
            if guess == answer.lower():
                #if guess and answer are the same, increase score by 1 and add a letter
                score += 1
                print(f"\ncorrect!\nscore: {score}")
                time.sleep(1)
                print("\033c")
            else:
                #if they are not the same, quit
                print(f"\nincorrect. The string was {answer}")
                print(f"score: {score}")
                time.sleep(1)
                break
            
        #save score
        check_highscore(score,"memory",highscores)

        while True:
            #ask user if they want to play again
            replay = input("\nwould you like to play again?\ntype 'y' to play again\ntype 'n' to quit\nyour answer here: ").strip().lower()
            if replay == "y":
                break
            elif replay == "n":
                playing = False
                break
            else:
                #exception handling
                print("\ninvalid input")
#this will be deleted when everything is finished
memory()