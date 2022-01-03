FROM python:3
# ENV FLASK_ENV=development
ADD . /
RUN pip install flask
CMD ["python", "MainScores.py"]