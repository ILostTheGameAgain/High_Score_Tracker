# Jacksons Code (File Functions)

import csv

# This checks then overwrites if you got the highscore, returns TRUE if highscore was passed, returns FALSE if you didn't beat the highscore
def check_highscore():
    with open("High_Score_Tracker/high_score_tracker/highscores.csv","w+"):
        reader = csv.reader()
        next(reader)
