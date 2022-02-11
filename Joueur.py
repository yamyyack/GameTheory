from abc import ABC, abstractmethod


class Joueur(ABC):


    @abstractmethod
    def getNextChoice(self):
        return (float)

    @abstractmethod
    def chooseStartingPoint(self):
        return (int)

