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

def getAbosolutePosition(arrayOfChoices, choicesPerPlayer):
    i = 0
    sum = 0
    combinedChoices = 1
    for x in arrayOfChoices:
        sum += combinedChoices * (x-1)
        combinedChoices *= choicesPerPlayer[i]
        i+=1
    return sum