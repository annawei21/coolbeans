import random
import time
import sys

empty = " "
x = "x"
o = "o"
print("welcome to tic tac toe!")

time.sleep(0.6)
for char in ("this will be the game board you can play on:"):
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.00000025)

def movegrid(board):
    board = board[:]

time.sleep(0.000002)
movegrid = """\n-----------
   |   |   
-----------
   |   |    
-----------
   |   |  
-----------"""


gridinfo = """\n-----------
 1 | 2 | 3 
-----------
 4 | 5 | 6  
-----------
 7 | 8 | 9
-----------"""

print(gridinfo)
for char in ("you may make your moves by entering the number which corresponds in the box you would like to take."):
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.0000003)

time.sleep(0.3)
answer = input("\nbut first, let's decide who can go first. we'll do this by a skill-testing question. \nwhat is 1+1? ")

correct = ["2", "two"]

if answer.lower() in correct:
    for char in ("you're a smart one. you won't be needing the first turn!"):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0000003)
    computer = "x"
    human = "o"

    new = list(movegrid)
    new[42] = computer
    time.sleep(0.3)
    print("".join(new))
    movegrid = "".join(new)
    
    for char in ("computer has made its turn."):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0000003)
    
else:
    for char in ("wow, not an intellect, i see. i guess you can go first. you'll be needing it :^)"):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0000003)
    human = "x"
    computer = "o"

while True:
    humanmove = input("\npick a square to conquer! ")

        
    #legal moves
    legal = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
  

    if humanmove in legal and humanmove in ("1", "2", "3"):
        time.sleep(0.3)
        print("nice move.")
        position = int(humanmove)*4+10
        new = list(movegrid)
        new[position] = human
        time.sleep(0.3)
        print("".join(new))
        movegrid = "".join(new)
        

    elif humanmove in legal and humanmove in ("4", "5", "6"):
        time.sleep(0.3)
        print("nice move.")
        position = int(humanmove)*4+22
        new = list(movegrid)
        new[position] = human
        time.sleep(0.3)
        print("".join(new))
        movegrid = "".join(new)
        
    elif humanmove in legal and humanmove in ("7", "8", "9"):
        time.sleep(0.3)
        print("nice move.")
        position = int(humanmove)*4+35
        new = list(movegrid)
        new[position] = human
        time.sleep(0.3)
        print("".join(new))
        movegrid = "".join(new)

    else:
        for char in ("yikes, you really aren't a bright one, huh?"):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.0000003)
        time.sleep(0.4)
        for char in ("\nmake sure you pick the number of a square that isnt already taken."):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.0000003)
            
    victory = ((0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6))
