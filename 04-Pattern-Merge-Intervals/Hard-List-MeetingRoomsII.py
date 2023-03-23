'''
leetcode: 919. Meeting Rooms II
https://www.educative.io/courses/grokking-coding-interview-patterns-python/qAQEWKkq73R

Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required.

Input: [(7,10),(2,4)]
Output: 1

Input: [(0, 30),(5, 10),(15, 20)]
Output: 2
Explanation: we need 2 meeting rooms -> room1: (0,30) .. room2: (5, 10),(15, 20)
(0,30) overlaps with (5,10) and (0,30) overlaps with (15,20) => 2 rooms needed


Process to solution -> using min-heap to keep track of needed rooms
[[0, 30],[5, 10],[15, 20], [18, 30]]
0   5     10    15    20     30
[-----------------------------]
    [------]    [------]
                      [-------]
loop over the remaing intervals, does the end time seen in the heap, is less than the curr start? -> if yes, no overlap and a meeting is ended which means a free room is available so pop the end time from heap. -> otherwise push the curr end time to the heap.
minheap[0] = 30
i=1 30<5? =>no .. add the end to the heap [10,30] .. min_rooms=2
i=2 10<15? =>yes .. pop it, heap becomes [30] .. then push end [20, 30] .. min_rooms=2
i=3 20<18? => no .. add it to the heap [18,20,30] min_rooms=3

'''

import heapq

def minMeetingRooms(intervals) -> int:
    intervals.sort(key=lambda x:x[0])

    min_rooms = 0
    minheap = [intervals[0][1]]
    for i in range(1, len(intervals)):
        if minheap[0] <= intervals[i][0]: #a meeting ended and a room is available
            heapq.heappop(minheap)
        heapq.heappush(minheap, intervals[i][1])
        min_rooms = max(min_rooms, len(minheap))
    
    return min_rooms


print(minMeetingRooms([[7, 10],[2, 4]])) #1
print(minMeetingRooms([[0, 30],[5, 10],[15, 20]])) #2
print(minMeetingRooms([[0, 30],[5, 10],[15, 20], [18, 30]])) #3
print(minMeetingRooms([[1, 2], [4, 6], [3, 4], [7, 8]])) #1
print(minMeetingRooms([[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]])) #3
print(minMeetingRooms([[1, 7], [2, 6], [3, 7], [4, 8], [5, 8]])) #5

'''
TC -> first we did sort: it takes O(nlogn), then we iterate over all the intervals, and every time we might need to push or pop to heap, so it takes O(nlogn) where n is the worst case where all n intervals overlap. So the total time complexity is O(nlogn)
SC -> O(n) we needed a list to store the number of rooms.
'''