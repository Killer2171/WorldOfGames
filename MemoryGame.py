from time import *
from random import *
from Utils import screen_cleaner




def generate_sequence(difficulty=str):
    random_list = []
    for i in range(difficulty):
        random_list.append(randint(1, 100))
    random_list.sort()
    print(random_list)
    sleep(0.7)
    screen_cleaner()
    return random_list


def get_list_from_user():
    print("Please type the numbers with comma between them for example 10,15,35: ")
    user_input = input()
    user_input_list = user_input.split(",")
    user_input_list.sort()
    return list(map(int, user_input_list))

def is_list_equal(sys_list, user_list ):
    compare = sys_list == user_list
    return compare

def play2(difficulty):
    sys_list = generate_sequence(difficulty)
    user_list = get_list_from_user()
    return is_list_equal(sys_list, user_list)