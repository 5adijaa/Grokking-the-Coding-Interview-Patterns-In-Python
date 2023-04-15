'''
Leetcode: 528. Random Pick with Weight
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/YQBmrGYVXZO

You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

Example 1:
Input: ['Solution','pickIndex'] .. [[[1]],[]]
Output: [null,0]
Explanation:
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.

Example 2:
Input: ['Solution','pickIndex','pickIndex','pickIndex','pickIndex','pickIndex']
[[[1,3]],[],[],[],[],[]]
Output: [null,1,1,1,1,0]

Explanation:
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on
'''
import random
from typing import List


class RandomPickWithWeight:
    def __init__(self, w: List[int]):
        self.cumul_sum = 0
        self.prefix_sum = []
        for weight in w:
            self.cumul_sum += weight
            self.prefix_sum.append(self.cumul_sum)

    def pickIndex(self) -> int:
        target = random.randrange(0, self.cumul_sum)

        left, right = 0, len(self.prefix_sum)
        while left < right:
            mid = left + (right - left) // 2
            
            if self.prefix_sum[mid] <= target: # <= For finding upper bound
                left = mid + 1
            else:
                right = mid
        
        return left   


def main():
    counter = 900
    weights1 = [1, 2, 3, 4, 5]
    weights2 = [1, 12, 23, 34, 45, 56, 67, 78, 89, 90]
    weights3 = [10, 20, 30, 40, 50]
    weights4 = [1, 10, 23, 32, 41, 56, 62, 75, 87, 90]
    weights5 = [12, 20, 35, 42, 55]
    weights6 = [10, 10, 10, 10, 10]
    weights7 = [10, 10, 20, 20, 20, 30]
    weights8 = [1, 2, 3]
    weights9 = [10, 20, 30, 40]
    weights10 = [5, 10, 15, 20, 25, 30]
    weights = [weights1, weights2, weights3, weights4, weights5,
               weights6, weights7, weights8, weights9, weights10]
    dict = {}
    for i in range(len(weights)):
        print(i + 1, '.\tInput: ', weights[i], ', pickIndex() called ', counter, ' times', '\n', sep='')
        [dict.setdefault(l, 0) for l in range(len(weights[i]))]
        for _ in range(counter):
            sol = RandomPickWithWeight(weights[i])
            index = sol.pickIndex()
            dict[index] += 1
        print('-'*95)
        print('{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<15}{:<5}{:<15}'.format( \
            'Indexes', '|', 'Weights', '|', 'Occurences', '|', 'Frequency', '|', 'Expected Frequency'))
        print('-'*95)

        for key, value in dict.items():
            print('{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<15}{:<5}{:<15}'.format(key, '|', weights[i][key], '|', value, '|', \
                str(round((value/counter)*100, 2)) + '%', '|', str(round(weights[i][key]/sum(weights[i])*100, 2))+'%'))
        dict = {}
        print('\n', '-'*100, '\n', sep='')


if __name__ == '__main__':
    main()

'''
TC -> 
Constructor: Since the prefix_sum list gets calculated in the constructor, so the time complexity for the constructor is O(n), where n is the size of the weights array.
PickIndex: Since we're performing binary search on a list of length n, the time complexity is O(logn)
SC -> 
Constructor: The prefix_sum list takes O(n) space during its construction. 
PickIndex: This function takes O(1) space, since constant space is utilized.
'''