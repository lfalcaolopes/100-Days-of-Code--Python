import random
import gamedata
import os


def clear():
    os.system('cls')


def random_account():
    return random.choice(gamedata.data)


def account():
    person = random_account()

    followers = person['follower_count']

    text = f"{person['name']}, a {person['description']}, from {person['country']}.\n"

    data = {'text': text, 'followers': followers}

    return data


def checking_answer(a_followers, b_followers, guess, score):
    clear()

    if a_followers > b_followers and guess == 'a':
        score += 1
        print(f"  You are Right! Your score is {score}\n")
        is_right = True
    elif a_followers < b_followers and guess == 'b':
        score += 1
        print(f"  You are Right! Your score is {score}\n")
        is_right = True
    elif a_followers == b_followers:
        is_right = True
    else:
        print(f"    You Lost... Your score was {score}\n")
        is_right = False

    data = {'isRight': is_right, 'score': score}

    return data


def higher_lower():
    is_right = True
    score = 0

    first_account = account()

    while is_right:
        second_account = account()

        print(f"Compare A: {first_account['text']}")
        print(f"Against B: {second_account['text']}")

        a_followers = first_account['followers']
        b_followers = second_account['followers']

        guess = input("Which one has more followers? Type 'a' or 'b': ")

        result = checking_answer(a_followers, b_followers, guess, score)

        is_right = result['isRight']
        score = result['score']
        first_account = second_account


clear()
higher_lower()
