'''
Leetcode: 37. Sudoku Solver (logic-based puzzle)
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/N8WvOqpoKk2 (Challenge Problem)

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example:
Input: 
board = [['5','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],['.','.','.','.','8','.','.','7','9']]
Output: 
[['5','3','4','6','7','8','9','1','2'],['6','7','2','1','9','5','3','4','8'],['1','9','8','3','4','2','5','6','7'],['8','5','9','7','6','1','4','2','3'],['4','2','6','8','5','3','7','9','1'],['7','1','3','9','2','4','8','5','6'],['9','6','1','5','3','7','2','8','4'],['2','8','7','4','1','9','6','3','5'],['3','4','5','2','8','6','1','7','9']]


Look for the empty cells: The first step is to look for the empty cells (i.e., cells with a value of 0) in the Sudoku grid.
Pick a cell: Once you have found an empty cell, pick that cell and start by guessing a number between 1 and 9 that could potentially fit into that cell.
Check for validity: Check if the number you have guessed is valid for that particular cell by making sure that it is not already present in the same row, same column, or same 3x3 sub-grid.
If valid, update the cell with the number and move on to the next empty cell.
If not valid, go back to the previous cell and try a different number.
Repeat until the entire grid is filled: Keep repeating steps 2-5 until the entire grid is filled with numbers that satisfy the Sudoku rules.
'''
from typing import List


def solveSudoku(board: List[List[str]]) -> None:
    '''
    Do not return anything, modify board in-place instead.
    '''
    DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9' ]
        
    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': #Find the empty cell
                    for num in DIGITS: #Try numbers 1-9 at this cell
                        if is_valid(r, c, num): #check if num is never seen in curr row, col, box
                            board[r][c] = str(num)
                            if backtrack(): #Move on to the next cell
                                return True
                            board[r][c] = '.' #backtrack the cell
                    
                    return False
        
        return True
    
    def is_valid(r, c, num): #Check if a number 'num' is valid at a given position
        #Check if num already exists in the row or column
        for i in range(9):
            if board[i][c] == num or board[r][i] == num: 
                return False
            
        #Check if num already exists in the 3x3 box
        box_r = (r//3)*3
        box_c = (c//3)*3
        for i in range(box_r, box_r+3):
            for j in range(box_c, box_c+3):
                if board[i][j] == num:
                    return False
        
        return True #num is valid

    backtrack()
    return board

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def main():
    input_board = [
        ['5','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9']
    ]
    print('The initial Board is: \n')
    print_board(input_board)

    board = solveSudoku(input_board)
    print('\nsudoko Solver: \n')
    print_board(board)

main()

'''
TC -> O(9^(nn)), where n is the size of the board (in this case, n=9). This is because for each empty cell, we try out 9 possible numbers, and in the worst case, there are nn empty cells in total
SC -> O(1) because the board is modified in place and no additional data structures are created.
'''