import math
import random



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


