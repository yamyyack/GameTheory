import math
import os
import json
import time
from datetime import datetime

from Joueur import Joueur
from Utils import *
from FirstChoice import getAllPayoffForPlay
from IterativeChoice import *
from FirstChoice import *
from MAB import *

anarchyValue = 0
anarchyValuePos = []

def selectionProcess(players, Values, playerChoices, anarchyValue, anarchyValuePos, f):
    currentChoice = []
    for player in players:
        currentChoice.append(player.chooseStartingPoint())

    for step in range(1000):
        currentChoice = iteration(players, currentChoice, Values, playerChoices, step)

    f.write("\n\nonce normalization is done : \n")
    playersum = 0
    for player in players:
        playersum += player.currentOutcome
        print(player.behaviorToString())
        f.write(player.behaviorToString())
    f.write("Anarchy value : {0}/{1}\n".format(str(playersum), str(anarchyValue)))
    print("Anarchy value : {0}/{1}".format(str(playersum), str(anarchyValue)))
    print("Following choices will give the Anarchy value : {0}".format(anarchyValuePos))
    f.write("Following choices will give the Anarchy value : {0}\n".format(anarchyValuePos))
    return playersum, currentChoice

def setAnarchyValue(Values, Positions):
    global anarchyValue
    global anarchyValuePos
    anarchyValuePos = []
    anarchyValue = 0
    for index, results in enumerate(Values):
        sum = 0
        for x in results:
            sum += int(x)
        if sum > anarchyValue:
            anarchyValuePos = []
            anarchyValue = sum
        if sum == anarchyValue:
            anarchyValuePos.append(Positions[index])

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

def createPlayers(playerChoices, Values, playerinfo):

    players = []
    for x in playerinfo:
        infoDict = {}
        if(x['starting method'] == "minmax"):
            StartingMethod = minmax
            if "tableValue" not in infoDict:
                infoDict.update({"tableValue" : Values})
                infoDict.update({"number of choices": playerChoices})
                infoDict.update({"player number": x['player number']})
        elif (x['starting method'] == "MAB"):
            StartingMethod = MAB
            if "MAB number of total plays" not in infoDict:
                infoDict.update({"MAB number of total plays": 0})


                infoDict.update({"number of choices": (playerChoices[x['player number']-1])})

                temparray = [0]*(playerChoices[x['player number']-1])
                infoDict.update({"number of selection": temparray})

                infoDict.update({"selection" : -1})

                temparray = [[]] * (playerChoices[x['player number']-1])
                infoDict.update({"list of value": temparray})

                infoDict.update({"max possible value": 10})

        if(x['iteration method'] == "IBR"):
            iterationMethod = IBR
            if "tableValue" not in infoDict:
                infoDict.update({"tableValue" : Values})
                infoDict.update({"number of choices": playerChoices})
                infoDict.update({"player number": x['player number']})
                infoDict.update({"array Current Choice" : -1})

        elif (x['iteration method'] == "MAB"):
            iterationMethod = MAB
            if "MAB number of total plays" not in infoDict:
                infoDict.update({"MAB number of total plays": 0})

                infoDict.update({"number of choices": (playerChoices[x['player number']-1])})

                temparray = [0]*(playerChoices[x['player number']]-1)
                infoDict.update({"number of selection": temparray})

                infoDict.update({"selection" : -1})

                temparray = [[]] * (playerChoices[x['player number']] - 1)
                infoDict.update({"list of value": temparray})

                infoDict.update({"max possible value": 10})



        players.append(Joueur(x["player number"], playerChoices, infoDict, iterationMethod, StartingMethod))
    return players

def ConvertFileToArray(file):
    Values = []
    Positions = []

    for line in file:
        if line[0] != "#":
            array = line.split(":")
            position = array[0][1:-2]
            value = array[1][3:-3]
            positionToArray = [float(posiiton) for posiiton in position.split("  ")]
            valueToArray = [float(tempValue) for tempValue in value.split(" ")]
            Positions.append(positionToArray)
            Values.append(valueToArray)
    return Values, Positions


def loadJsonFile():
    global playerChoices
    configSettings = ""
    f = open('config.json')
    data = json.load(f)

    GameInfo = data["game info"]
    PlayerInfo = data['player info']

    configSettings += " -players " + str(len(GameInfo['number of choices per player'])) + " -actions "
    for x in GameInfo['number of choices per player']:
        configSettings += str(x) + " "
    configSettings += " -min_payoff " + str(GameInfo['min payoff']) + " -max_payoff " + str(GameInfo['max payoff'])
    if GameInfo['int payoff'] == True:
        configSettings += " -int_payoffs -int_mult " + str(GameInfo['int payoff multiplier'])

    playerChoices = GameInfo['number of choices per player']


    f.close()
    return configSettings, PlayerInfo

playerChoices = []
players = []


if __name__ == '__main__':
    wTotal = 0
    wError = 0
    wPlayerF = 0
    wPlayerO = 0
    for var in range(10):
        filename = ""
        time.sleep(1)
        filename = datetime.today().strftime('%Y%m%d%H%M%S')
        gameinfo, playerinfo = loadJsonFile()
        os.system(
            'cmd /c "java -jar gamut.jar -g RandomGame -normalize {0} -f games/{1}.game"'.format(gameinfo, filename))
        file = open("games/{0}.game".format(filename), "r")

        Values, Positions = ConvertFileToArray(file)

        setAnarchyValue(Values, Positions)
        players = createPlayers(playerChoices, Values, playerinfo)

        f = open("outcome/{0}.txt".format(filename), "x")
        f = open("outcome/{0}.txt".format(filename), "a")

        #choose a random choice for each player
        playersum, currentChoice = selectionProcess(players, Values, playerChoices, anarchyValue, anarchyValuePos, f)

        originalsum = playersum

        #normalize
        #Values = normalize(Values, playersum, currentChoice, playerChoices, players)

        #k-implementation
        #K_implementaion(anarchyValuePos, Positions, Values)

        #reiterate
        #playersum, currentChoice = selectionProcess(players, Values, playerChoices, anarchyValue, anarchyValuePos, f)


        #final
        print("changes from {0} to {1}".format(originalsum, playersum))
        f.write("changes from {0} to {1}\n".format(originalsum, playersum))

        if(playersum >= anarchyValue+1):
            wError +=1
        else:
            wTotal += anarchyValue
            wPlayerO += originalsum
            wPlayerF += playersum

        f.close
        f = open("debug/{0}.txt".format(filename), "x")
        f = open("debug/{0}.txt".format(filename), "a")

        for x in Values:
            f.write("[")
            for y in x:
                f.write(str(y))
                f.write(", ")
            f.write("]\n")

        for player in players:
            del player

    print("total max")
    print(wTotal)
    print("total player original")
    print(wPlayerO)
    print("total player final")
    print(wPlayerF)
    print("error count : ")
    print(wError)