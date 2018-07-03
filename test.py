import time
import sys
import random

print('Welcome to the game!')
print('This is rock paper scissors lizard spock.')

while True:
    print("Choose your weapon:")
    weapon = input("")
    valid = ["scissors", "rock", "paper", "spock", "lizard"]
    randomnum = random.randint(0,4)
    computer = valid[randomnum]

    if weapon.lower() in valid:
        print("You chose:")
        for char in weapon:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print("!")
        time.sleep(0.5)    
        print("computer picked " + computer + ".")
        
    if weapon.lower() == "scissors":
        if computer == "scissors":
            time.sleep(0.2)
            print("tied!")

        elif computer == "paper":
            time.sleep(0.2)
            print("YEET you win!")

        elif computer == "rock":
            time.sleep(0.2)
            print("boohoo, you lose.")

        elif computer == "lizard":
            time.sleep(0.2)
            print("YEET you win!.")

        elif computer == "spock":
            time.sleep(0.2)
            print("boohoo, you lose.")

    elif weapon.lower() == "paper":
        if computer == "scissors":
            time.sleep(0.2)
            print("boohoo, you lose.")

        elif computer == "paper":
            time.sleep(0.2)
            print("tied!")

        elif computer == "rock":
            time.sleep(0.2)
            print("YEET you win!")

        elif computer == "lizard":
            time.sleep(0.2)
            print("boohoo, you lose.")

        elif computer == "spock":
            time.sleep(0.2)
            print("YEET you win!")

    elif weapon.lower() == "rock":
        if computer == "scissors":
            time.sleep(0.2)
            print("YEET you win!")

        elif computer == "paper":
            time.sleep(0.2)
            print("boohoo, you lose.")

        elif computer == "rock":
            time.sleep(0.2)
            print("tied!")

        elif computer == "lizard":
            time.sleep(0.2)
            print("YEET you win!")

        elif computer == "spock":
            time.sleep(0.2)
            print("boohoo, you lose.")

    elif weapon.lower() == "lizard":
        if computer == "scissors":
            time.sleep(0.2)
            print("boohoo, you lose.")

        elif computer == "paper":
            time.sleep(0.2)
            print("YEET you win!")

        elif computer == "rock":
            time.sleep(0.2)
            print("boohoo, you lose.")

        elif computer == "lizard":
            time.sleep(0.2)
            print("tied!")

        elif computer == "spock":
            time.sleep(0.2)
            print("YEET you win!")

    elif weapon.lower() == "spock":
        if computer == "scissors":
            time.sleep(0.2)
            print("YEET you win!")

        elif computer == "paper":
            time.sleep(0.2)
            print("boohoo, you lose!")

        elif computer == "rock":
            time.sleep(0.2)
            print("YEET you win!")

        elif computer == "lizard":
            time.sleep(0.2)
            print("boohoo, you lose.")

        elif computer == "spock":
            time.sleep(0.2)
            print("tied!")
        

            
    else:
        time.sleep(0.2)
        for char in "Come on, is that all you got?":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.00001)
        time.sleep(0.2)
        for char in " Let's try that again....":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.00001)
        time.sleep(1)
        print("Pick from rock, paper, scissors, lizard, or spock.")
        time.sleep(1)

    
