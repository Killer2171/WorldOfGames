
def add_score(difficulty=3):
        with open("./Scores.txt" , "r") as score_file:
            score_file_read = score_file.readlines()
            score_result = int(score_file_read[0])
        total_score = (difficulty * 3) + 5 + score_result
        with open("./Scores.txt" , "w") as score_file:
             score_file.write(str(total_score))
        return total_score
print(add_score())


