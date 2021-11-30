from GuessGame import *
from MemoryGame import *
from Score import add_score
from Utils import *




def welcome(name):
    hello = ("\nHello %s and welcome to the World of Games (WoG)\n" 
             "Here you can find many cool games to play.\n" % name)
    return hello

def load_game():

    choose = 0
    difficult_number = 0

    menu = ("Please choose a game to play:\n"
                "\t1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                "\t2.Guess Game - guess a number and see if you chose like the computer\n"
                "\t3.Currency Roulette - try and guess the value of a random amount of USD in ILS\n")

    difficult_number_string = "Please choose game difficulty from 1 to 5:\n"
    range_number_message3 = "You must use number between 1-3\n"
    range_number_message5 = "You must use number between 1-5\n"

    while choose == 0:
        print(menu)
        choose = input()
        if choose.isalpha():
            print(range_number_message3)
            choose = 0
        elif choose.isnumeric():
            choose = int(choose)
            if 1 > choose or choose > 3:
                print(range_number_message3)
                choose = 0
            else:
                while difficult_number == 0:
                    print(difficult_number_string)
                    difficult_number = input()
                    if difficult_number.isalpha():
                        print(range_number_message5)
                        difficult_number = 0
                    elif difficult_number.isnumeric():
                        difficult_number = int(difficult_number)
                        if 1 > difficult_number or difficult_number > 5:
                            print(range_number_message5)
                            difficult_number = 0
                        elif choose == 2:
                            result = play(difficult_number)
                            print(result)
                            if result == True :
                                add_score(difficulty=difficult_number)
                        elif choose == 1:
                            result = play2(difficult_number)
                            print(result)
                            if result == True :
                                add_score(difficulty=difficult_number)
                    else:
                        print(difficult_number_string)




