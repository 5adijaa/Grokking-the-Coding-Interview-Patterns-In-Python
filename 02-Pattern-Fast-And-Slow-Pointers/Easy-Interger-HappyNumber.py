'''
Leetcode: 202. Happy Number
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/qZnwmQO8ADp 

Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not

Input: n = 19
Output: True
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Input n = 2
Explanation: 
2^2=4 -> 4^2=16 -> 1^2+6^2=37 -> 3^2+0^2=9 -> 9^2=81 -> 8^2+5*2=65 -> 6^2+5^2=61 ->6^2+1= 
                           ⬆___________________infinite loop___________________________⬆
Output: False
'''

# Fast and Slow pointers Approach
#  -> TC: Since there were two pointers: the cost is O(logn+logn), that is: O(logn)
#  -> SC: O(1) as we don't need any extra space
def HappyNumber(n: int) -> bool:
    slow = n
    fast = squared_sum(n)

    if slow == 1: return True #base case where n=1

    while slow != fast:
        slow = squared_sum(slow) # move slow one step forward 
        fast = squared_sum(squared_sum(fast)) # move fast two steps forward.

        if fast == 1:
            return True
    
    return False

    
def squared_sum(n: int) -> int:
    total = 0
    while n:
        digit = n % 10
        total += digit**2
        n = n // 10
    return total

'''
# brute force approach: Hash set
# We repeatedly calculate the squared sum of digits of the input number and store it in a hash set. and check if the sum is already exist in the set -> if yes, we detected a cycle # => return false. If our sum converges to 1, we've found a happy number
# -> TC: O(logn) since we loop through a set of squared numbers 
# -> SC: O(n) since we're using additional space to store our calculated sums.
def HappyNumber(n: int) -> bool:
    visited = set()

    while n not in visited:
        visited.add(n)
        n = squared_sum(n)

        if n == 1 :
            return True
    
    return False
'''


print(HappyNumber(19)) #True
print(HappyNumber(2)) #False
print(HappyNumber(1)) #True
print(HappyNumber(7)) #True
print(HappyNumber(8)) #False
print(HappyNumber(2147483646)) #False