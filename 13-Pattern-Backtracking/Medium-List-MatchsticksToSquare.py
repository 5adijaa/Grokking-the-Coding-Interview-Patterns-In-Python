'''
Leetcode: 473. Matchsticks to Square
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/mEn2Xwv6490 (Challenge Problem)

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
'''
from typing import List


def makeSquare(matchsticks: List[int]) -> bool:
    if len(matchsticks) < 4: #Check if the number of matchsticks is less than 4
            return False
        
    total = sum(matchsticks)
    length = total // 4 #The length of one side (we know that perimeter of square=a*4)
    sides = [0]*4 #To track the 4 sides of the square that we gonna build in each comb
    
    if total < 4: #Check If the sum of all values is less than 4
        return False
    
    if total % 4 != 0: #Check if the sum of all values is not a multiple of 4
        return False
    
    matchsticks.sort(reverse=True) #Useful to check the longer matchsticks first
    def dfs(index):
        if index == len(matchsticks):
            return True
        
        for i in range(4):
            if sides[i] + matchsticks[index] <= length:
                sides[i] += matchsticks[index]
                if dfs(index+1):
                    return True
                sides[i] -= matchsticks[index] #backtrack
        
        return False
    
    return dfs(0)


def main():
    matchsticks = [
        [1,1,2,2,2],
        [3,3,3,3,4],
        [1,1,1,2,1],
        [3,4,4,1,2,2],
        [5,6,1,1,2,2]
    ]

    for i in range(len(matchsticks)):
        print(i + 1, '.\t Input Matchsticks:', matchsticks[i])
        print('\t Can we form a square? ->', makeSquare(matchsticks[i]))
        print('-' * 80)


if __name__ == '__main__':
    main()

'''
TC -> O(4^n) where n is the number of matchsticks. This is because for each matchstick, we have 4 choices of which side to add it to. We have four choices to either add the current matchstick to one of the four sides of the square or not. This makes the number of recursive calls 4^N.
SC -> O(n) which is the space used by the recursion stack. This is because we are only keeping track of the matchsticks used in each recursive call, which is proportional to the height of the recursion tree, and the height of the recursion tree is proportional to the number of matchsticks used.
'''