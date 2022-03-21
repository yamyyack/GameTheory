from Utils import *
from abc import ABC
from IterativeChoice import *
from FirstChoice import *

class Joueur():

    def __init__(self, playerNumber, numberOfChoices, values, iterationMethod, startMethod):
        self.playerNumber = playerNumber
        self.numberOfChoices = numberOfChoices
        self.Values = values
        self.currentOutcome = 0
        self.iterationMethod = iterationMethod
        self.maxOutcome = 0
        self.minOutcome = 99999999999
        self.averageOutcome = 0
        self.iterationCount = 0
        self.startMethod = startMethod

    def chooseStartingPoint(self):
        self.startPosition = self.startMethod(self.numberOfChoices, self.Values, self.playerNumber)
        return self.startPosition

    #overriding abstract mrthod
    def getNextChoice(self, arrayCurrentChoice):
        self.currentChoice = self.iterationMethod(self.playerNumber, self.numberOfChoices, arrayCurrentChoice, self.Values)
        return self.currentChoice


    def setCurrentOutcome(self, outcome):
        if(outcome > self.maxOutcome):
            self.maxOutcome = outcome
        if(outcome < self.minOutcome):
            self.minOutcome = outcome
        self.currentOutcome = outcome
        self.iterationCount +=1
        self.averageOutcome += (outcome - self.averageOutcome)/self.iterationCount

    def updateValues(self, Values):
        self.Values = Values


    def toString(self):
        return "player number {0} had a max value of {1}, and a min value of {2} and the average of {3}\nthey are currently " \
        "sitting at {4}".format(
            self.playerNumber, self.maxOutcome, self.minOutcome, self.averageOutcome, self.currentOutcome)

    def behaviorToString(self):
        return "player {0} " \
               "\n\toriginal choice method : {1}" \
               "\n\titerated method : {2}" \
               "\n\tcurrent choice : {7}"\
               "\n\tcurrent outcome : {6}" \
               "\n\thighest value : {3}" \
               "\n\taverage value : {4}" \
               "\n\tlowest value  : {5}" \
            "\n\n".format(self.playerNumber, self.startMethod.__name__, self.iterationMethod.__name__, self.maxOutcome,
                   self.averageOutcome, self.minOutcome, self.currentOutcome, self.currentChoice)