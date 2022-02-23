from Utils import getAbosolutePosition


def minmax(playerChoices, Values, currentPlayer):
    randarray = [9999999999]*(playerChoices[currentPlayer])
    for x in range(playerChoices[currentPlayer]):
        kek = getAllPayoffForPlay(Values, currentPlayer, playerChoices, x+1)
        for y in kek:
            if(int(y[currentPlayer]) < int(randarray[x])):
                randarray[x] = y[currentPlayer]

    max_value = max(randarray)
    return randarray.index(max_value)+1



#this will loop through for all the values if a specific player makes a choice
def getAllPayoffForPlay(Values, CurrentPlayer, PlayerChoices, playerChoice):
    payoff = []

    currentChoice = [1] * len(PlayerChoices)
    currentChoice[CurrentPlayer] = playerChoice

    array = []

    getArrayForChoice(currentChoice,0,PlayerChoices, CurrentPlayer, array)

    for x in array:
        payoff.append(Values[getAbosolutePosition(x, PlayerChoices)])

    array = []

    return payoff







def getArrayForChoice(currentChoice, depth, PlayerChoices, playerChoiceSet, array):
    if(depth >= len(PlayerChoices)):
        return True
    if(depth > 0):
        if(playerChoiceSet == depth):
            return getArrayForChoice(currentChoice, depth + 1, PlayerChoices, playerChoiceSet, array)
        currentChoice[depth] +=1
        if (currentChoice[depth] > PlayerChoices[depth]):
            currentChoice[depth] = 1
            return getArrayForChoice(currentChoice, depth + 1, PlayerChoices, playerChoiceSet, array)
        return False
    while(True):
        array.append(currentChoice.copy())
        if(playerChoiceSet == 0):
            if (getArrayForChoice(currentChoice, depth + 1, PlayerChoices, playerChoiceSet, array)):
                return
        else:
            currentChoice[depth] += 1
            if (currentChoice[depth] > PlayerChoices[depth]):
                currentChoice[depth] = 1
                if (getArrayForChoice(currentChoice, depth + 1, PlayerChoices, playerChoiceSet, array)):
                    return
