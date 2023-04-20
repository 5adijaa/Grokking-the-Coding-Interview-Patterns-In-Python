'''
Leetcode: 871. Minimum Number of Refueling Stops
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/qVRq9mQnqV7

A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.


Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.

'''
from heapq import heappush, heappop
from typing import List


def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
    # target = 100 miles .. startFuel = 10
    # stations = [[10,60], [20,30], [30,30], [60,40]] ,, [[position, fuel]]
    # start(10)-------(10+60)-----------------------(70+40)--->Target=100
    #                    +1                           +2
   
    if startFuel >= target:
        return 0
    
    max_heap = []
    max_distance = startFuel #Max miles that we can reach, starting with startFuel
    min_refuel = 0

    i = 0
    while max_distance < target: #Loop until car reach the target or it's out of fuel
        if i < len(stations) and max_distance >= stations[i][0]: #There are still stations
            '''
            Sice, I am already ahead of or at this station (i.e. 
            max_distance >= stations[i][0]) we don't use this station and try to move ahead but I store this station in maxheap to use in future
            '''
            heappush(max_heap, -stations[i][1]) #So, add its fuel capacity to the heap
            i += 1
        
        elif not max_heap: #If there are no more stations and we can't reach the target
            return -1
        
        else: #Otherwise, fill up at the station with the highest fuel capacity
            max_distance += -heappop(max_heap)
            min_refuel += 1 #And increment stops
    
    return min_refuel


def main():
    input = [
        (1, 1, []),
        (100, 1, [[10, 100]]),
        (59, 14, [[9, 12], [11, 7], [13, 16], [21, 18], [47, 6]]),
        (15, 3, [[2, 5], [3, 1], [6, 3], [12, 6]]),
        (570, 140, [[140, 200], [160, 130], [310, 200], [330, 250]]),
        (1360, 380, [[310, 160], [380, 620], [700, 89], [850, 190],[990, 360]])
    ]
    num = 1
    for i in input:
        print(num, '.\tStations =', i[2])
        print('\tTarget =', i[0])
        print('\tStarting fuel =', i[1])
        print('\n\tMinimum number of refueling stops is:', minRefuelStops(i[0], i[1], i[2]))
        num += 1
        print('-' * 85, '\n')


if __name__ == '__main__':
    main()

'''
TC -> O(nlogn), where n is the number of stations. The while loop runs until the car reaches the target or runs out of fuel, which takes O(target/startFuel) iterations in the worst case. The inner while loop runs until all the stations that can be reached from the current fuel level are added to the heap, which takes O(n) iterations in the worst case. The heappush and heappop operations take O(logn) time each, and they are performed for each station, so the total time complexity of the heap operations is O(nlogn). Therefore, the overall time complexity of the function is O(nlogn)
SC -> O(n), since there will be maximum n fuel capacities in the heap.
'''