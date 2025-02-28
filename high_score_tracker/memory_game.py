#Alec George Memory Game

#will create a random string of letters and numbers and let the user rewrite it when they no longer see it. If they get it correct, it gets longer


import random
import time

#import functions and variables to check highscore
from file_functions import *


#function for normal mode, capitalization doesn't matter and it just adds a letter to the end
def normal(string):
    #variable for all possible characters to add
    possible_figures = "1234567890qwertyuiopasdfghjklzxcvbnm"
    #add a random letter
    string += possible_figures [random.randint(0,len(possible_figures)-1)]
    return string


#function for hard mode, capitalization matters, more characters, and randomizes the string
def hard(string, length):
    possible_figures = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+-=~`[];:',<.>/?"
    for i in range(length):
        string += possible_figures[random.randint(0,len(possible_figures)-1)]

    return string

    

#main function
def memory():
    #introduction to the game
    print("\nWelcome to the memory game!\nA string of letters/numbers will appear for about 3 seconds.\nYour goal is to type the string of letters again after it disappears.\nAs you get more and more correct, the string will get longer and longer.")
    playing = True
    #allow the user to play again using a while loop
    while playing:
        mode = input("type 1 for normal mode\ntype 2 for hard mode\nyour answer here: ")
        #make variables for score and the string to guess
        score = 0
        answer = ""
        playing = True
        #while loop to run until the user fails
        while playing:
            if mode == "1":
                #add one character to answer if answer is 1 (normal mode)
                answer = normal(answer)

            elif mode == "2":
                #randomize the string and add characters if answer is 2 (hard mode)
                answer = hard(answer, score+1)

            else: #exception handling
                print("\ninvalid input")
                continue

            #show the answer for 5 seconds
            print(f"\nstring:\n{answer}")
            time.sleep(3)
            print("\033c")

            #variable for the user's guess to what the string is
            guess = input("what was the string? ").strip()
            if guess == answer:
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
        check_highscore(score,"memory",highscores,data)

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

memory()