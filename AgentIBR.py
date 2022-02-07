from Utils import *

class AgentIBR():

    def __init__(self, playerNumber, numberOfChoices, values):
        self.playerNumber = playerNumber
        self.numberOfChoices = numberOfChoices
        self.Values = values
        self.currentOutcome = 0

    def getNextChoice(self, arrayCurrentChoice):
        tempCurrent = 0
        tempPosition = None
        for x in range(1, self.numberOfChoices[self.playerNumber]+1):
            arrayCurrentChoice[self.playerNumber] = x



            if (float(self.Values[getAbosolutePosition(arrayCurrentChoice, self.numberOfChoices)][self.playerNumber]) > tempCurrent):
                tempCurrent = float(self.Values[getAbosolutePosition(arrayCurrentChoice, self.numberOfChoices)][self.playerNumber])
                tempPosition = x

        return tempPosition

    def setCurrentOutcome(self, outcome):
        self.currentOutcome = outcome