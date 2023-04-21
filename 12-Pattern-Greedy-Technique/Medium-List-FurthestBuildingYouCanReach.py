'''
Leetcode: 1642. Furthest Building You Can Reach

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Example 1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
'''
import heapq
from typing import List


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    min_heap = [] #Store each diff(climb) between two contiguous buildings

    for i in range(len(heights)-1):
        climb = heights[i+1] - heights[i]

        if climb <= 0:
            continue
        
        if climb > 0: #we need to use a ladder or some bricks, always take a ladder first
            heapq.heappush(min_heap, climb)

            if ladders: #we only subtract one ladder regardless the diff climbs
                ladders -= 1
                continue
            
            bricks -= heapq.heappop(min_heap) #Find the curr shortest climb to use bricks
            
            if bricks < 0: #all bricks and all ladders are used
                return i
    
    return len(heights) - 1

def main():
    input = [
        (5, 1, [4, 2, 7, 6, 9, 14, 12]),
        (10, 2, [4, 12, 2, 7, 3, 18, 20, 3, 19]),
        (17, 0, [14, 3, 19, 3]),
        (9, 1, [9, 12, 11, 7, 13, 16, 21, 18, 47, 6]),
        (18, 3, [2, 5, 3, 1, 6, 3, 12, 6, 9, 10]),
    ]
    num = 1
    for i in input:
        print(num, '.\theights =', i[2])
        print('\tBricks =', i[0], '\n\tLadders =', i[1])
        print('\n\tFurthest Building I Can Reach is:', furthestBuilding(i[2], i[0], i[1]))
        num += 1
        print('-' * 85, '\n')

main()

'''
TC -> O(nlogk), where n is the length of the heights, and k is length of the heap. The for loop iterates through all n-1 pairs of adjacent buildings and performs a heap push and a heap pop for each positive difference between heights. Since the heap can have at most k elements, both push and pop operations take O(logk) time. So the total time complexity of this function is O(nlogk).
SC -> O(k), the space used by the heap
'''