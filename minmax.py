from Utils import getAbosolutePosition


def minmax(playerChoices, Values, currentPlayer):
    currentChoice = playerChoices.copy()
    for x in currentChoice:
        x = 1




#this will loop through for all the values if a specific player makes a choice
def getAllPayoffForPlay(Values, CurrentPlayer, PlayerChoices, playerChoice):
    payoff = []

    currentChoice = [1] * len(PlayerChoices)
    currentChoice[CurrentPlayer] = playerChoice

    getArrayForChoice(currentChoice,0,PlayerChoices, CurrentPlayer)

    for x in array:
        payoff.append(Values[getAbosolutePosition(x)])
    print(array)




array = []


def getArrayForChoice(currentChoice, depth, PlayerChoices, playerChoiceSet):
    if(depth >= len(PlayerChoices)):
        return True
    if(depth == playerChoiceSet and playerChoiceSet != 0):
        return getArrayForChoice(currentChoice, depth + 1, PlayerChoices, playerChoiceSet)
    if(depth >0):
        currentChoice[depth]+=1
        if (currentChoice[depth] > PlayerChoices[depth]):
            currentChoice[depth] = 1
            return getArrayForChoice(currentChoice, depth + 1, PlayerChoices, playerChoiceSet)
        else:
            return False
    while(True):
        array.append(currentChoice.copy())
        print("pain")
        if(playerChoiceSet == 0):

            if (getArrayForChoice(currentChoice, depth + 1, PlayerChoices, playerChoiceSet)):
                print("pain")
                return
        #print(array)
        else:
            currentChoice[depth] +=1
            if(currentChoice[depth] > PlayerChoices[depth]):
                currentChoice[depth] = 1
                if(getArrayForChoice(currentChoice, depth+1, PlayerChoices, playerChoiceSet)):
                    print("pain")
                    return
