import math
import os
import json
from datetime import datetime

from Joueur import Joueur
from Utils import *
from FirstChoice import getAllPayoffForPlay
from IterativeChoice import *


def iteration(players, currentChoice, Values, playerChoices, step):
    tempChoice = []
    for player in players:
        tempChoice.append(player.getNextChoice(currentChoice.copy()))
    print("this is the choice after the : {0}".format(step+1))
    print(tempChoice)
    print("")
    i = 0
    for player in players:
        player.setCurrentOutcome(float(Values[getAbosolutePosition(tempChoice, playerChoices)][i]))
        i += 1
    return tempChoice

def createPlayers(playerChoices, Values, iterationMethod):
    players = []
    for x in range(len(playerChoices)):
        players.append(Joueur(x, playerChoices, Values, iterationMethod))
    return players

def ConvertFileToArray(file):
    Values = []
    Positions = []

    for line in file:
        if line[0] != "#":
            array = line.split(":")
            position = array[0][1:-2]
            value = array[1][3:-3]
            positionToArray = position.split("  ")
            valueToArray = value.split(" ")
            Positions.append(positionToArray)
            Values.append(valueToArray)
    return Values, Positions


def loadJsonFile():
    global playerChoices
    configSettings = ""
    f = open('config.json')
    data = json.load(f)

    configSettings += " -players " + str(len(data['number of choices per player'])) + " -actions "
    for x in data['number of choices per player']:
        configSettings += str(x) + " "
    configSettings += " -min_payoff " + str(data['min payoff']) + " -max_payoff " + str(data['max payoff'])
    if data['int payoff'] == True:
        configSettings += " -int_payoffs -int_mult " + str(data['int payoff multiplier'])

    playerChoices = data['number of choices per player']

    f.close()
    return configSettings

playerChoices = []
players = []


if __name__ == '__main__':
    filename = datetime.today().strftime('%Y%m%d%H%M%S')
    os.system(
        'cmd /c "java -jar gamut.jar -g RandomGame -normalize {0} -f games/{1}.game"'.format(loadJsonFile(), filename))
    file = open("games/{0}.game".format(filename), "r")

    Values, Positions = ConvertFileToArray(file)

    getAllPayoffForPlay(Values, 0, playerChoices, 1)

    players = createPlayers(playerChoices, Values, IBR)

    #choose a random choice for each player
    currentChoice = []
    for player in players:
        currentChoice.append(player.chooseStartingPoint())


    print(currentChoice)

    for step in range(5):
        currentChoice = iteration(players, currentChoice, Values, playerChoices, step)

    for player in players:
        print(player.toString())