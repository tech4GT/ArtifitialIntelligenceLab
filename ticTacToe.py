

# Print Board positions
print("1 2 3\n4 5 6\n7 8 9")

O = {}
X = {}

winCombos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
def checkBoard():
    for combo in winCombos:
        if O.__contains__(combo[0]) and O.__contains__(combo[1]) and O.__contains__(combo[2]):
            print(combo)
            return "<O wins>"
        if X.__contains__(combo[0]) and X.__contains__(combo[1]) and X.__contains__(combo[2]):
            print(combo)
            return "<X wins>"
    if len(O)+len(X) == 9:
        return "draw"
    return None

def printBoard():
    print()
    for i in range(3):
        for j in range(3):
            loc = 3*i + j + 1
            if O.__contains__(loc):
                print("O",end='')
            elif X.__contains__(loc):
                print("X",end='')
            else:
                print("_",end='')
        print()

result=None
turn="O"
while(True):
    loc = int(input("\nPlease Enter the position for " + turn + "\n"))

    if O.__contains__(loc) or X.__contains__(loc):
        print("Invalid Move\n")
        continue

    col = None
    if turn == "O":
        col = O
        turn = "X"
    else:
        col = X
        turn = "O"

    col[loc] = True
    result = checkBoard()
    if(result != None):
        break
    printBoard()

print("The result of the game is " + result)

