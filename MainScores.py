from flask import Flask, request, render_template
from Utils import SCORES_FILE_NAME
app = Flask("Myserver")


@app.route('/', methods=['GET'])
def render_scores():
    try:
        with open(SCORES_FILE_NAME, "r") as score_file:
            score = score_file.readlines()
            return render_template('SuccessScore.html', SCORE=score[0])
    except Exception as ERROR:
        return render_template('FailScore.html', ERROR=ERROR)




app.run(host="0.0.0.0", port=5001, debug=True)