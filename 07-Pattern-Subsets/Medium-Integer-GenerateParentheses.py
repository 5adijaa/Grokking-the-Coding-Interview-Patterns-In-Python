'''
Leetcode: 22. Generate Parentheses
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/qV7VDZRMPDp

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 1
Output: ['()']

Input: n = 3
Output: ['((()))','(()())','(())()','()(())','()()()']

                            ['(']
            ['(']                       [')']
    ['(']          [')']                ['(']       
    [')']       ['(']   [')']       ['(']    [')']
    [')']       [')']   ['(']       [')']    ['(']
    [')']       [')']   [')']       [')']    [')']

Instructions:
We start with an open parentesis, we have 2 choices: Add an open or a closed parenthesis:
-> we only add an open '(' if open parenthesis is less than n
-> we only add a closing ')' id closing parenthesis is less than open parenthesis
-> Base case will be at: open = closing = n
Solution:
The key observation in constructing the solution is to keep track of the number of opening '(' and closing ')' parentheses.
'''

from typing import List

def backtrack(n, opening, closing, stack, res):
    if opening == closing == n :
        s = ''.join(stack)
        res.append(s)
        return
    
    if opening < n:
        stack.append('(')
        backtrack(n, opening + 1, closing, stack, res)
        stack.pop()
    
    if closing < opening:
        stack.append(')')
        backtrack(n, opening, closing + 1, stack, res)
        stack.pop()


def generateParenthesis(n: int) -> List[str]:
    parentheses = []
    backtrack(n, 0, 0, [], parentheses)
    return parentheses


def main():
    n = [1, 2, 3, 4, 5]
    for i in range(len(n)):
        print(i + 1, '.\t n = ', n[i], sep='')
        print('\t All combinations of valid balanced parentheses are: ')

        result = generateParenthesis(n[i])
        # print(result)
        for rs in result:
            print('\t\t ', rs)

        print('-' * 100)

main()

'''
TC -> Our tree has a branching of 2: because we only add an opening or a closing brace at each step. And there is a maximum depth of 2n because the length of the output is the sum of n opening and n closing parentheses. => This leads us to a time complexity O(2^(2n)) ~ O(4^n)
SC -> We used a stack of 2n length => The space complixity is linear O(n)
'''