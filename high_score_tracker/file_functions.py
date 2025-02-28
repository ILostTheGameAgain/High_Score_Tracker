# Jacksons Code (File Functions)

import csv

highscores = {}
data = {}

# This checks then overwrites if you got the highscore, returns TRUE if highscore was passed, returns FALSE if you didn't beat the highscore

def start_highscores(highscores, data):
    try:
        with open("high_score_tracker/highscores.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                if len(row) == 2: 
                    name, score = row[0], row[1]
                    highscores[name] = int(score) 
    except FileNotFoundError:
        print("High scores file not found. Starting fresh.")
    try:
        with open("high_score_tracker/tophighscores.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                if len(row) == 2: 
                    data_name = row[0].strip()
                    if data_name not in data:
                        data[data_name] = [] 
    except FileNotFoundError:
        print("Top high scores file not found. Starting fresh.")

import csv

def check_highscore(score, game, highscores, data):
    score = int(score)
    if game not in data:
        data[game] = []  
    data[game].append(score)
    data[game].sort(reverse=True)
    data[game] = data[game][:10]  
    with open("your_file.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Score"])  # Write header
        for key, value in data.items():
            writer.writerow([key] + value)  
    if game not in highscores:
        highscores[game] = score  
    if game == "reaction":
        if score < highscores[game]: 
            highscores[game] = score 
            with open("high_score_tracker/highscores.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Score"])
                writer.writerows(highscores.items()) 
            with open("high_score_tracker/top10highscores.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Name", "Score"])
                for key, value in data.items():
                    writer.writerow([key] + value) 
            return True 
        else:
            return False  # No new high score for "reaction"
    else:
        if score > highscores[game]:
            highscores[game] = score 
   
            with open("high_score_tracker/highscores.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Score"])
                writer.writerows(highscores.items())
            with open("high_score_tracker/top10highscores.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Name", "Score"])
                for key, value in data.items():
                    writer.writerow([key] + value)  

            return True  # New high score for other games
        else:
            return False  