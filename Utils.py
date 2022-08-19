import math
import random


#function to get the position of the coordinates in the single array
#3,4 when each player has 5 choices means 17
def getAbosolutePosition(arrayOfChoices, choicesPerPlayer):
    i = 0
    sum = 0
    combinedChoices = 1
    for x in arrayOfChoices:
        sum += combinedChoices * (x-1)
        combinedChoices *= choicesPerPlayer[i]
        i+=1
    return sum



def randomChoice(playerChoices):
    choice = []
    for x in playerChoices:
        choice.append(random.randint(1,x))
    return choice

#transforms the values in the tables to be the same proportion as the current selection
#if we get a distribution of 3 for one player and 6 for the other we will divide everything so player 2 recieves twice as much as player 1 in all cases
def normalize(Values, playersum, currentChoice, playerChoices, players):
    baseline = Values[getAbosolutePosition(currentChoice, playerChoices)]

    temp = []
    for x in baseline:
        temp.append(int(x) / playersum)

    baseline = temp

    newValues = []
    for x in Values:
        linesum = 0
        for i in x:
            linesum += int(i)
        temp = []
        for y, z in enumerate(x):
            temp.append(linesum * baseline[y])

        newValues.append(temp)

    Values = newValues
    for player in players:
        player.updateValues(Values)
    return Values