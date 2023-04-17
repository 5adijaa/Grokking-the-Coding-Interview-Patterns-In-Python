'''
Leetcode: 134. Gas Station
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/7Do6kWMqDLr

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
'''
from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    gas_in_tank = 0
    start_index = 0

    for i in range(len(gas)):
        gas_in_tank += gas[i] - cost[i]

        if gas_in_tank < 0: #Means, we cannot complete a loop form this starting index, 
            gas_in_tank = 0 #So, we reset the total gas in tank
            start_index = i+1 #And we increment the starting index by 1.
    
    return start_index


def main():
    gas = [[1, 2, 3, 4, 5], [2, 3, 4], [1, 1, 1, 1, 1], [1, 1, 1, 1, 10], [1, 1, 1, 1, 1], [1, 2, 3, 4, 5]]
    cost = [[3, 4, 5, 1, 2], [3, 4, 3], [1, 2, 3, 4, 5], [2, 2, 1, 3, 1], [1, 0, 1, 2, 3], [1, 2, 3, 4, 5]]
    
    for i in range(len(gas)):
        print(i+1, '.\tGas =', gas[i])
        print('\tCost =', cost[i])
        print('\n \tThe index of the gas station we can start our journey from is ', canCompleteCircuit(
            gas[i], cost[i]), '... (If it\'s -1 => that \n \tmeans no solution exists)')
        print('-' * 100)


if __name__ == '__main__':
    main()


'''
TC -> O(n), since there are n elements in the array and we only visit each element once. 
SC -> O(1), since we don't use any additional data structures.
'''