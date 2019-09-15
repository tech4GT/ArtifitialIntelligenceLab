import queue as queue


# a is the initial state of the board and b is the final staate of the board
# Empty spot is represented by 0
a = [[1, 2, 3],
       [5, 6, 0],
       [7, 8, 4]]

b = [[1,2,3],
        [5,8,6],
        [0,7,4]]

class Node:
    def __init__(self, board, parent):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.board[i][j] = board[i][j]
        self.parent = parent

def matchBoard(o1,o2):

    if len(o1) != len(o2) or len(o1[0]) != len(o2[0]):
        return False

    for i in range(len(o1)):
        for j in range(len(o1[i])):
            if(o1[i][j] != o2[i][j]):
                return False
    return True

def serielizeBoard(board):
    rv = ""
    for arr in board:
        for el in arr:
            rv = rv + str(el) + " "
        rv = rv + "\n"

    return rv

def findEmptySlot(board):
    xPos = -1
    yPos = -1
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == 0:
                xPos = i
                yPos = j
    return [xPos,yPos]

def swap(board, x1, y1, x2, y2):
    temp = board[x1][y1]
    board[x1][y1] = board[x2][y2]
    board[x2][y2] = temp

q = queue.Queue(maxsize=-1)
visited = {}

q.put(Node(a,None))
n = False
while(not q.empty()):
    n = q.get()
    if visited.__contains__(serielizeBoard(n.board)):
        continue
    visited[serielizeBoard(n.board)] = True
    if matchBoard(n.board,b):
        break

    pos = findEmptySlot(n.board)
    if pos[0] > 0:
        swap(n.board,pos[0],pos[1],pos[0]-1,pos[1])
        q.put(Node(n.board,n))
        swap(n.board,pos[0],pos[1],pos[0]-1,pos[1])
    if pos[1] > 0:
        swap(n.board,pos[0],pos[1],pos[0],pos[1]-1)
        q.put(Node(n.board,n))
        swap(n.board,pos[0],pos[1],pos[0],pos[1]-1)
    if pos[0] < 2:
        swap(n.board,pos[0],pos[1],pos[0]+1,pos[1])
        q.put(Node(n.board,n))
        swap(n.board,pos[0],pos[1],pos[0]+1,pos[1])
    if pos[1] < 2:
        swap(n.board,pos[0],pos[1],pos[0],pos[1]+1)
        q.put(Node(n.board,n))
        swap(n.board,pos[0],pos[1],pos[0],pos[1]+1)


if not matchBoard(n.board,b):
    print("Not Possible!")
else:
    stack = queue.LifoQueue(maxsize=-1)
    while n != None:
        stack.put(n)
        n = n.parent
    while stack.qsize() != 0:
        n = stack.get()
        print(serielizeBoard(n.board))
        print("\n")