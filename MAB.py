# Implementing UCB
import math


def MAB(a, dict):
    max_upper_bound = 0
    for i in range(dict["number of choices"]):
        #selection process (which one to take)
        if (dict["number of selection"][i] > 0):
            length = len(dict["list of value"][i])
            average_reward = 0
            #gets the weighted averga with the most recent values worth more
            #value in the array (value of 25) * it position (position 3) / total sum(1 + 2 + 3 + 4...)
            for x in range(length):
                average_reward += dict["list of value"][i][x] * ((x+1)/((length*(length+1))/2))

            delta_i = math.sqrt(2*math.log(dict["MAB number of total plays"] + 1, 10) / dict["number of selection"][i]) * dict["max possible value"]

            upper_bound = delta_i + average_reward
        else:
            upper_bound = 1e400

        if(upper_bound > max_upper_bound):
            max_upper_bound = upper_bound
            dict.update({"selection" : i})

    temparray = dict["number of selection"]
    temparray[dict["selection"]] += 1

    dict.update({"number of selection" : temparray})
    print(dict["selection"])
    return dict["selection"]