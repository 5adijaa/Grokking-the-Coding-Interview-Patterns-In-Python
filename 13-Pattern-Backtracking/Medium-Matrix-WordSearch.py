'''
Leetcode: 79. Word Search
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/7nQKMDRRv8G

Given an mxn grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCCED'
Output: true

Example 2:
Input: board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCB'
Output: false
'''

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    ROWS = len(board)
    COLS = len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True

        if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i]:
            return False
        
        tmp, board[r][c] = board[r][c], '#'

        for _r, _c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if dfs(_r, _c, i+1):
                return True
        
        board[r][c] = tmp

        return False


    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0): return True
    
    return False


def main():
    input = [
        ([['A', 'B', 'C', 'E'],
          ['S', 'F', 'C', 'S'],
          ['A', 'D', 'E', 'E']], 'ABCCED'),

        ([['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']], 'ABCB'),

        ([['E', 'D', 'X', 'I', 'W'],
        ['P', 'U', 'F', 'M', 'Q'],
        ['I', 'C', 'Q', 'R', 'F'],
        ['M', 'A', 'L', 'C', 'A'],
        ['J', 'T', 'I', 'V', 'E']], 'educative'),

        ([['O', 'Y', 'O', 'I'],
        ['B', 'I', 'E', 'M'],
        ['K', 'D', 'Y', 'R'],
        ['M', 'T', 'W', 'I'],
        ['Z', 'I', 'T', 'O']], 'DYNAMIC'),

        ([['h', 'e', 'c', 'm', 'l'],
        ['w', 'l', 'i', 'e', 'u'],
        ['a', 'r', 'r', 's', 'n'],
        ['s', 'i', 'i', 'o', 'r']], 'WARRIOR'),

        ([['C', 'Q', 'N', 'A'],
        ['P', 'S', 'E', 'I'],
        ['Z', 'A', 'P', 'E'],
        ['J', 'V', 'T', 'K']], 'save'),

        ([['A']], 'ABC'),

        ([['P', 'S', 'S', 'I', 'W', 'P'],
        ['P', 'Y', 'C', 'A', 'Q', 'T'],
        ['I', 'S', 'H', 'P', 'F', 'Y'],
        ['M', 'T', 'O', 'L', 'O', 'I'],
        ['J', 'I', 'N', 'O', 'G', 'K'],
        ['I', 'M', 'D', 'T', 'Y', 'T']], 'PSYCHOLOGY')
    ]
    num = 1

    for i in input:
        print(num, '.\tBoard =', sep='')
        for j in range(len(i[0])):
            print('\t\t', i[0][j])
        if i[1] == '':
            print('\n\tWord = ''')
        else:
            print(f'\n\tWord =  {i[1]}')
        search_result = exist(i[0], i[1])
        if search_result:
            print('\n\tSearch result = Word found')
        else:
            print('\n\tSearch result = Word could not be found')
        num += 1
        print('-'*100, '\n')


if __name__ == '__main__':
    main()

'''
TC -> O(MNx3^W), where M is number of rows, N is number of columns, and W length of the word being surched for. This is because for each cell in the board, the function performs a depth-first-search with up to 3 recursive calls (one for each neighbor, except for the one we just came from: we don't revisit the visited cell). And the search continues until either the word is found or all possible paths have been explored.

SC -> O(W), where W is the length of the word to be searched. This is because we only need to store the index of the current character of the word during the depth-first search, which takes up constant space. We are not using any additional data structures, so the space complexity is O(W).
'''