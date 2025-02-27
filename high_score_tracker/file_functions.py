# Jacksons Code (File Functions)

import csv

highscores = {}

# This checks then overwrites if you got the highscore, returns TRUE if highscore was passed, returns FALSE if you didn't beat the highscore

def start_highscores():
    with open("High_Score_Tracker/high_score_tracker/highscores.csv","w+"):
        reader = csv.reader()
        next(reader)
        for row in reader:
            highscores.update({row[0]:row[1]})
