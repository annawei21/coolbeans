import time
import sys
import random

print('Welcome to the game!')
for char in ('This is rock paper scissors lizard spock.'):
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.0005)
    
yourscore = 0
compscore = 0

while True:
    time.sleep(0.6)
    print("""
you v.s. cpu: the current score is: """)

    for char in (str(yourscore) + "-" + str(compscore)):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)

    time.sleep(1)    
    print("""

Choose your weapon:""")
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
            yourscore += 1

        elif computer == "lizard":
            time.sleep(0.2)
            print("YEET you win!.")
            yourscore += 1
        else:
            time.sleep(0.2)
            print("boohoo, you lose.")
            compscore += 1
    elif weapon.lower() == "paper":

        if computer == "paper":
            time.sleep(0.2)
            print("tied!")

        elif computer == "rock":
            time.sleep(0.2)
            print("YEET you win!")
            yourscore += 1

        elif computer == "spock":
            time.sleep(0.2)
            print("YEET you win!")
            yourscore += 1

        else:
            time.sleep(0.2)
            print("boohoo, you lose.")
            compscore += 1

    elif weapon.lower() == "rock":
        if computer == "scissors":
            time.sleep(0.2)
            print("YEET you win!")
            yourscore += 1

        elif computer == "rock":
            time.sleep(0.2)
            print("tied!")

        elif computer == "lizard":
            time.sleep(0.2)
            print("YEET you win!")
            yourscore += 1
            
        else:
            time.sleep(0.2)
            print("boohoo, you lose.")
            compscore += 1

    elif weapon.lower() == "lizard":
        if computer == "paper":
            time.sleep(0.2)
            print("YEET you win!")
            yourscore += 1

        elif computer == "lizard":
            time.sleep(0.2)
            print("tied!")

        elif computer == "spock":
            time.sleep(0.2)
            print("YEET you win!")
            yourscore += 1

        else:
            time.sleep(0.2)
            print("boohoo, you lose.")
            compscore += 1

    elif weapon.lower() == "spock":
        if computer == "scissors":
            time.sleep(0.2)
            print("YEET you win!")
            yourscore += 1

        elif computer == "rock":
            time.sleep(0.2)
            print("YEET you win!")
            yourscore += 1

        elif computer == "spock":
            time.sleep(0.2)
            print("tied!")

        else:
            time.sleep(0.2)
            print("boohoo, you lose.")
            compscore += 1
            
                           
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

    
