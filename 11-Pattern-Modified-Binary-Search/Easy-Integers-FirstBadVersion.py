'''
Leetcode: 278. First Bad Version
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/my18VDQ9AwA

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Constraints: 1 <= bad <= n <= 231 - 1

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Input: n = 1, bad = 1
Output: 1
'''
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

def firstBadVersion(n: int) -> int:
    l = 1
    r = n
    res = -1
    calls = 0

    if n == 1:
        return n if isBadVersion(n) else -1

    while l < r:
        mid = (l + r)//2
        if isBadVersion(mid):
            res = mid #Record mid as current answer
            r = mid #Try to find a smaller version in the left side, if exist
        else:
            l = mid + 1 #Try to find in the right side
        calls += 1
    return res, calls


'''
TC -> O(logn) because we keep dividing the searching space in half at each iteration, where n is the size of the array.
SC -> O(1)
'''