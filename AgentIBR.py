from Utils import *
from Joueur import Joueur
from abc import ABC
from IterativeChoice import *

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
        return IBR(self.playerNumber, self.numberOfChoices, arrayCurrentChoice, self.Values)


    def setCurrentOutcome(self, outcome):
        self.currentOutcome = outcome