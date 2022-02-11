import math
import os
from datetime import datetime

from AgentIBR import AgentIBR
from Joueur import Joueur
from Utils import *

playerChoices = [3,3,3]
players = []


if __name__ == '__main__':
    filename = datetime.today().strftime('%Y%m%d%H%M%S')
    #os.system('cmd /c "java -jar gamut.jar -g BattleOfTheSexes -normalize -min_payoff 0 -max_payoff 150 -f games/{0}.game"'.format(filename))
    os.system(
        'cmd /c "java -jar gamut.jar -g RandomGame -players 3 -normalize -min_payoff 0 -max_payoff 5 -int_payoffs -int_mult 1 -f BoS.game -actions 3 3 3 -f games/{0}.game"'.format(
            filename))
    file = open("games/{0}.game".format(filename), "r")

    Values, Positions = ConvertFileToArray(file)

    players = createPlayers(AgentIBR, playerChoices, Values)

    #choose a random choice for each player
    currentChoice = []
    for player in players:
        currentChoice.append(player.chooseStartingPoint())


    print(currentChoice)

    for step in range(5):
        currentChoice = iteration(players, currentChoice, Values, playerChoices, step)












