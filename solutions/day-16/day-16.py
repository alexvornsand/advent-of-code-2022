# advent of code 2022
# day 16

# part 1
import re

valveRates = open('input.txt', 'r').read()[:-1].split('\n')

def releasePressure(valveRates, start=['AA'], timeRemaining=30, openedValves=[], pressureSoFar=0):
    def parseValves(valveRates):
        valves = {}
        for valve in valveRates:
            valveInfo = re.match('Valve\s(.{2}).*=(\d+).*valves?\s(.*)', valve).groups()
            name = valveInfo[0]
            rate = int(valveInfo[1])
            connectedValves = valveInfo[2].split(', ')
            valves[name] = {
                'rate': rate,
                'connectedValves': connectedValves
            }
        return(valves)
    def findValveRoutes(valves):
        pathBetweenValves = {}
        for start in valves:
            for end in valves:
                if start < end:
                    queue = [key for key in valves]
                    distances = dict({key: 999999 for key in valves})
                    distances[start] = 0
                    currentValve = start
                    while(True):
                        if currentValve == end:
                            path = [end]
                            currentValve = end
                            while(True):
                                for valve in valves[currentValve]['connectedValves']:
                                    if valve == start:
                                        path.append(start)
                                        break
                                    elif distances[valve] == distances[currentValve] - 1:
                                        if any([distances[next] == distances[currentValve] - 2 for next in valves[valve]['connectedValves']]):
                                            nextValve = valve
                                else:
                                    currentValve = nextValve
                                    path.append(currentValve)
                                    continue
                                break
                            pathBetweenValves[(start, end)] = path[::-1][1:]
                            pathBetweenValves[(end, start)] = path[1:]
                            break
                        for neighbor in valves[currentValve]['connectedValves']:
                            if neighbor in queue:
                                if distances[currentValve] + 1 < distances[neighbor]:
                                    distances[neighbor] = distances[currentValve] + 1
                            else:
                                pass
                        queue.remove(currentValve)
                        currentValve = sorted(queue, key=distances.get)[0]
                else:
                    pass
        return(pathBetweenValves)
    def findPath(valves, pathBetweenValves, valveSequence, unopenedValves, openedValves, timeRemaining, pressureSoFar):
        valve = valveSequence[-1]
        potentialNextValves = [nextValve for nextValve in unopenedValves if len(pathBetweenValves[valve, nextValve]) < timeRemaining - 2]
        if timeRemaining == 0 or len(potentialNextValves) == 0:
            nextPressureSoFar = pressureSoFar + sum([valves[open]['rate'] * timeRemaining for open in openedValves])
            return(valveSequence, nextPressureSoFar)
        else:
            nextSteps = []
            for nextValve in potentialNextValves:
                nextValveSequence = valveSequence.copy()
                nextValveSequence += [nextValve]
                nextPressureSoFar = pressureSoFar + sum([valves[openValve]['rate'] * (len(pathBetweenValves[(valve, nextValve)]) + 1) for openValve in openedValves])
                nextOpenedValves = openedValves.copy()
                nextOpenedValves += [nextValve]
                nextUnopenedValves = unopenedValves.copy()
                nextUnopenedValves.remove(nextValve)
                nextTimeRemaining = timeRemaining - len(pathBetweenValves[valve, nextValve]) - 1
                if valveSequence == originalInput:
                    print('valveRates=valveRates, start=' + str(nextValveSequence) + ', timeRemaining=' + str(nextTimeRemaining) + ', openedValves=' + str(nextOpenedValves) + ', pressureSoFar=' + str(nextPressureSoFar))
                nextValveResult = findPath(
                    valves=valves, 
                    pathBetweenValves=pathBetweenValves, 
                    valveSequence=nextValveSequence, 
                    unopenedValves=nextUnopenedValves, 
                    openedValves=nextOpenedValves, 
                    timeRemaining=nextTimeRemaining, 
                    pressureSoFar=nextPressureSoFar
                )
                if valveSequence == originalInput:
                    print(nextValveResult)
                nextSteps.append(nextValveResult)
            bestDownstream = max(nextSteps, key=lambda s: s[1])
            return(bestDownstream)

    valves = parseValves(valveRates)
    usefulValves = [valve for valve in valves if valves[valve]['rate'] > 0]
    pathBetweenValves = findValveRoutes(valves)
    unopenedValves = list(set(usefulValves.copy()).difference(set(openedValves)))
    valveSequence = originalInput = start

    return(findPath(valves, pathBetweenValves, valveSequence, unopenedValves, openedValves, timeRemaining, pressureSoFar))

releasePressure(valveRates)

# part 2
releasePressure(valveRates, True)
