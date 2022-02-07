import math
import os
from datetime import datetime

from AgentIBR import AgentIBR
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

    for x in range(len(playerChoices)):
        players.append(AgentIBR(x, playerChoices, Values))

    currentChoice = [1,2,3]
    tempChoice = []
    for x in range(5):
        for player in players:
            tempChoice.append(player.getNextChoice(currentChoice.copy()))
        print("this is the choice after the : {0}".format(x))
        print(tempChoice)
        print("\n\n\n")
        i=0
        for player in players:
            player.setCurrentOutcome(float(Values[getAbosolutePosition(tempChoice, playerChoices)][i]))
            i+=1
        currentChoice = tempChoice
        tempChoice = []










