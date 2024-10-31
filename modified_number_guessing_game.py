import random
winning_number = random.randint(1,100)
attempts = 0
while True:
    guess_number = int(input("enter a number between 1 and 100 :"))
    attempts += 1
    if guess_number < winning_number:
        print("too low !! guess again : ")
         
    elif guess_number > winning_number:
        print("too high !! guess again : ")

    else:
        print(f"congrats you have won the game in {attempts}  attempts")
        break

