'''
leetcode: 57. Insert Interval
https://www.educative.io/courses/grokking-coding-interview-patterns-python/m22YrXJwmWO

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary). Return intervals after the insertion.

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Explanation: Because the new interval [2,5] overlaps with [1,3]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

'''

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    output = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < newInterval[0]: #case1: intervals occur before newInterval
        output.append(intervals[i])
        i += 1
    
    while i < n and intervals[i][0] <= newInterval[1]: #case2: overlap -> merge all intervals
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    output.append(newInterval)

    while i < n and newInterval[1] < intervals[i][0]: #case3: add remaining intervals
        output.append(intervals[i])
        i += 1
    
    return output

def main():
    v1 = [[1,3],[6,9]]
    v2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    v3 = [[1,2],[3,4],[5,8],[9,15]]
    v4 = [[1,6],[8,9],[10,15],[16,18]]
    v6 = [[1,3],[4,6],[7,8],[9,10]]

    v_list = [v1, v2, v3, v4, v6]

    newIntervals = [[2,5], [4,8], [2,5], [9,10], [1,10]]

    for i in range(len(v_list)):
        print(i + 1, '. Intervals= ', v_list[i], ' and; newInterval= ', newIntervals[i], sep='')
        # result = merge(v_list[i])
        print(' Inserted interval:\t', insert(v_list[i], newIntervals[i]))
        print('-'*100)

if __name__ == '__main__':
    main()

'''
TC -> O(n)
SC -> O(n)
'''