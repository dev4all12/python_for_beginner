# higher lower game
import random
import ascii_art
import high_lower_db
import os


print(ascii_art.higher_lower_logo)

score = 0


def display_db_info(account):
    name = account['name']
    return f" {name}"


def is_correct(guess, follower_count1, follower_count2):
    if follower_count1 < follower_count2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False


account_2 = random.choice(high_lower_db.db)

continue_flag = True
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(high_lower_db.db)
    while account_1 == account_2:
        account_2 = random.choice(high_lower_db.db)

    print(f"Compare1: {display_db_info(account_1)}")
    print(ascii_art.vs)
    print(f"Compare2: {display_db_info(account_2)}")

    guess = int(input('Who has more follower 1 or 2: '))
    follower_count1 = account_1['value']
    follower_count2 = account_2['value']
    print(follower_count1)
    print(follower_count2)
    check_ans = is_correct(guess, follower_count1, follower_count2)
    os.system('cls')
    print(ascii_art.higher_lower_logo)
    if check_ans:
        score += 1
        print(f"You are right. Your Score is: {score}")
    else:
        print(f"You are wrong. Your Score is: {score}")
        continue_flag = False