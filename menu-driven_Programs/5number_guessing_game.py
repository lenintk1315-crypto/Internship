import random

def game_begin():
    num = random.randint(1, 10)
    count = 0
    print( f"Number :{num}")  
    while True:
        user_guess = int(input(f"its Your Turn to Guess Broh..!: "))
        count += 1
        if user_guess > num:
            print("Your guess is larger bro... Try again!")
        elif user_guess == num:
            print("Your guess is perfect... You won!")
            print(f"You took {count} attempts.")
            return count
        else:
            print("Your guess is small bro... Try again!")


def game_high_score(high_score):
    attempts = game_begin()
    if high_score is None or attempts < high_score:
        high_score = attempts
        print(f"New high score: {high_score}")
    else:
        print(f"Your attempts: {attempts}")
        print(f"Current high score: {high_score}")
    return high_score, attempts



def game_main():
    high_score=None
    attempts=None
    while True:
        choice=int(input("\n 1.Start The game : \n 2.View The high score \n 3.Exit...\n select your option : "))
        match choice:
            case 1:
                high_score, attempts = game_high_score(high_score)
            case 2:
                if high_score is None:
                    print("Begin the first game")
                else:
                    print(f"Your high score is {high_score}")
            case 3:
                print("exiting....")
                break
game_main()


