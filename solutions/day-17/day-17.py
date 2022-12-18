import time
import os

wind = open('input.txt', 'r').read()[:-1]
#wind = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
def playTetris(wind, n=2022, printImage=False):
    def checkCollisions(stack, currentRock, wind):
        rock = currentRock.copy()
        crashed = False
        if rock['shape'] == '-':
            # check for collisions on the side
            if wind == '<':
                # check for horizontal collision with wall
                if rock['pos'][0] == 1:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1]) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] - 1, rock['pos'][1])
            else:
                # check for horizontal collision with wall
                if rock['pos'][0] == 4:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 4, rock['pos'][1]) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] + 1, rock['pos'][1])

            # check for collisions with the ground
            if rock['pos'][1] == 1:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0], rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 1, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 2, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 3, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            else:
                # update rock position
                rock['pos'] = (rock['pos'][0], rock['pos'][1] - 1)
        elif rock['shape'] == '+':
            # check for collisions on the side
            if wind == '<':
                # check for horizontal collision with wall
                if rock['pos'][0] == 1:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0], rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0], rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] - 1, rock['pos'][1])
            else:
                # check for horizontal collision with wall
                if rock['pos'][0] == 5:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 2, rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 3, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 2, rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] + 1, rock['pos'][1])

            # check for collisions with the ground
            if rock['pos'][1] == 1:
                # crashed
                crashed = True
            # check for vertical collision with the stack
            elif (rock['pos'][0] + 1, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collision with the stack
            elif (rock['pos'][0], rock['pos'][1]) in stack:
                # crashed
                crashed = True
            # check for vertical collision with the stack
            elif (rock['pos'][0] + 2, rock['pos'][1]) in stack:
                # crashed
                crashed = True
            else:
                # update rock position
                rock['pos'] = (rock['pos'][0], rock['pos'][1] - 1)
        elif rock['shape'] == 'L':
            # check for collisions on the side
            if wind == '<':
                # check for horizontal collision with wall
                if rock['pos'][0] == 1:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] - 1, rock['pos'][1])
            else:
                # check for horizontal collision with wall
                if rock['pos'][0] == 5:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 3, rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 3, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 3, rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] + 1, rock['pos'][1])

            # check for collisions with the ground
            if rock['pos'][1] == 1:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0], rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 1, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 2, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            else:
                # update rock position
                rock['pos'] = (rock['pos'][0], rock['pos'][1] - 1)
        elif rock['shape'] == 'I':
            # check for collisions on the side
            if wind == '<':
                # check for horizontal collision with wall
                if rock['pos'][0] == 1:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1] + 3) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] - 1, rock['pos'][1])
            else:
                # check for horizontal collision with wall
                if rock['pos'][0] == 7:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1] + 3) in stack:
                    # crashed
                    pass

                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] + 1, rock['pos'][1])

            # check for collisions with the ground
            if rock['pos'][1] == 1:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0], rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            else:
                # update rock position
                rock['pos'] = (rock['pos'][0], rock['pos'][1] - 1)
        else:
            # check for collisions on the side
            if wind == '<':
                # check for horizontal collision with wall
                if rock['pos'][0] == 1:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1]) in stack:
                    # crashed
                    pass
                elif (rock['pos'][0] - 1, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] - 1, rock['pos'][1])
            else:
                # check for horizontal collision with wall
                if rock['pos'][0] == 6:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 2, rock['pos'][1]) in stack:
                    # crashed
                    pass
                elif (rock['pos'][0] - 2, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] + 1, rock['pos'][1])

            # check for collisions with the ground
            if rock['pos'][1] == 1:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0], rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 1, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            else:
                # update rock position
                rock['pos'] = (rock['pos'][0], rock['pos'][1] - 1)
        return(rock, crashed)
    def generateNextRock(maxHeight, rockIndex):
        rocks = ['-', '+', 'L', 'I', 'o']
        rockType = rocks[rockIndex % 5]
        position = (3, maxHeight + 4)
        rock = {
            'shape': rockType,
            'pos': position
        }
        return(rock)
    def rockCoordinates(rock):
        if rock['shape'] == '-':
            return([
                (rock['pos'][0], rock['pos'][1]),
                (rock['pos'][0] + 1, rock['pos'][1]),
                (rock['pos'][0] + 2, rock['pos'][1]),
                (rock['pos'][0] + 3, rock['pos'][1]),
            ])
        elif rock['shape'] == '+':
            return([
                (rock['pos'][0], rock['pos'][1] + 1),
                (rock['pos'][0] + 1, rock['pos'][1]),
                (rock['pos'][0] + 1, rock['pos'][1] + 1),
                (rock['pos'][0] + 1, rock['pos'][1] + 2),
                (rock['pos'][0] + 2, rock['pos'][1] + 1),
            ])
        elif rock['shape'] == 'L':
            return([
                (rock['pos'][0], rock['pos'][1]),
                (rock['pos'][0] + 1, rock['pos'][1]),
                (rock['pos'][0] + 2, rock['pos'][1]),
                (rock['pos'][0] + 2, rock['pos'][1] + 1),
                (rock['pos'][0] + 2, rock['pos'][1] + 2),
            ])
        elif rock['shape'] == 'I':
            return([
                (rock['pos'][0], rock['pos'][1]),
                (rock['pos'][0], rock['pos'][1] + 1),
                (rock['pos'][0], rock['pos'][1] + 2),
                (rock['pos'][0], rock['pos'][1] + 3),
            ])
        else:
            return([
                (rock['pos'][0], rock['pos'][1]),
                (rock['pos'][0] + 1, rock['pos'][1]),
                (rock['pos'][0], rock['pos'][1] + 1),
                (rock['pos'][0] + 1, rock['pos'][1] + 1)
            ])
    def printStack(stack, i, rock=[], m=0):
        m = max(0, m)
        image = ''
        for r in range(m, m + 9)[::-1]:
            if r == m + 8:
                image += str(i).ljust(6, ' ')
            else:
                image += '      '
            if r == m + 8:
                image += ''
            if r == 0:
                image += '+'
            else:
                image += '|'
            for c in range(1, 8):
                if (c,r) in stack:
                    image += '#'
                elif (c,r) in rock:
                    image += '@'
                elif r == 0:
                    image += '-'
                else:
                    image += '.'
            if r == 0:
                image += '+'
            else:
                image += '|'
            if r % 5 == 0:
                image += str(r).rjust(5, ' ')
            else:
                image += '     '
            image += '\n'
        os.system('cls')
        print(image, end='\r')
        if i == n:
            time.slee(1)
        elif i > n - 3:
            time.sleep(.25)
    modularity = len(wind)
    maxHeight = 0
    stack = []
    w = 0
    maxHeights = []
    for i in range(n):
        currentRock = generateNextRock(maxHeight, i)
        crashed = False
        if printImage == 'all':
            printStack(stack, i, rockCoordinates(currentRock), currentRock['pos'][1] - 4)
        while(crashed is False):
            currentRock, crashed = checkCollisions(stack, currentRock, wind[w % modularity])
            if printImage  == 'all':
                printStack(stack, i, rockCoordinates(currentRock), currentRock['pos'][1] - 4)
            if crashed is True:
                stack += rockCoordinates(currentRock)
                maxHeight = max([coord[1] for coord in stack])
                maxHeights.append(maxHeight)
                w += 1
                if printImage == 'all':
                    printStack(stack, i, rockCoordinates(currentRock), currentRock['pos'][1] - 4)
            else:
                w += 1
    if printImage == 'all' or printImage == 'last':
        printStack(stack, i, m=currentRock['pos'][1] - 4)
    return(maxHeight)
playTetris(wind, 47, printImage = 'all')
