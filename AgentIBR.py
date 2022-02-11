from Utils import *
from Joueur import Joueur
from abc import ABC

class AgentIBR(Joueur):

    def __init__(self, playerNumber, numberOfChoices, values):
        self.playerNumber = playerNumber
        self.numberOfChoices = numberOfChoices
        self.Values = values
        self.currentOutcome = 0

    def chooseStartingPoint(self):
        return random.randint(1, self.numberOfChoices[self.playerNumber])

    #overriding abstract mrthod
    def getNextChoice(self, arrayCurrentChoice):
        #sets the current temp to be equal to the original choice
        #so unless theres something larger it will choose the same one
        tempCurrent = float(self.Values[getAbosolutePosition(arrayCurrentChoice, self.numberOfChoices)][self.playerNumber])
        tempPosition = arrayCurrentChoice[self.playerNumber]

        #loops through every choice this player can make
        for x in range(1, self.numberOfChoices[self.playerNumber]+1):
            arrayCurrentChoice[self.playerNumber] = x

            #if the choice is larger than the current choice change
            if (float(self.Values[getAbosolutePosition(arrayCurrentChoice, self.numberOfChoices)][self.playerNumber]) > tempCurrent):
                tempCurrent = float(self.Values[getAbosolutePosition(arrayCurrentChoice, self.numberOfChoices)][self.playerNumber])
                tempPosition = x

        return tempPosition

    def setCurrentOutcome(self, outcome):
        self.currentOutcome = outcome