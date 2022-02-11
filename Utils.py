import math
import random

def ConvertFileToArray(file):
    Values = []
    Positions = []

    for line in file:
        if line[0] != "#":
            array = line.split(":")
            position = array[0][1:-2]
            value = array[1][3:-3]
            positionToArray = position.split("  ")
            valueToArray = value.split(" ")
            Positions.append(positionToArray)
            Values.append(valueToArray)
    return Values, Positions

def getAbosolutePosition(arrayOfChoices, choicesPerPlayer):
    i = 0
    sum = 0
    combinedChoices = 1
    for x in arrayOfChoices:
        sum += combinedChoices * (x-1)
        combinedChoices *= choicesPerPlayer[i]
        i+=1
    return sum

def createPlayers(classOfPlayer, playerChoices, Values):
    players = []
    for x in range(len(playerChoices)):
        players.append(classOfPlayer(x, playerChoices, Values))
    return players

def randomChoice(playerChoices):
    choice = []
    for x in playerChoices:
        choice.append(random.randint(1,x))
    return choice

def iteration(players, currentChoice, Values, playerChoices, step):
    tempChoice = []
    for player in players:
        tempChoice.append(player.getNextChoice(currentChoice.copy()))
    print("this is the choice after the : {0}".format(step))
    print(tempChoice)
    print("\n")
    i = 0
    for player in players:
        player.setCurrentOutcome(float(Values[getAbosolutePosition(tempChoice, playerChoices)][i]))
        i += 1
    return tempChoice
