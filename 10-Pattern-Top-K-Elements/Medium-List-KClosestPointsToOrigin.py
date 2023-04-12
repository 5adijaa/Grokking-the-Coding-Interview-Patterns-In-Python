'''
Leetcode: 973. K Closest Points to Origin
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/gkj5Z8wQ859

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x^2 + y^2)).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
'''
from heapq import *
import math
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    def euclidean_distance(point: List[int]) -> float: #O(1)
        return math.sqrt(point[0]**2 + point[1]**2)
    
    max_heap = []
    for i in range(k): 
        distance = euclidean_distance(points[i])
        heappush(max_heap, (-distance, points[i]))
    
    for i in range(k, len(points)): 
        curr_distance = euclidean_distance(points[i])
        if abs(curr_distance) < abs(max_heap[0][0]):
            heappop(max_heap)
            heappush(max_heap, (-curr_distance, points[i]))            
    
    return [point for distance, point in max_heap]


def main():
    points_lists = [
        [[1,3],[-2,2]],
        [[3,3],[5,-1],[-2,4]],
        [[-1,-3],[-4,-5],[-2,-2],[-2,-3]],
        [[1,3],[2,4],[2,-1],[-2,2],[5,3],[3,-2]],
        [[1, 3], [5, 3], [3, -2], [-2, 2]]
    ]
    k_list = [1, 2, 3, 3, 1]

    for i in range(len(k_list)):
        res = kClosest(points_lists[i], k_list[i])
        print(i + 1, '.\t- List of points =', points_lists[i], ', k =', k_list[i])
        print('\tThere are the k =', k_list[i], 'points, closest to the', \
        'origin (0, 0): ', res)
        print('-'*100)


main()
 
'''
TC -> The algorithm's time complexity is O(nlogk), where n is the total number of points and k is the number of points closest to the origin. This is because we need to iterate over all the n points and perform operations on a heap of size k, which takes O(nlogk) time in the worst case.
SC -> The memory complexity will be O(k) because we need to store k points in the heap.
'''