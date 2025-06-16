import random

def main():
    print("THIS A NUMBER GUESSING GAME. YOU HAVE TO GUESS THE RANDOM NUMBER SELECTED BETWEEN 0 TO 100.")
    rand_num = get_rand()
    count = 1
    while True:
        num = get_num()
        if num < 0 or num > 100:
            print("Number out of range!!")
            print("try again")
        elif num == rand_num:
            print(f"CONGRATS!! You have guessed the number in {count} attempts. ")
            break
        elif num < rand_num:
            print("Too low")
            print("TRY AGAIN")
        else:
            print("Too high")
            print("TRY AGAIN")
        
        count += 1


def get_rand():
    return random.randint(0,100)

def get_num():
    while True:
        try:
            return int(input("Guess the number here: "))   
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER.")

main()