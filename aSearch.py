'''
Course: CS3642
Student name: Erick Reyes
Student ID: 000762122
Assignment #: #1
Due Date: 03/05/2021
'''
import copy

#program will try to reach this state from the initial state
goalState = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

#initial state of the program
#has additional attributes to keep track of f-value as well 
#as assigning it its own id for future reference
initialState = [
    [2,4,6],
    [1,3,0],
    [8,7,5],
    0,          # g value
    0,          # h value
    0,          # f value
    0,          # id
    None        # child of
]

identifier = 1
openNodes = []
closedNodes = []
path = []

#determines whether initial state is solvable or not
def solvability(state):
    nums = []
    for x in range(3):
        for i in range(3):
            nums.append(state[x][i])
    nums.remove(0)
    total = 0
    loop = 1
    for x in nums[1:]:
        for i in range(loop):
            if x < nums[i]:
                total += 1
        loop += 1
    
    if total % 2 == 1:
        return True
    else:
        return False

#determines manhattan value of current state
def manhattan(state):
    total = 0
    for x in range(3):
        for y in range(3):
            if state[x][y] == 1:
                row = x
                col = y
                total += abs(row - 0) + abs(col - 0)
                break
    for x in range(3):
        for y in range(3):
            if state[x][y] == 2:
                row = x
                col = y
                total += abs(row - 0) + abs(col - 1)
                break       
    for x in range(3):
        for y in range(3):
            if state[x][y] == 3:
                row = x
                col = y
                total += abs(row - 0) + abs(col - 2)
                break
    for x in range(3):
        for y in range(3):
            if state[x][y] == 4:
                row = x
                col = y
                total += abs(row - 1) + abs(col - 2)
                break
    for x in range(3):
        for y in range(3):
            if state[x][y] == 5:
                row = x
                col = y
                total += abs(row - 2) + abs(col - 2)
                break
    for x in range(3):
        for y in range(3):
            if state[x][y] == 6:
                row = x
                col = y
                total += abs(row - 2) + abs(col - 1)
                break
    for x in range(3):
        for y in range(3):
            if state[x][y] == 7:
                row = x
                col = y
                total += abs(row - 2) + abs(col - 0)
                break
    for x in range(3):
        for y in range(3):
            if state[x][y] == 8:
                row = x
                col = y
                total += abs(row - 1) + abs(col - 0)
                break
    return total

#returns where blank space is located
def getZeroPosition(state):
    for x in range(3):
        for y in range(3):
            if state[x][y] == 0:
                row = x
                col = y
                break
    return row, col

#checks to see if new node already exists in the closed nodes to avoid repetition
def checkClosedNodes(state):
    for x in range(len(closedNodes)):
        if state[0:3] == closedNodes[x]:
            return True
    return False
    
#swaps blank position with number to the right
def moveR(state):
    global identifier
    a, b = getZeroPosition(state)
    if b == 2:
        return
    else:
        newState = copy.deepcopy(state)
        num = newState[a][b+1]
        newState[a][b+1] = 0
        newState[a][b] = num
        newState[4] = manhattan(newState)
        newState[3] = state[3] + 1
        newState[5] = newState[3] + newState[4]

        if not checkClosedNodes(newState):
            newState[6] = identifier
            newState[7] = state[6]
            openNodes.append(newState)
            identifier += 1

#swaps blank position with number to the left
def moveL(state):
    global identifier
    a, b = getZeroPosition(state)
    if b == 0:
        return
    else:
        newState = copy.deepcopy(state)
        num = newState[a][b-1]
        newState[a][b-1] = 0
        newState[a][b] = num
        newState[4] = manhattan(newState)
        newState[3] = state[3] + 1
        newState[5] = newState[3] + newState[4]
        
        if not checkClosedNodes(newState):
            newState[6] = identifier
            newState[7] = state[6]
            openNodes.append(newState)
            identifier += 1

#swaps blank position with number above
def moveU(state):
    global identifier
    a, b = getZeroPosition(state)
    if a == 0:
        return
    else:
        newState = copy.deepcopy(state)
        num = newState[a-1][b]
        newState[a-1][b] = 0
        newState[a][b] = num
        newState[4] = manhattan(newState)
        newState[3] = state[3] + 1
        newState[5] = newState[3] + newState[4]
        
        if not checkClosedNodes(newState):
            newState[6] = identifier
            newState[7] = state[6]
            openNodes.append(newState)
            identifier += 1

#swaps blank position with number below
def moveD(state):
    global identifier
    a, b = getZeroPosition(state)
    if a == 2:
        return
    else:
        newState = copy.deepcopy(state)
        num = newState[a+1][b]
        newState[a+1][b] = 0
        newState[a][b] = num
        newState[4] = manhattan(newState)
        newState[3] = state[3] + 1
        newState[5] = newState[3] + newState[4]
        
        if not checkClosedNodes(newState):
            newState[6] = identifier
            newState[7] = state[6]
            openNodes.append(newState)
            identifier += 1

#checks to see if the current state matches the goal state
def compare(currentState):
    if currentState[0:3] == goalState:
        return True
    else:
        return False

#sorts open nodes from least to greatest based on f-values
def sort(nodes): 
    nodes.sort(key = lambda x: x[5]) 
    return nodes

#build path from initial state to goal one node at a time
def findPath():
    i = 0
    path.append(openNodes[0][7])
    for x in range(len(closedNodes)):
        for j in range(len(closedNodes)):
            if closedNodes[j][6] == path[i]:
                path.append(closedNodes[j][7])
                i += 1
    path.reverse()

#shows user the steps taken from initial to goal state
def printPath():
    findPath()
    for x in range(len(path)):
        for i in range(len(closedNodes)):
            if path[x] == closedNodes[i][6]:
                for k in range(3):
                    print(closedNodes[i][k]) 
        print()
    for x in range(3):
        print(openNodes[0][x])

#calls to build new nodes and appends explored nodes to closed nodes list
def solve():
    while True:
        if compare(openNodes[0]):
            return
        moveR(openNodes[0])
        moveL(openNodes[0])
        moveU(openNodes[0])
        moveD(openNodes[0])
        closedNodes.append(openNodes.pop(0))
        sort(openNodes)

#initializes the open nodes list
if __name__ == '__main__':
    openNodes.append(initialState)
    openNodes[0][4] = manhattan(openNodes[0])
    openNodes[0][5] = openNodes[0][4]

    if solvability(openNodes[0]):
        solve()
        printPath()
    else:
        print("initial state has an even number of inversions and therefore is not solvable")