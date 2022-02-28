from Utils import *

def IBR(playerNumber, numberOfChoices, arrayCurrentChoice, Values):
    playerNumber -= 1
    # sets the current temp to be equal to the original choice
    # so unless theres something larger it will choose the same one
    tempCurrent = float(Values[getAbosolutePosition(arrayCurrentChoice, numberOfChoices)][playerNumber])
    tempPosition = arrayCurrentChoice[playerNumber]

    # loops through every choice this player can make
    for x in range(1, numberOfChoices[playerNumber] + 1):
        arrayCurrentChoice[playerNumber] = x

        # if the choice is larger than the current choice change
        if (float(Values[getAbosolutePosition(arrayCurrentChoice, numberOfChoices)][
                      playerNumber]) > tempCurrent):
            tempCurrent = float(
                Values[getAbosolutePosition(arrayCurrentChoice, numberOfChoices)][playerNumber])
            tempPosition = x

    return tempPosition