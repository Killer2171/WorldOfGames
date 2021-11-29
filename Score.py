

def add_score(difficulty=2):
    try:
        with open("Scores.txt", "r") as score_file:
            score_file_read = score_file.readlines()
            score_result = int(score_file_read[0])
            total_score = (difficulty * 3) + 5 + score_result
            with open("Scores.txt", "w") as score_file:
                score_file.write(str(total_score))
            return total_score
    except :
        with open("Scores.txt", "w") as score_file:
            total_score = (difficulty * 3) + 5
            score_file.write(str(total_score))
            return "No Score file exist , Scores.txt created "

print(add_score())