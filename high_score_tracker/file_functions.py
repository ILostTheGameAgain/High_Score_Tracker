# Jacksons Code (File Functions)

import csv

highscores = {}
data = {}

# This checks then overwrites if you got the highscore, returns TRUE if highscore was passed, returns FALSE if you didn't beat the highscore

def start_highscores(highscores):
    with open("high_score_tracker/highscores.csv","r") as file:
        reader = csv.reader(file)
        next(reader,None)
        for row in reader:
            highscores.update({row[0]:row[1]})
    with open("high_score_tracker/top10highscores.csv", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header row
        data = {row[0]: eval(row[1]) if row[1] else [] for row in reader}

def check_highscore(score,game,highscores): # Games are reaction, math, memory as a string
    if game == "reaction":
        if int(score) < int(highscores[str(game)]):
            highscores[str(game)] = score
            data[game].append(score).sort(reverse=True)
            with open("high_score_tracker/highscores.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Score"])
                writer.writerows(highscores.items()) 
            with open("high_score_tracker/top10highscores.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Name", "score"])
                for key, value in data.items():
                    writer.writerow([key, str(value)])  # Convert list to string format

            return True
        else:
            return False
    else:
        if int(score) > int(highscores[str(game)]):
            highscores[str(game)] = score
            data[game].append(score).sort()
            with open("high_score_tracker/highscores.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Score"])
                writer.writerows(highscores.items()) 
            with open("high_score_tracker/top10highscores.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Name", "score"])
                for key, value in data.items():
                    writer.writerow([key, str(value)])  # Convert list to string format
            return True
        else:
            return False
    

