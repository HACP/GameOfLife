# create/read board
# validate board is correct
# define function update board
#   input board
#   output updated board
#   for cells in board:
#       apply conditions 1-3 to live cells
#       apply condition 4 to dead cells

import numpy as np

def createBoard(m,n,random_state=2022):
    """
    creates board of given dimensions (m,n) with random entries of 0,1
    improvement -  add probability of drawing 1 or 0

    input: size of board, tuple (m,n)
    output: numpy array
    """

    board = np.random.randint(0,2,(m,n))
    return(board)


def findNeighbors(board_shape, i,j):
    """
    finds neighbors of a given cell (i,j)

    cases:
        - boundary
        - inner part

    input: cell coordiates (i,j)
    output: array of coordiates of adjacent neighboors
    """

    (m,n) = board_shape

    lNeighborsInner = [[(i-1) ,(j+1)  ],[(i+0) ,(j+1)  ],[(i+1) ,(j+1)  ],
                       [(i-1) ,(j+0)  ],[(i+0) ,(j+0)  ],[(i+1) ,(j+0)  ],
                       [(i-1) ,(j-1)  ],[(i+0) ,(j-1)  ],[(i+1) ,(j-1)  ]]
    lNeighbors = lNeighborsInner

    if 0 < i < m and 0 < j < n:
        return(sorted(lNeighborsInner))
    else:
        lNeighborsBorder = []
        for item in lNeighborsInner:
            if (item[0]>=0) and (item[1] >= 0) and (item[0]<=m) and (item[1]<=n):
                lNeighborsBorder.append(item)
        return(sorted(lNeighborsBorder))

def findLiveNeighbors(board,i,j):
    """
    Finds the number of live neighboors as a sum of the elements in the board
    """
    lNeighbors = findNeighbors(board.shape, i,j)
    print(lNeighbors)
    return(sum([board[item[0]][item[1]] for item in lNeighbors])) - board[i][j]

def update_rule1(board,i,j):
    """
    Implements rule 1: underpopulation
    """
    if board[i][j] == 1 and findLiveNeighbors(board,i,j)<2:
        board[i][j] = 0

def update_rule2(board,i,j):
    """
    Implements rule 2
    """
    if board[i][j] == 1 and 2 < = findLiveNeighbors(board,i,j)<=3:
        board[i][j] = 1

def update_rule3(board,i,j):
    """
    Implements rule 3: overpopulation
    """
    if board[i][j] == 1 and findLiveNeighbors(board,i,j)>3:
        board[i][j] = 0

def update_rule4(board,i,j):
    """
    Implements rule 4
    """
    if board[i][j] == 0 and findLiveNeighbors(board,i,j)==3:
        board[i][j] = 1

def update_board(board):
    for ii in range(board.shape[0]):
        for jj in range(boars.range[1]):
            update_rule1(board,ii,jj)
            update_rule2(board,ii,jj)
            update_rule3(board,ii,jj)
            update_rule4(board,ii,jj)
    return(board)
