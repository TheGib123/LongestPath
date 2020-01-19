class Place():
    def __init__(self, row, col):
        self.row = row
        self.col = col
'''
matrix = [
    [0,0,0,1,0,0,0,1,1],    
    [0,0,0,1,0,0,0,0,1],
    [0,1,1,1,1,1,1,1,1],
    [0,1,0,0,0,0,0,1,0],
    [0,1,0,1,1,0,0,1,0],
    [1,1,0,0,1,1,1,1,0],
    #[0,0,0,0,0,0],
]
'''
'''
matrix = [
    [1,1,1,1,1],    
    [0,1,0,0,0],
    [0,1,0,1,1],
    [0,1,0,0,1],
    [0,1,0,0,1],
    [0,1,1,1,1]
]
'''
matrix = [
[0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,1,1,1],
[0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1],
[1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,0,1,0,1],
[0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1],
[0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1],
[0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0],
[0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0],
[1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
[1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0],
[1,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0],
[1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0],
[1,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0],
[1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
[1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
[0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,1,1,1],
[0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0]  
]

maxList = []
temp = []

# finds all ones in matrix and stores the row and col in a list
def FindAllOnes():
    onesList = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (matrix[row][col] == 1):
                x = Place(row,col)
                onesList.append(x)
    return onesList

# the recursion loop
def Recur(row,col):
    global temp
    if (col >= 0 and row >= 0):
        x = Place(row,col)
        temp.append(x)
        maxList.append(temp.copy())
    else:
        return

    matrix[row][col] = 2

    try:
        right = matrix[row][col + 1]
        if (right == 1):
            Recur(row,col+1)
    except:
        pass
    try:
        left = matrix[row][col - 1]
        if (left == 1):
            Recur(row,col-1)
    except:
        pass

    try:
        down = matrix[row+1][col]
        if (down == 1):
            Recur(row+1,col)
    except:
        pass

    try:
        up = matrix[row-1][col]
        if (up == 1):
            Recur(row-1,col)
    except:
        pass

    temp = temp[:len(temp)-1]
    matrix[row][col] = 1

# changes the longest path to 2's 
def ShowLongestPath():
    longest = 0
    for i in range(len(maxList)):
        if (len(maxList[i]) > len(maxList[longest])):
            longest = i
    if (len(maxList) != 0):
        for i in range(len(maxList[longest])):
            matrix[maxList[longest][i].row][maxList[longest][i].col] = 2

# prints the matrix to the terminal neatly
def PrintMatrix():
    print('*********************************************')
    for row in range(len(matrix)):
        x = '* '
        for col in range(len(matrix[0])):
            if (matrix[row][col] == 2):
                x = x + 'x '
            elif (matrix[row][col] == 1):
                x = x + '1 '
            else:
                x = x + '  '
        x = x + ' *'
        print(x)
    print('*********************************************')

# starting 
def start():
    PrintMatrix()
    ones = FindAllOnes()

    for i in ones:
        global temp
        temp = []
        Recur(i.row,i.col)
    
    ShowLongestPath()
    PrintMatrix()
    
start()

