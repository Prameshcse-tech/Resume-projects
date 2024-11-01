from Board import *

def solve(bo):
    find = find_empty(bo)
    #Base case
    if not find:
        return True
    else:
        row ,column = find
    #recursive Case

    for i in range(1,10):
        if valid(bo, i, (row, column)):
            bo[row][column]=i
            if solve(bo):
                return True
            bo[row][column]=0

    return False

def print_board(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("\n- - - - - - - - - - -")
        else:
            print()
        for j in range(len(bo)):
            if j%3==0 and j!=0:
                print("| ",end="")
            print(bo[i][j], end=" ")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j]==0:
                return (i,j) #row,column

    return None


def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1]!=i:
            return False
    #check Column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0]!=i:
            return False
    #check Box
    box_x=pos[1]//3
    box_y=pos[0]//3 #box co-ordinates
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo[i][j]==num and (i, j)!=pos:
                return False

    return True

print_board(Bo)
print("\n\n")
solve(Bo)
print_board(Bo)