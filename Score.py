from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    try:
        with open(SCORES_FILE_NAME, "r") as score_file:
            score_file_read = score_file.readlines()
            score_result = int(score_file_read[0])
            total_score = (difficulty * 3) + 5 + score_result
            with open(SCORES_FILE_NAME, "w") as score_file:
                score_file.write(str(total_score))
            return total_score
    except :
        with open(SCORES_FILE_NAME, "w") as score_file:
            total_score = (difficulty * 3) + 5
            score_file.write(str(total_score))
            return "No Score file exist , Scores.txt created "

