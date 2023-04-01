'''
Leetcode: 17. Letter Combinations of a Phone Number
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/qVXG8l42yq0

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = '2'
Output: ['a','b','c']

Input: digits = '23'
Output: ['ad','ae','af','bd','be','bf','cd','ce','cf']

                  '23'
                  (2)
                /  |  \ 
               /   |   \ 
              /    |    \ 
             /     |     \ 
            /      |      \                
           /       |       \ 
          a        b        c
 (3)   / | \     / | \     / | \ 
      d  e  f   d  e  f   d  e  f

Process:
* Create a backtrack function that considers a digit as a starting point, map it to all its possible letters, and generate all possible combinations with that letter
* Base Case: if the length of the combination is the same as the input => we get an answer, add it to the results and backtrack.
'''

from typing import List

def backtrack(i, path, digits, letters, res):
    if len(path) == len(digits):
        res.append(path) #we have a complete combination (full path)
        return
    
    possible_letters = letters[digits[i]] #ex. 2 is mapped to letters 'abc'
    for curr_letter in possible_letters:
        backtrack(i + 1, path + curr_letter, digits, letters, res)


def letterCombinations(digits: str) -> List[str]:
    combinations = []
    digits_mapping = {
        '1': [''],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    if not digits: return []

    backtrack(0, '', digits, digits_mapping, combinations)
    return combinations


def main():
    digits_array = ['2', '23', '73', '426', '925', '2345']
    counter = 1
    for digits in digits_array:
        print(counter, '.\t All letter combinations for "', digits, '": ')
        print('\t',letterCombinations(digits))
        counter += 1
        print('-' * 100)

main()

'''
TC -> O(4^n*n) time, where n is the number of input digits. The worst case is to have digits of number 9, we know that 9 is mapped to 4 letters, so at most we gonns have 4 choices for each digit (4 will represent the maximum number of letters with any giving digit in our mapping) => Generating the letter combinations takes O(n*4^n) time since there are 4^n possible combinations for every digit.
SC -> O(4*n) where n is the total number of input digits, and 4 is the maximum number of letters mapped to any digit. 
Our recursive solution takes up space on the call stack, with n being the maximum depth of the stack, corresponding to the number of input digits. At each level in the stack, a list of up to k letters is maintained. Therefore, the space complexity is O(4n)
'''