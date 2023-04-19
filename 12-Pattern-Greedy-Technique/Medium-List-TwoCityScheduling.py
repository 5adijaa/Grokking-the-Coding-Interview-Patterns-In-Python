'''
Leetcode 1029. Two City Scheduling
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/JPEkVEL1XgD

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Example 1:
Input: costs = [[10,20], [30,200], [400,50], [30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Example 2:
Input: costs = [[259,770], [448,54], [926,667], [184,139], [840,118], [577,469]]
Output: 1859
'''

from typing import List


def twoCitySchedCost(costs: List[List[int]]) -> int:
    # Calculate the difference cost between B and A cities 
    # Sort, Then send n//2 to city B and next n//2 to city A

    n = len(costs)
    min_cost = 0
    diff_costs = []

    for A, B in costs:
        diff_costs.append([B - A, B, A])
    
    diff_costs.sort()
    for i in range(n):
        if i < (n//2):
            min_cost += diff_costs[i][1] #send them to city B
        else:
            min_cost += diff_costs[i][2] #send them to city A
    
    return min_cost


def main():
    input_costs = [
        [[10, 20], [30, 200], [400, 50], [30, 20]],
        [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]],
        [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]],
        [[1, 2], [3, 4], [5, 6], [7, 8], [9, 6], [5, 8]],
        [[1, 2], [1, 2], [1, 2], [1, 2]]
    ]
            
    for i in range(len(input_costs)):
        print('Test Case #', i + 1)
        print('\nThe minimum cost to send people equally into City A and B when the costs are ', input_costs[i], ' is:', twoCitySchedCost(input_costs[i]))
        print('-' * 140)


if __name__ == '__main__':
    main()

'''
TC -> O(nlogn) because we need to sort the diff_costs
SC -> O(n+m) where n represents the number of elements we added into our difference array, and m represents the memory required to sort this array. Python uses a combination of merge sort and insertion sort which can sort the array in O(m) but this can differ for other languages like Java or C++
'''