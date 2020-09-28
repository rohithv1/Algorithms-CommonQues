# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:30:33 2020

@author: Rohith_Vemulapally
"""

import numpy as np

sudoku = [[0,0,0,2,6,0,7,0,1],
          [6,8,0,0,7,0,0,9,0],
          [1,9,0,0,0,4,5,0,0],
          [8,2,0,1,0,0,0,4,0],
          [0,0,4,6,0,2,9,0,0],
          [0,5,0,0,0,3,0,2,8],
          [0,0,9,3,0,0,0,7,4],
          [0,4,0,0,5,0,0,3,6],
          [7,0,3,0,1,8,0,0,0]]

#print(np.matrix(sudoku))

def possible(x,y,n):
    global sudoku
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    for i in range(9):
        if sudoku[x][i] == n:
            return False
    
    X, Y = 3 *(x//3), 3*(y//3)
    
    for i in range(X, X+3):
        for j in range(Y, Y+3):
            if sudoku[i][j] == n:
                return False
    
    return True

def solve_sudoku():
    global sudoku
    
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                for n in range(1,10):
                    if possible(x,y,n):
                        sudoku[x][y] = n
                        solve_sudoku()
                        sudoku[x][y] = 0
                return
    print(np.matrix(sudoku))
    
solve_sudoku()
        