from time import sleep
from random import *



def generate_sequence(difficulty=str):
    random_list = []
    for i in range(difficulty):
        random_list.append(randint(1, 30))
    random_list.sort()
    return random_list


print(generate_sequence())