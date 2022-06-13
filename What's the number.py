import random, os
from time import sleep


_wins = 0
_losses = 0
#How many tries you can do, if 0 means it's game over
tries = None

#Generate a random number.
_randomNumber = None

#Set difficulty
_difficulty = None

#Clear terminal.
def cls():
    os.system("cls")

    
#Generate a random number.(FUNCTION)
#def randomNum():
#    return random.randint(1,10)
    

def setSettings(randomNum, diff, triesLeft):
    global _randomNumber
    global tries
    global _difficulty
    _randomNumber = randomNum
    _difficulty = diff
    tries = triesLeft


def loadGame():
    cls()
    print("Loading...")
    sleep(3)
    cls()
    guess()

    
def valError():
    cls()
    print("Please, Input number only.")
    sleep(1)
    cls()

def difficulty():
    cls()
    
    print("===============================")
    print("        0 - Easy")
    print("        1 - Medium")
    print("        2 - Hard")
    print("===============================")

    try:
        _getInput = int(input("Pick difficulty: "))

        if _getInput == 0:
            setSettings(random.randint(1,10), "1-10", 5)
            loadGame()
            
        elif _getInput == 1:
            setSettings(random.randint(1,50), "1-50", 3)
            loadGame()
            
        elif _getInput == 2:
            setSettings(random.randint(1,100), "1-100", 2)
            loadGame()
            
        else:
            cls()
            print("ERROR: The number you picked doesn't exist. Please pick again between 0, 1, and 2.")
            sleep(1.5)
            cls()
            difficulty()
            
    except (ValueError, TypeError):
        valError()
    
#In-game
def guess():
    global tries
    global _wins
    global _losses
    cls()
    while tries != 0:
        try:
            print(f"Tries left: {tries}")
            
            _getInput = int(input(f"What's the number?({_difficulty}): "))

            if _getInput > _randomNumber:
                cls()
                print("The number you input is a bit larger.")
                tries = tries - 1
                sleep(1)
                guess()
            elif _getInput < _randomNumber:
                cls()
                print("The number you input is a bit smaller.")
                tries = tries - 1
                sleep(1)
                guess()
            elif _getInput == _randomNumber:
                cls()
                print("YOU GUESSES IT RIGHT! YOU WIN!!!")
                _wins = _wins + 1
                sleep(2)
                cls()
                tries = 0
                print("Going back to menu...")
                sleep(1.5)
                restart()
                
        except (ValueError,TypeError):
            valError()
    cls()
    print("GAME OVER!")
    _losses = _losses + 1
    sleep(2)
    cls()
    print("Going back to menu...")
    sleep(1.5)
    restart()

#New Game
def restart():
    cls()
    print("===============================")
    print(f"  Wins: {_wins}")
    print(f"  Losses: {_losses}")
    print("===============================")
    print("===============================")
    print("        0 - New Guess")
    print("        1 - Exit ( WARNING: All your records will be lost.)")
    print("===============================")

    try:
        _choose = int(input("Pick: "))
        if _choose == 0:
            cls()
            sleep(1)
            difficulty()
        elif _choose == 1:
            cls()
            print("Exiting program...")
            sleep(1.5)
            cls()
            exit()
        else:
            cls()
            print("ERROR: The number you picked doesn't exist. Please pick again between 0 and 1.")
            sleep(1.5)
            cls()
            restart()
    except (ValueError, TypeError):
        valError()




#Starts the program.
restart()






