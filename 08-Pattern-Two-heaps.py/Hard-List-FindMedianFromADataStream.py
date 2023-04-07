'''
Leetcode: 295. Find Median from a Data Stream
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/q2pO5lqJ9rR

Implement a data structure that'll store a dynamically growing list of integers and provide access to their median in O(1)

Example:
Input: 
['MedianFinder', 'addNum', 'addNum', 'findMedian', 'addNum', 'findMedian']
[[], [1], [2], [], [3], []]
Output: 
[null, null, null, 1.5, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Follow up: (=> Using Two heaps pattern)
- If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
- If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

Answer' Process:
- The best time complexity we can get for this problem is O(logn) of addNum() and O(1) of findMedian(). This data structure seems highly likely to be a tree => So, we can use heap to solve this problem: We can use two heaps to store the lower half and the higher half of the data stream. The size of the two heaps shoudl be approximatively equals or differs at most 1.
- step1: each Num is added to one of the heaps: I'm gonna choose to add Num to min-heap first.
- step2: Then the minimum num is popped out from min-heap and pushed to the max-heap. This ensures all elements in min-heap are greater than max-heap 
- step3: check lenghth to make sure the two heaps are balanced

    small (max-heap) n/2           large (min-heap) n/2+1
            [-1]                            [2,3]


'''
from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.small = [] #max-heap for left small nums (n/2 items)
        self.large = [] #min-heap for right large nums (n/2 + 1 items)

    def addNum(self, num: int) -> None: #TC: O(logn) .. SC: O(n)
        heappush(self.large, num) #push Num to 'large'
        heappush(self.small, -heappop(self.large)) #pop from large and push it to small 

        if len(self.large) < len(self.small):
            heappush(self.large, -heappop(self.small))
        
        print('\t- max-heap for left small nums', self.small)
        print('\t- min-heap for right large nums', self.large)
        
    def findMedian(self) -> float: #TC: O(1) .. SC: O(1)
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0


def main():
    median_finder = MedianFinder()
    nums = [35, 22, 30, 25, 1]
    numlist = []
    x = 1
    for i in nums:
        numlist.append(i)
        print(x, '.\tData stream: ', numlist, sep='')
        median_finder.addNum(i)
        print('\tThe median for the given numbers is: ' +
              str(median_finder.findMedian()), sep='')
        print(100*'-'+'\n')
        x += 1


if __name__ == '__main__':
    main()
