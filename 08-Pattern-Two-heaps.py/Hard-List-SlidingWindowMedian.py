'''
Leetcode: 480. Sliding Window Median
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/gkEEkwY5m79

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10^-5 of the actual value will be accepted.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
'''
import heapq
from heapq import heapify, heappush, heappop
from typing import List

def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    output = []
    small = [] ## max-heap
    large = [] ## min-heap

    def getMedian(k):
        if k % 2 == 0:
            return (-small[0] + large[0]) / 2.0
        else:
            return large[0]

    def balanceHeaps():
        if len(large) < len(small):
            heappush(large, -heappop(small))
    
    def removeFromHeap(heap, val):
        # deleted[val] = deleted.get(val, 0) + 1
        index = heap.index(val)
        heap[index] = heap[-1] #replace the value we want to remove with the last value
        heap.pop()
        # heapify(heap) #re-heapify the heap -> takes O(k)
        if index < len(heap): #will take log(k)
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

    for i in range(len(nums)):
        if i >= k: #Remove prev item from the window:
            if large and nums[i - k] >= large[0]:
                removeFromHeap(large, nums[i - k])
            else:
                removeFromHeap(small, -nums[i - k])

        heappush(large, nums[i]) #Add value to min-heap first
        heappush(small, -heappop(large)) #Shift min value from min-heap to max-heap
        balanceHeaps()

        if i >= k-1: #Get Median of curr window
            output.append(getMedian(k))
    
    return output

def main():
    input = (
        ([1,3,-1,-3,5,3,6,7], 3),
        ([1,4,2,3], 4),
        ([3,1,2,-1,0,5,8],4), 
        ([1, 2], 1), 
        ([4, 7, 2, 21], 2), 
        ([22, 23, 24, 56, 76, 43, 121, 1, 2, 0, 0, 2, 3, 5], 5), 
        ([1, 1, 1, 1, 1], 2)
    )
    x = 1
    for i in input:
        print(x, '.\tInput array: ', i[0],  ', k = ', i[1], sep = '')
        print('\tMedians: ', medianSlidingWindow(i[0], i[1]), sep = '')
        print(100*'-', '\n', sep = '')
        x += 1


if __name__ == '__main__':
    main()

