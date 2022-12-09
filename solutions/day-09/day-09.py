# advent of code 2022
# day 9

# part 1
headMoves = open('input.txt', 'r').read().split('\n')[:-1]

def traceTail(headMoves, partTwo=False):
    if partTwo is False:
        positions = {
            'h': [0,0],
            't': [0,0]        
        }
        knots = ['h', 't']
    else:
        positions = {
            'h': [0,0],
            '1': [0,0],
            '2': [0,0],
            '3': [0,0],
            '4': [0,0],
            '5': [0,0],
            '6': [0,0],
            '7': [0,0],
            '8': [0,0],
            't': [0,0]        
        }
        knots = ['h', '1', '2', '3', '4', '5', '6', '7', '8', 't']
    tailPositions = {}
    tailPositions[tuple(positions['h'])] = [0]
    movements = {
        'R': [1,0],
        'L': [-1,0],
        'U': [0,1],
        'D': [0,-1]
    }
    time = 0
    for move in headMoves:
        for i in range(int(move[2:])):
            time += 1
            positions['h'] = [a + b for a, b in zip(positions['h'], movements[move[0]])]
            for i in range(1,len(knots)):
                if abs(positions[knots[i - 1]][0] - positions[knots[i]][0]) == 2 and positions[knots[i - 1]][1] == positions[knots[i]][1]:
                    positions[knots[i]][0] = int((positions[knots[i - 1]][0] + positions[knots[i]][0]) / 2)
                    if knots[i] == 't':
                        if tuple(positions[knots[i]]) in tailPositions.keys():
                            tailPositions[tuple(positions[knots[i]])].append(time)
                        else:
                            tailPositions[tuple(positions[knots[i]])] = [time]
                elif abs(positions[knots[i - 1]][1] - positions[knots[i]][1]) == 2 and positions[knots[i - 1]][0] == positions[knots[i]][0]:
                    positions[knots[i]][1] = int((positions[knots[i - 1]][1] + positions[knots[i]][1]) / 2)
                    if knots[i] == 't':
                        if tuple(positions[knots[i]]) in tailPositions.keys():
                            tailPositions[tuple(positions[knots[i]])].append(time)
                        else:
                            tailPositions[tuple(positions[knots[i]])] = [time]
                elif abs(positions[knots[i - 1]][0] - positions[knots[i]][0]) == 2 and abs(positions[knots[i - 1]][1] - positions[knots[i]][1]) == 1:
                    positions[knots[i]][0] = int((positions[knots[i - 1]][0] + positions[knots[i]][0]) / 2)
                    positions[knots[i]][1] = positions[knots[i - 1]][1]
                    if knots[i] == 't':
                        if tuple(positions[knots[i]]) in tailPositions.keys():
                            tailPositions[tuple(positions[knots[i]])].append(time)
                        else:
                            tailPositions[tuple(positions[knots[i]])] = [time]
                elif abs(positions[knots[i - 1]][1] - positions[knots[i]][1]) == 2 and abs(positions[knots[i - 1]][0] - positions[knots[i]][0]) == 1:
                    positions[knots[i]][1] = int((positions[knots[i - 1]][1] + positions[knots[i]][1]) / 2)
                    positions[knots[i]][0] = positions[knots[i - 1]][0]
                    if knots[i] == 't':
                        if tuple(positions[knots[i]]) in tailPositions.keys():
                            tailPositions[tuple(positions[knots[i]])].append(time)
                        else:
                            tailPositions[tuple(positions[knots[i]])] = [time]
                elif abs(positions[knots[i - 1]][1] - positions[knots[i]][1]) == 2 and abs(positions[knots[i - 1]][0] - positions[knots[i]][0]) == 2:
                    positions[knots[i]][1] = int((positions[knots[i - 1]][1] + positions[knots[i]][1]) / 2)
                    positions[knots[i]][0] = int((positions[knots[i - 1]][0] + positions[knots[i]][0]) / 2)
                    if knots[i] == 't':
                        if tuple(positions[knots[i]]) in tailPositions.keys():
                            tailPositions[tuple(positions[knots[i]])].append(time)
                        else:
                            tailPositions[tuple(positions[knots[i]])] = [time]

                else:
                    if knots[i] == 't':
                        if tuple(positions[knots[i]]) in tailPositions.keys():
                            tailPositions[tuple(positions[knots[i]])].append(time)
                        else:
                            tailPositions[tuple(positions[knots[i]])] = [time]
    return(len(tailPositions.keys()))

traceTail(headMoves)

# part 2
traceTail(headMoves, True)