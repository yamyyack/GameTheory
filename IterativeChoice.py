from Utils import *

def IBR(arrayCurrentChoice, infoDict):
    playerNumber = infoDict["player number"] - 1
    numberOfChoices = infoDict["number of choices"]
    # sets the current temp to be equal to the original choice
    # so unless theres something larger it will choose the same one
    tempCurrent = float(infoDict["tableValue"][getAbosolutePosition(arrayCurrentChoice, numberOfChoices)][playerNumber])
    tempPosition = arrayCurrentChoice[playerNumber]

    # loops through every choice this player can make
    for x in range(1, numberOfChoices[playerNumber] + 1):
        arrayCurrentChoice[playerNumber] = x

        # if the choice is larger than the current choice change
        if (float(infoDict["tableValue"][getAbosolutePosition(arrayCurrentChoice, numberOfChoices)][
                      playerNumber]) > tempCurrent):
            tempCurrent = float(
                infoDict["tableValue"][getAbosolutePosition(arrayCurrentChoice, numberOfChoices)][playerNumber])
            tempPosition = x

    return tempPosition