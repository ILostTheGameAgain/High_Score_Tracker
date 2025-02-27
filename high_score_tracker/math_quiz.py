import random

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
        

def math_quiz():
    while True:
        math_score = 0
        quiz = input("Welcome to the math game press 1 to start and 2 to return to the main menu: ")
        if quiz == "1":
            while True:
                equation = random.randint(1,10), operators[random.randint(0,3)], random.randint(1,10)
                print(equation)
                solution = answer(equation)
                while True:
                    try:
                        user_input = float(input("What is the answer: "))
                        break
                    except ValueError:
                        print("Invalid input please try again")
                if user_input == solution:
                    print("Correct")
                    math_score += 1
                elif user_input != solution:
                    print("Im sorry that is incorrect your score was", math_score)
                    math_score = 0
        if quiz == "2":
            break

math_quiz()