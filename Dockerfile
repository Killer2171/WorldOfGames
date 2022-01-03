FROM python:3
ADD . /
RUN pip install flask
CMD ["python", "MainScores.py"]