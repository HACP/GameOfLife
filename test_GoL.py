from src.GoL import *
import pytest
import numpy as np

def test_board_entries():
    """
    Checking that all the entries in the board are (0, 1) integers
    """
    # fail example with fractions
    board_with_fractions = np.array([[0.5,1],[0,0]])
    #board = board_with_fractions

    # fail example with elements different from 0,1
    board_with_integers_diff_01 = np.array([[-1,0],[2,1]])
    #board = board_with_integers_diff_01

    # if np.min(board) = np.max(board) then we have the board completely filled with 0s or 1s
    # and it won't be a good state - confirm

    board = createBoard(2,3)
    assert (board.astype(int) == board).all() & (np.max(board)==1) & (np.min(board)==0)

def test_cell_neighbors_inner():
    """
    Checking if findNeighbors returns right neighbors for inner cells

    if m = 5, n = 5 and i = 2, j = 2 (inner section) then
        lNeighbors =   [[1,3],[2,3],[3,3],
                        [1,2],[2,2],[3,2],
                        [1,1],[2,1],[3,1]]
        ]

    """
    lNeighborsTest =   [[1,3],[2,3],[3,3],
                        [1,2],[2,2],[3,2],
                        [1,1],[2,1],[3,1]]

    assert (findNeighbors((5,5),2,2) == sorted(lNeighborsTest))

def test_cell_neighbors_corners():
    """
    Checking if findNeighbors returns right neighbors for boundary cells
    a. corner
    if m = 5, n = 5 and i = 0, j = 0 (inner section) then
        lNeighbors =   [      [0,1],[1,1],
                              [0,0],[1,0]

                        ]

    """
    lNeighborsTest1 =  sorted([[0,1],[1,1],[0,0],[1,0]])
    lNeighborsTest2 =  sorted([[0,5],[1,5],[0,4],[1,4]])
    lNeighborsTest3 =  sorted([[4,5],[5,5],[4,4],[5,4]])
    lNeighborsTest4 =  sorted([[5,1],[4,1],[5,0],[4,0]])



    assert (findNeighbors((5,5),0,0) == lNeighborsTest1) and (findNeighbors((5,5),0,5) == lNeighborsTest2) and (findNeighbors((5,5),5,5) == lNeighborsTest3) and (findNeighbors((5,5),5,0) == lNeighborsTest4)

def test_cell_neighbors_live():
    """
    Checking if the count of neighbors is correct
    """
    test_board = np.array([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
    assert (findLiveNeighbors(test_board,0,0) == 1) and (findLiveNeighbors(test_board,2,1) == 3)
