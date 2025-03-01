# Jacksons Code (File Functions)

import csv

highscores = {}
def start_highscores(highscores):
    with open('high_score_tracker/highscores.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            game = row[0]
            scores = list(map(int, row[1:]))  
            highscores[game] = scores

def check_highscore(score, game, highscores):
    highscores[game].append(score)
    highscores["reaction"].sort()
    highscores["memory"].sort()
    highscores["math"].sort()
    highscores["math"].reverse()
    highscores["memory"].reverse()
    if game == "reaction":
        if score < highscores["reaction"][0]:
            writeback()
            return True
        else:
            writeback()
            return False
    else:
        if score > highscores[game][0]:
            writeback()
            return True
        else:
            writeback()
            return False
        
def writeback():
    with open('high_score_tracker/highscores.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['game', 'scores'])  # Writing header
        for game, scores in highscores.items():
            writer.writerow([game] + scores)

