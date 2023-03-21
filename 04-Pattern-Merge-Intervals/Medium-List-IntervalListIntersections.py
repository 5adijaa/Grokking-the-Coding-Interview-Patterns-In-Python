'''
986. Interval List Intersections
https://www.educative.io/courses/grokking-coding-interview-patterns-python/gxGkwKK2mEj

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order. Return the intersection of these two interval lists.

* A closed interval [a, b] (with a<=b) denotes the set of real numbers x with a <= x <= b.
* The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
'''

from typing import List


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]):
    i, j = 0, 0
    output = []

    while i < len(firstList) and j < len(secondList):
        f_start, f_end = firstList[i]
        s_start, s_end = secondList[j]
        
        if f_start <= s_end and s_start <= f_end:
            intersect0 = max(f_start, s_start)
            intersect1 = min(f_end, s_end)
            output.append([intersect0, intersect1])
        
        if f_end < s_end:
            i += 1
        else:
            j += 1
    
    return output


def main():
    firstList = [
        [[1, 2]],
        [[1, 4], [5, 6], [9, 15]],
        [[3, 6], [8, 16], [17, 25]],
        [[4, 7], [9, 16], [17, 28], [39, 50], [55, 66]],
        [[1, 3], [5, 6], [7, 8], [12, 15]]
    ]

    secondList = [
        [[1, 2]],
        [[2, 4], [5, 7], [9, 15]],
        [[2, 3], [10, 15], [18, 23]],
        [[3, 6], [7, 8], [9, 10], [14, 19], [23, 33], [35, 40],[45, 59]],
        [[2, 4], [7, 10]]
    ]

    for i in range(len(firstList)):
        print(i + 1, '.\t Interval firstList: ', firstList[i], sep='')
        print('\t Interval secondList: ', secondList[i], sep='')
        print('\t Intersecting intervals are: ', intervalIntersection(firstList[i], secondList[i]), sep='')

        print('-' * 100)


if __name__ == '__main__':
    main()

'''
TC -> O(n+m) where n is length of firstList and m is length of secondList
TC -> O(1) as only a fixed amount of memory is consumed by a few temporary variables for computations performed by the algorithm
'''