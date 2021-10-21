from random import randint


def generate_num(difficulty=int):
    secret_number = randint(1, difficulty)
    return secret_number

def get_guess_from_user():
    user_guess = int(input("Please enter your number: "))
    return user_guess



def compare_results(secret_number, user_guess):
    results = secret_number == user_guess
    return results


def play(number):
    secret_number = generate_num(number)
    user_guess = get_guess_from_user()
    return compare_results(secret_number, user_guess)



