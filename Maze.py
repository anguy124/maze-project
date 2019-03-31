#An Nguyen
#Maze Project
#For my maze, my basic operations are the comparisons made for checking left, right, up, and down, checking to see if the point
#following it is a '*'. Written in my search function, it will count each time it will run and check the if statements for left, right, up, and down
#and add it towards the counter, which is the total number of moves.
import time
import os


def main():

    print(os.listdir("mazes/"))

    filename = "mazes/"
    filename += input("Please enter in maze: ")
    fileContents = open(filename,"r")
    #for line in fileContents:
        #print(line)
    maze = []
    start = ()
    end = ()
    xcoord = 0
    ycoord = 0
    for i in fileContents.readlines():
        x = ""
        array = []
        for j in i:
            if j!= "\n":
                array.append(j)
            if j == "s":
                #this is the start of the maze
                start = (xcoord,ycoord)
            if j == "e":
                #this is the end of the maze
                end = (xcoord,ycoord)
            ycoord+=1
        xcoord+=1
        maze.append(array)
        ycoord = 0 #reset y

    #print(start)
    #print(end)
    printMaze(maze)

    startTime = time.time()
    counter = search(maze, start, end)
    endTime = time.time()
    lengthOfTime = endTime - startTime
    print("The game took: ",lengthOfTime, "seconds")
    print("Total moves: ",counter)

    main()

def printMaze(maze):
    for line in maze:
        print(line)


def search(maze,start,end):
    #start at s
    #look at coordinates left, right, above, & below
    #what's running through the maze from start to end

    # deque mouse queue

    mouse = []
    mouse.append(start)


    left = (start[0],start[1]-1)
    right = (start[0],start[1]+1)
    up = (start[0]-1, start[1])
    down = (start[0]+1, start[1])


    #will be a while loop later on when you run out of moves
    #while mouse is still moving or has not reached the end

    counter = 0
    while mouse!= []:
        previousLocation = mouse[0]

    #this is the mouse that is moving
        maze[mouse[0][0]][mouse[0][1]] = '@'
    #need to reset the location prior to the append(left/right/up/down)
        # update left right up down using previous location
        left = (previousLocation[0],previousLocation[1]-1)
        right = (previousLocation[0],previousLocation[1]+1)
        up = (previousLocation[0]-1, previousLocation[1])
        down = (previousLocation[0]+1, previousLocation[1])

#for intersections: you "split off" meaning you check the point to the right
        #and you check the point beneath

        mouse = mouse[1:]
        if maze[left[0]][left[1]] != '*':
            print("Can move left")
            mouse.append(left)
            # change mouse's previous location on maze into a wall (*)
            maze[previousLocation[0]][previousLocation[1]] = '*'
        if maze[right[0]][right[1]] != '*':
            print("Can move right")
            mouse.append(right)
            maze[previousLocation[0]][previousLocation[1]] = '*'

        if maze[up[0]][up[1]] != '*':
            print("Can move up")
            mouse.append(up)
            maze[previousLocation[0]][previousLocation[1]] = '*'
        if maze[down[0]][down[1]] != '*':
            print("Can move down")
            mouse.append(down)
            maze[previousLocation[0]][previousLocation[1]] = '*'

        counter+=1

        if previousLocation == end:
            print("Game finished!")
            return counter
        print(mouse)
        printMaze(maze)
    return counter



#breadth first search
#intersection: when the location of the mouse and the points left, right, above, or down are '.'
#psuedo code for reference
'''
makes a list for locations  # what the location the mouse will travel (x,y)
def breadthfirstsearch(maze,mouse):
    visited, queue = list(), [mouse] #list of points (,) added to queue
    while it is in queue:
        remove previous point
        if vertex not in visited:
            visited.add(vertex)     #if visited already
    return visited'''

main()