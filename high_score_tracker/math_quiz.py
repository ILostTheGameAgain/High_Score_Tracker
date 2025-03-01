import random
from file_functions import *

operators = ["+", "-", "*", "/"]
#This function solves the equation to get an answer
def answer(equation):
    if equation[1] == "+":
        solution = int(equation[0]) + int(equation[2])
        return solution
    if equation[1] == "-":
        solution = int(equation[0]) - int(equation[2])
        return solution
    if equation[1] == "*":
        solution = int(equation[0]) * int(equation[2])
        return solution
    if equation[1] == "/":
        solution = int(equation[0]) / int(equation[2])
        return solution
        
def cs():
    print("\033c")
def math_quiz():
    while True:
        math_score = 0
        top = 1
        cs()
        print("Top 10 Scores:")
        if len(highscores["math"]) >= 10:
            reactionscores = 10
        else:
            reactionscores = len(highscores["math"])
        for x in range(reactionscores):
            print(f"{top}: {highscores["math"][x]}")
            top += 1
        quiz = input("Welcome to the math game press 1 to start and 2 to return to the main menu: ")
        if quiz == "1":
            while True:
                #This gets the equation and runs the answer function
                equation = random.randint(1,10), operators[random.randint(0,3)], random.randint(1,10)
                print(f"{equation[0]}{equation[1]}{equation[2]}")
                solution = answer(equation)
                while True:
                    try:
                        #This gets user imput
                        user_input = float(input("What is the answer: "))
                        break
                    except ValueError:
                        print("Invalid input please try again")
                        #This checks if its correct
                if user_input == solution:
                    print("Correct")
                    math_score += 1
                elif user_input != solution:
                    print("Im sorry that is incorrect your final score was", math_score)
                    check_highscore(math_score,"math",highscores)
                    break
        if quiz == "2":
            break
