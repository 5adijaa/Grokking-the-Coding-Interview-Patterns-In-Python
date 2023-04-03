'''
Leetcode: 502. IPO
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/3jmBWVEznrR

You need to develop a program for making automatic investment decisions for a busy investor. The investor has some start-up capital, c, to invest and a portfolio of projects in which they would like to invest in. The investor wants to maximize their cumulative capital as a result of this investment.

To help them with their decision, they have information on the capital requirement for each project and the profit it's expected to yield. For example, if project A has a capital requirement of 3, and the investor's current capital is 1, then the investor can't invest in this project. On the other hand, if the capital requirement of a project B is 1, then the investor can invest in this project. Now, supposing that the project yields a profit of 2, the investor's capital at the end of the project will be 1+2=3. The investor can now choose to invest in project A as well since their current capital has increased.

As a basic risk-mitigation measure, the investor would like to set a limit on the number of projects, k, they invest in. For example, if the value of k is 2, then we need to identify the two projects that the investor can afford to invest in, given their capital requirements, and that yield the maximum profits.

Further, these are one-time investment opportunities, that is, the investor can only invest once in a given project.
'''

from typing import List
from heapq import heapify, heappop, heappush

def findMaximizedCapital(k: int, c: int, profits: List[int], capital: List[int]) -> int:
    min_capital = [(c, p) for c, p in zip(capital, profits)]
    heapify(min_capital) #min-heap
    
    max_profit = [] #only max profits that we can afford #max-heap

    curr_capital = c

    for i in range(k): #number of projects that can be done
        while min_capital and min_capital[0][0] <= curr_capital:
            c, p = heappop(min_capital) #we gonna get the capital and the profit
            
            heappush(max_profit, -p) #we add - to reverse default min heap in python to max heap
        
        if not max_profit: #empty heap
            break
        
        # 1. Every single time, we want to pop from the max_profit heap, 
        # So, take the removed item and add it to the curr capital
        curr_capital += -1*heappop(max_profit)
    
    return curr_capital


# print(findMaximizedCapital(2,1,[2,4,6,8], [1,2,2,3]))

def main():
    inputs =(
        (2, 0, [1 ,2, 3], [0, 1, 1]),
        (3, 0, [1 ,2, 3], [0, 1, 2]),
        (1, 0, [1 ,2, 3], [1, 1, 2]),
        (2, 1, [2, 4, 6, 8], [1, 2, 2, 3]),
        (3, 2, [1, 2, 3, 4, 5], [1, 3, 4, 5, 6]),
        (3, 1, [1, 3, 5, 7], [1, 2, 3, 4]),
        (2, 7, [4, 8, 12, 14], [6, 7, 8, 10]),
        (4, 2, [1, 2, 5, 6, 8, 9], [2, 3, 5, 6, 8, 12])
    )
    num = 1
    for i in inputs:
        print(f'{num}.\tProject Capital Requirements:  capital={i[2]}')
        print(f'\tProject Expected Profits:      profits={i[3]}')
        print(f'\tNumber of Projects:            k={i[0]}')
        print(f'\tStart-up Capital:              c={i[1]}')
        print('\n\tMaximum Capital Earned: ',
              findMaximizedCapital(i[0], i[1], i[2], i[3]))
        print('-' * 100, '\n')
        num += 1

main()

'''
TC -> The time complexity to push the required capital values on to the min-heap is O(nlogn), where n represents the number of projects. The time complexity to select the projects with the maximum profits from the heaps is O(klogn), where k represents the number of selected projects. However, in the worst case, k=n, hence, the time complexity of selecting the projects with the maximum profits from the heap will become O(nlogn). So, the total time complexity of the solution becomes O(nlogn+nlogn), that is, O(n logn)
SC -> We are using two heaps, one to store capital requirements and one to store profits. In the worst case, where we meet the capital requirements of all the projects right from the start, we populate both heaps with n elements each. Hence, the space complexity of this solution is O(n).
'''