from Utils import *
from abc import ABC
from IterativeChoice import *
from FirstChoice import *

class Joueur():

    def __init__(self, playerNumber, numberOfChoices, values, iterationMethod):
        self.playerNumber = playerNumber
        self.numberOfChoices = numberOfChoices
        self.Values = values
        self.currentOutcome = 0
        self.iterationMethod = iterationMethod
        self.maxOutcome = 0
        self.minOutcome = 99999999999
        self.averageOutcome = 0
        self.iterationCount = 0

    def chooseStartingPoint(self):
        return minmax(self.numberOfChoices, self.Values, self.playerNumber)

    #overriding abstract mrthod
    def getNextChoice(self, arrayCurrentChoice):
        return self.iterationMethod(self.playerNumber, self.numberOfChoices, arrayCurrentChoice, self.Values)


    def setCurrentOutcome(self, outcome):
        if(outcome > self.maxOutcome):
            self.maxOutcome = outcome
        if(outcome < self.minOutcome):
            self.minOutcome = outcome
        self.currentOutcome = outcome
        self.iterationCount +=1
        self.averageOutcome += (outcome - self.averageOutcome)/self.iterationCount


    def toString(self):
        return "player number {0} had a max value of {1}, and a min value of {2} and the average of {3}\nthey are currently " \
        "sitting at {4}".format(
            self.playerNumber, self.maxOutcome, self.minOutcome, self.averageOutcome, self.currentOutcome)