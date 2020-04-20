import argparse


class Player:
    def __init__(self):
        self._dead = 0
        self._x = 0
        self._y = 0
        self._canmove = 0
        self._ammo = 0
        self._startX = 0
        self._startY = 0
    
    def set_corr(self, x, y):
        self._x = x
        self._y = y
    
    def set_start(self, startX, startY):
        self._startX = startX
        self._startY = startY
    
    def set_ammo(self, count):
        self._ammo = count
    
    def set_stun(self, stun):
        self._canmove = stun
    
    def set_dead(self):
        self._x = _startX
        self._y = _startY
    
    def backpack_info(self):
        print(self._dead, end=' ')
        print(self._x, end=' ')
        print(self._y, end=' ')
        
        print(self._canmove, end=' ')
        print(self._ammo)
    
    def helpIns(self):
        print("Enter w to move up")
        print("Enter s to move down")
        print("Enter d to move right")
        print("Enter a to move left")
        print("Enter shoot w to shoot up")
        print("Enter shoot s to shoot down")
        print("Enter shoot d to shoot right")
        print("Enter shoot a to shoot left")
        print("Enter backpack to show your status")
        
    def shootU(self, graph, players):
        if self._ammo > 0:
            self._ammo -= 1
            currX = self._x
            currY = self._y
            while graph[currX][currY]._moveableU == 0:
                for p in players:
                    if p._x == currX and p._y == currY and p != self:
                        p.set_dead
                        print("You shot someone")
                currX -= 1
            for p in players:
                    if p._x == currX and p._y == currY and p != self:
                        p.set_dead
                        print("You shot someone")
        else:
            print("You have no ammo")
    
    def shootD(self, graph, players):
        if self._ammo > 0:
            self._ammo -= 1
            currX = self._x
            currY = self._y
            while graph[currX][currY]._moveableD == 0:
                for p in players:
                    if p._x == currX and p._y == currY and p != self:
                        p.set_dead
                        print("You shot someone")
                currX += 1
            for p in players:
                    if p._x == currX and p._y == currY and p != self:
                        p.set_dead
                        print("You shot someone")
        else:
            print("You have no ammo")
    
    def shootR(self, graph, players):
        if self._ammo > 0:
            self._ammo -= 1
            currX = self._x
            currY = self._y
            while graph[currX][currY]._moveableR == 0:
                for p in players:
                    if p._x == currX and p._y == currY and p != self:
                        p.set_dead
                        print("You shot someone")
                currY += 1
            for p in players:
                    if p._x == currX and p._y == currY and p != self:
                        p.set_dead
                        print("You shot someone")
        else:
            print("You have no ammo")
    
    def shootL(self, graph, players):
        if self._ammo > 0:
            self._ammo -= 1
            currX = self._x
            currY = self._y
            while graph[currX][currY]._moveableL == 0:
                for p in players:
                    if p._x == currX and p._y == currY and p != self:
                        p.set_dead
                        print("You shot someone")
                currY -= 1
            for p in players:
                    if p._x == currX and p._y == currY and p != self:
                        p.set_dead
                        print("You shot someone")
        else:
            print("You have no ammo")


class Cell:
    def __init__(self):
        self._moveableR = 0
        self._moveableL = 0
        self._moveableU = 0
        self._moveableD = 0
        self._ammo = 0
        self._cellType = 0
    
    def print_cell(self):
        print(self._moveableR, end=' ')
        print(self._moveableL, end=' ')
        print(self._moveableU, end=' ')
        print(self._moveableD, end=' ')
        print(self._ammo, end=' ')
        print(self._cellType) 
   
   
def WriteMaze(MAZE):
    path = input()
    handle = open(path, "w")
    for item in range(len(MAZE)):
        handle.write("%s\n" % str(MAZE[item]))
    handle.close()


def OpenAndShowMaze(path):
    f = open(path, "r")
    labi = list()
    currline = ""
    for line in f:
        currline = currline + line[0:-1]
        if(line[-2] == ']'):
            mline = currline
            labi.append(list(currline.replace(']', ' ')
                             .replace('[', ' ').split()))
            currline = ""
    f.close()
    
    b = len(mline.split())
    a = int((len(labi)/2) + 1)
    
    actualMaze = [[Cell() for i in range(a)] for j in range(b)]
    t = 0
    
    for i in range(len(labi)):
        wallCount = 0
        for j in range(len(labi[i])):
            if t == 0:
                
                if labi[i][j] == "|":
                    actualMaze[int(i/2)][j-wallCount-1]._moveableR = 1
                    actualMaze[int(i/2)][j-wallCount]._moveableL = 1 
                    wallCount += 1
                else:
                    
                    if int(i/2) == 0:
                        actualMaze[int(i/2)][j-wallCount]._moveableU = 1
                    if int(i/2) == a-1:
                        actualMaze[int(i/2)][j-wallCount]._moveableD = 1
                    if int(j-wallCount) == 0:
                        actualMaze[int(i/2)][j-wallCount]._moveableL = 1
                    if int(j-wallCount) == b-1:
                        actualMaze[int(i/2)][j-wallCount]._moveableR = 1
                
                    if labi[i][j] == "S":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "S"
                    elif labi[i][j] == "R":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "R"
                        actualMaze[int(i/2)][j-wallCount]._moveableD = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableL = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableU = 1
                    elif labi[i][j] == "L":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "L"
                        actualMaze[int(i/2)][j-wallCount]._moveableD = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableR = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableU = 1
                    elif labi[i][j] == "U":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "U"
                        actualMaze[int(i/2)][j-wallCount]._moveableD = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableL = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableR = 1
                    elif labi[i][j] == "D":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "D"
                        actualMaze[int(i/2)][j-wallCount]._moveableR = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableL = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableU = 1
                    elif labi[i][j] == "T":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "T"
                    elif labi[i][j] == "E":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "E"
                    elif labi[i][j] == "A":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "A"
                    elif labi[i][j] == "|":
                        actualMaze[int(i/2)][j-wallCount-1]._moveableR = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableL = 1 
                        wallCount += 1
            
            else:
                if labi[i][j] == "_":
                    actualMaze[int(i/2)][j]._moveableD = 1
                    actualMaze[int((i/2)+1)][j]._moveableU = 1
        if t == 0:
            t = 1
        else:
            t = 0
                
    return actualMaze


def WriteMaze():
    size = input()
    sizeList = size.split()
    a = int(sizeList[0])
    b = int(sizeList[1])
    actualMaze = [[Cell() for i in range(a)] for j in range(b)]
    labi = list()
    for i in range(b*2-1):
        s = input()
        labi.append(s.split())
    t = 0
    for i in range(len(labi)):
        wallCount = 0
        for j in range(len(labi[i])):
            if t == 0:
                
                if labi[i][j] == "|":
                    actualMaze[int(i/2)][j-wallCount-1]._moveableR = 1
                    actualMaze[int(i/2)][j-wallCount]._moveableL = 1 
                    wallCount += 1
                else:
                    
                    if int(i/2) == 0:
                        actualMaze[int(i/2)][j-wallCount]._moveableU = 1
                    if int(i/2) == a-1:
                        actualMaze[int(i/2)][j-wallCount]._moveableD = 1
                    if int(j-wallCount) == 0:
                        actualMaze[int(i/2)][j-wallCount]._moveableL = 1
                    if int(j-wallCount) == b-1:
                        actualMaze[int(i/2)][j-wallCount]._moveableR = 1
                
                    if labi[i][j] == "S":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "S"
                    elif labi[i][j] == "R":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "R"
                        actualMaze[int(i/2)][j-wallCount]._moveableD = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableL = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableU = 1
                    elif labi[i][j] == "L":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "L"
                        actualMaze[int(i/2)][j-wallCount]._moveableD = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableR = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableU = 1
                    elif labi[i][j] == "U":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "U"
                        actualMaze[int(i/2)][j-wallCount]._moveableD = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableL = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableR = 1
                    elif labi[i][j] == "D":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "D"
                        actualMaze[int(i/2)][j-wallCount]._moveableR = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableL = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableU = 1
                    elif labi[i][j] == "T":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "T"
                    elif labi[i][j] == "E":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "E"
                    elif labi[i][j] == "A":
                        actualMaze[int(i/2)][j-wallCount]._cellType = "A"
                    elif labi[i][j] == "|":
                        actualMaze[int(i/2)][j-wallCount-1]._moveableR = 1
                        actualMaze[int(i/2)][j-wallCount]._moveableL = 1 
                        wallCount += 1
            
            else:
                if labi[i][j] == "_":
                    actualMaze[int(i/2)][j]._moveableD = 1
                    actualMaze[int((i/2)+1)][j]._moveableU = 1
        if t == 0:
            t = 1
        else:
            t = 0
    return actualMaze


def DFSwithTP(corr, form, graph):           
    
    canExit = 0
    visited = [[0]*form[0] for _ in range(form[1])]
    stack = []
    stack.append(corr)  
    visited[corr[0]][corr[1]] = 1
     
    while (len(stack)):  

        s = stack[-1]  
        stack.pop() 
        
        if graph[s[0]][s[1]]._cellType == "E":
            canExit = 1
            return canExit

        if graph[s[0]][s[1]]._moveableU == 0:
            if graph[s[0] - 1][s[1]]._cellType != "T":
                if visited[s[0] - 1][s[1]] == 0:
                    visited[s[0] - 1][s[1]] = 1
                    stack.append((s[0] - 1, s[1]))
                    
        if graph[s[0]][s[1]]._moveableD == 0:
            if graph[s[0] + 1][s[1]]._cellType != "T":
                if visited[s[0]+1][s[1]] == 0:
                    visited[s[0]+1][s[1]] = 1
                    stack.append((s[0]+1, s[1]))
                    
        if graph[s[0]][s[1]]._moveableL == 0:
            if graph[s[0]][s[1]-1]._cellType != "T":
                if visited[s[0]][s[1]-1] == 0:
                    visited[s[0]][s[1]-1] = 1
                    stack.append((s[0], s[1]-1))
        
        if graph[s[0]][s[1]]._moveableR == 0:
            if graph[s[0]][s[1]+1]._cellType != "T":
                if visited[s[0]][s[1]+1] == 0:
                    visited[s[0]][s[1]+1] = 1
                    stack.append((s[0], s[1] + 1))
    
    print("end")
    return canExit 


def DFSwithoutTP(corr, form, graph):           
    canExit = 0
    visited = [[0]*form[0] for _ in range(form[1])]
    stack = [] 
    stack.append(corr)  
    visited[corr[0]][corr[1]] = 1
     
    while (len(stack)):  

        s = stack[-1]  
        stack.pop() 
        
        if graph[s[0]][s[1]]._cellType == "E" or graph[s[0]][s[1]]._cellType == "T":
            canExit = 1
            return canExit

        if graph[s[0]][s[1]]._moveableU == 0:
            if visited[s[0] - 1][s[1]] == 0:
                visited[s[0] - 1][s[1]] = 1
                stack.append((s[0] - 1, s[1]))
                    
        if graph[s[0]][s[1]]._moveableD == 0:
            if visited[s[0]+1][s[1]] == 0:
                visited[s[0]+1][s[1]] = 1
                stack.append((s[0]+1, s[1]))
                    
        if graph[s[0]][s[1]]._moveableL == 0:
            if visited[s[0]][s[1]-1] == 0:
                visited[s[0]][s[1]-1] = 1
                stack.append((s[0], s[1]-1))
        
        if graph[s[0]][s[1]]._moveableR == 0:
            if visited[s[0]][s[1]+1] == 0:
                visited[s[0]][s[1]+1] = 1
                stack.append((s[0], s[1] + 1))
    
    print("end")
    return canExit    
 

def play(actualMaze, players):
    while(True):
        for i in range(len(players)):
            if(players[i]._canmove == 0):
                print("Player " + str(i + 1) + " - your turn")
                command = ""
                while command != "w" and command != "s" and command != "d" and command != "a" and command != "shoot w" and command != "shoot d" and command != "shoot s" and command != "shoot a":
                    command = input()
                    if command == "w":
                        if actualMaze[players[i]._x][players[i]._y]._cellType == "E":
                            if(commToExit == "w"):
                                return i
                        
                        if actualMaze[players[i]._x][players[i]._y]._moveableU == 0:
        
                            players[i].set_corr(players[i]._x - 1, players[i]._y)
                            print("You moved 1 cell up")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "S":
                                players[i].set_stun(stunCount)
                                print("You are stunned for " + str(stunCount) + " turns")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "A":
                                players[i].set_ammo(3)
                                print("You entred the armory")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "T":
                                players[i].set_corr(telCorr[0], telCorr[1])
                                print("You entred the teleport")
                        else:
                            print("Player "+ str(i + 1) + " You wasted your turn")
                    elif command == "s":
                        if actualMaze[players[i]._x][players[i]._y]._cellType == "E":
                            if(commToExit == "s"):
                                return i
                        if actualMaze[players[i]._x][players[i]._y]._moveableD == 0:
                            players[i].set_corr(players[i]._x + 1,players[i]._y)
                            print("You moved 1 cell down")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "S":
                                players[i].set_stun(stunCount)
                                print("You are stunned for " + str(stunCount) + " turns")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "A":
                                players[i].set_ammo(3)
                                print("You entred the armory")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "T":
                                players[i].set_corr(telCorr[0], telCorr[1])
                                print("You entred the teleport")
                        else:
                            print("Player "+ str(i+1) + " You wasted your turn")
                        
                    elif command == "d":
                        if actualMaze[players[i]._x][players[i]._y]._cellType == "E":
                            if(commToExit == "d"):
                                return i
                        if actualMaze[players[i]._x][players[i]._y]._moveableR == 0:
                            players[i].set_corr(players[i]._x , players[i]._y + 1)
                            print("You moved 1 cell right")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "S":
                                players[i].set_stun(stunCount)
                                print("You are stunned for " + str(stunCount) + " turns")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "A":
                                players[i].set_ammo(3)
                                print("You entred the armory")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "T":
                                players[i].set_corr(telCorr[0], telCorr[1])
                                print("You entred the teleport")
                        else:
                            print("Player "+ str(i+1) + " You wasted your turn")
                    elif command == "a":
                        if actualMaze[players[i]._x][players[i]._y]._cellType == "E":
                            if(commToExit == "a"):
                                return i
                        if actualMaze[players[i]._x][players[i]._y]._moveableL == 0:
                            players[i].set_corr(players[i]._x , players[i]._y - 1)
                            print("You moved 1 cell left")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "S":
                                players[i].set_stun(stunCount)
                                print("You are stunned for " + str(stunCount) + " turns")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "A":
                                players[i].set_ammo(3)
                                print("You entred the armory")
                            if actualMaze[players[i]._x][players[i]._y]._cellType == "T":
                                players[i].set_corr(telCorr[0], telCorr[1])
                                print("You entred the teleport")
                        else:
                            print("Player "+ str(i + 1) + " You wasted your turn")
                    elif command == "backpack":
                        players[i].backpack_info()
                    elif command == "shoot w":
                        players[i].shootU(actualMaze, players)
                    elif command == "shoot d":
                        players[i].shootD(actualMaze, players)
                    elif command == "shoot d":
                        players[i].shootR(actualMaze, players)
                    elif command == "shoot a":
                        players[i].shootL(actualMaze,players)
                    elif command == "help":
                        players[i].helpIns()
                    else:
                        print("Enter a valid command")
            else:
                print("Player "+ str(i + 1) + " You wasted your turn")
                players[i]._canmove = players[i]._canmove - 1

                
def checkMaze(a,b,mymaze):
    
    
    canExitAny = 1;
    
    tpCorr = telCorr
    t = DFSwithTP(tpCorr, [a,b], mymaze)
    if t == 0:
        print([i,j])
        canExitAny = 0
    for i in range(a):
        for j in range(b):
            t = DFSwithoutTP([i, j], [a, b], mymaze)
            if t == 0:
                print([i, j])
                canExitAny = 0
    if (canExitAny == 1):
        print("OK")
    else:
        print("FAILED")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CodeReview')
    parser.add_argument('mode', type=int, nargs='?', default = 1)
    parser.add_argument('maze', type=str, nargs='?',default = "maze.txt")
    arg = parser.parse_args()
    if (arg.mode == 1):
        mymaze = OpenAndShowMaze(arg.maze)
        a = len(mymaze)
        b = len(mymaze[0])
        stunCount = 3
        commToExit = "w"
        telCorr = [0,0]
        checkMaze(a,b,mymaze)
    if (arg.mode == 2):
        print("Press 1 and enter a maze or 2 and enter the file of a maze")
        command2 = int(input())
        if (command2 == 1):
            print("Enter the maze size")
            mymaze = WriteMaze()
        elif (command2 == 2):
            mazePath = input()
            mymaze = OpenAndShowMaze(mazePath)
        a = len(mymaze)
        b = len(mymaze[0])

        print("Enter the number of players")
        playerCount = int(input())
        players = [Player() for i in range(playerCount)]
        for i in range(playerCount):
            print("Enter Player " + str(i+1) + " starting position")
            pXY = input().split()
            while int(pXY[0])>=a or int(pXY[1]) >= b or int(pXY[0]) < 0 or int(pXY[1]) < 0:
                print("Pls enter valid starting position")
                pXY = input().split()
            players[i].set_corr(int(pXY[0]),int(pXY[1]))
            players[i].set_start(int(pXY[0]),int(pXY[1]))


        stunCount = 3
        commToExit = "w"
        telCorr = [0,0]

        winner = play(mymaze,players)
        print("The winner is " + str(winner + 1))