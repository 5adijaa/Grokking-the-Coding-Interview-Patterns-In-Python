'''
Leetcode: 881. Boats to Save People
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/7DJgZ304O1y

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
'''
from typing import List


def numRescueBoats(people: List[int], limit: int) -> int:    
    people.sort()
    count_boats = 0

    l, r = 0, len(people)-1
    while l <= r:
        #Instead of picking 2 smaller or 2 larger weights first. We'll pick the mix of two
        weight = people[r] + people[l] 
        if weight <= limit:
            l += 1
            r -= 1
            count_boats += 1
        else:
            r -= 1
            count_boats += 1
    
    return count_boats 

def main():
    people = [[1, 2], [3, 2, 2, 1], [3, 5, 3, 4], [5, 5, 5, 5], [1, 2, 3, 4], [1, 2, 3, 4, 5], [3, 4, 5]]
    limit = [3, 3, 5, 5, 5, 3, 1]
    for i in range(len(people)):
        print(i + 1, '\tWeights =', people[i])
        print('\tWeight Limit =', limit[i])
        print('\tThe minimum number of boats required to save all people are',
              numRescueBoats(people[i], limit[i]))
        print('-' * 100)


if __name__ == '__main__':
    main()

'''
TC-> O(nLogn+n) where n is the length of the list. O(nlogn) for sorting the list, and O(n) for looping over the list
SC-> O(n) space to sort the list 
'''