'''
Leetcode: 51. N-Queens
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/g7qQw2kqN6D

The n-queens puzzle is the problem of placing n queens on an nxn chessboard such that no two queens attack each other.
(A queen can move horizontally, vertically, and diagonally on a chessboard. One queen can be attacked by another queen if both share the same row, column, or diagonal.)

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [['.Q..','...Q','Q...','..Q.'],['..Q.','Q...','...Q','.Q..']]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [['Q']]
'''
from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    board = [['.' for _ in range(n)] for _ in range(n)]
    result = []

    cols = set() #make sure that no queen has been set at same column
    diagonals = set() #make sure, there is no queen at same positive diagonal (row+col)
    anti_diagonals = set() ##make sure, there is no queen at same anti diagonal (row-col)

    def backtrack(row): #DFS
        if row == n:
            copy = [''.join(row) for row in board] #make a copy b/c we're still using the board in next calls
            result.append(copy)
            return
        
        for col in range(n):
            if col in cols or row + col in diagonals or row - col in anti_diagonals:
                continue

            cols.add(col)
            diagonals.add(row + col)
            anti_diagonals.add(row - col)
            board[row][col] = 'Q' #Place a queen in the curr cell

            backtrack(row+1) #Move to the next row and try to place a queen

            cols.remove(col)
            diagonals.remove(row + col)
            anti_diagonals.remove(row - col)
            board[row][col] = '.' #Backtrack by removing the queen from curr cell
        
    backtrack(0)

    return result


def main():
    n = [1, 4, 5]
    for i in range(len(n)):
        print(i+1, '. Queens = ', n[i], ', Chessboard: (', n[i], 'x', n[i], ')', sep='')
        res = solveNQueens(n[i])
        print('\nAll distinct solutions to the', n[i], '- queens puzzle on a (', n[i], 'x', n[i], ') chessboard are: \n', res)
        print('-'*150, '\n')


if __name__ == '__main__':
    main()

'''
TC -> O(n!), since there are n choices for the first row, n-2 choices for the second row (since it can't share the same col or diagonal with the first), n-4 choices for the third row (since it can't share the same col or diagonal with the first two) and so on. This results in a TC of n*(n-2)(n-4)...*1 = n!!(double factorial) = O(n!) in the worst case.

SC -> O(n^2) because we use a 2D board of size n x n to represent the board. Additionally, we use a list 'result' to store the solutions, which can contain up to n! solutions. However, we can ignore the size of the solution list since it is part of the output and not part of the algorithm's space complexity
'''