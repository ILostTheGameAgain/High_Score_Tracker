# Jacksons Code (File Functions)

import csv

highscores = {}

# This checks then overwrites if you got the highscore, returns TRUE if highscore was passed, returns FALSE if you didn't beat the highscore

def start_highscores(highscores):
    with open("high_score_tracker/highscores.csv","r") as file:
        reader = csv.reader(file)
        next(reader,None)
        for row in reader:
            highscores.update({row[0]:row[1]})

def check_highscore(score,game,highscores): # Games are reaction, math, memory as a string
    if game == "reaction":
        if int(score) < int(highscores[str(game)]):
            highscores[str(game)] = score
            with open("high_score_tracker/highscores.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Score"])
                writer.writerows(highscores.items()) 
            return True
        else:
            return False
    else:
        if int(score) > int(highscores[str(game)]):
            highscores[str(game)] = score
            with open("high_score_tracker/highscores.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Score"])
                writer.writerows(highscores.items()) 
            return True
        else:
            return False
    

