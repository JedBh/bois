# . Create a Lotto game:
#  Puts in a list of 6 numbers, between 1-37, as in a real lottery. V
#  The numbers must not be repeated. V
#  Each game (row) in Lotto costs 3 ILS, Insert how much money do you have? V
#  Random 6 numbers – the winner's number. V
#  Then play few rounds (rows) as your budget can handle.
#  On each round, random 6 numbers , between 1-37, and check if you won.
#  In the end sum the entire prize from all rounds.

# If you guess:
# 6 numbers = won 1M ILS
# 5 numbers = won 5000 ILS
# 4 numbers = won 100 ILS
# 3 numbers = won 10 ILS

import random

def genRanNum():
    ranList = []
    while(len(ranList) < 6):
        ranNum = random.randint(1,37)
        if ranNum not in ranList:
            ranList.append(ranNum)
    return ranList

def calcPrize(count):
    if (count < 3):
        return "0 ILS"
    if (count < 4):
        return "10 ILS"
    if (count < 5):
        return "100 ILS"
    if (count < 6):
        return "5000 ILS"
    else:
        return "1M ILS"

def game():
    budget = input("How much money do you have: ")
    budget = float(budget)

    count = 0
    while (budget >= 3):
        winningList = genRanNum()
        print("This game costs 3 ILS")
        answer = input("\nDo you wish to play a round? y/n ")
        if (answer == "y" or answer == "Y" or answer == "Yes" or answer == "yes"):
            budget -= 3
            userList = genRanNum()
            print("\n" + "Your numbers:    " + str(userList))
            print("Winning Numbers: " + str(winningList))

            for number in userList:
                if (number in winningList):
                    wIndex = winningList.index(number)
                    uIndex = userList.index(number)
                    if (wIndex == uIndex):
                        count += 1

            print("\nYou have matched " + str(count) + " numbers.")
        else:
            print("\nYou have matched " + str(count) + " numbers.")
            break
        
        
        print("\nremaining budget " + str(budget))

    if (budget < 3):
        print("You go away with a cash prize of " + str(calcPrize(count)) + "!")
        print("Insufficient Funds.")
    else:
        print("You go away with a cash prize of " + str(calcPrize(count)) + "!")
        print("We hope to see you soon!")
        print("remaining budget " + str(budget))

game()