import os

def get_score():
    with open(r"./Scores.txt" , "r") as score_file:
        score_result = score_file.readlines()
        return score_result[0]

SCORES_FILE_NAME = get_score()

def screen_cleaner():
    os.system('cls')

