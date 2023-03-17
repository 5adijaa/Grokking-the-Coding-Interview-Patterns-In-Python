'''
Leetcode: 76. Minimum Window Substring
https://www.educative.io/courses/grokking-coding-interview-patterns-python/3Y0OpBLPYnr

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string ''.

The testcases will be generated such that the answer is unique.

Input: s = 'ADOBECODEBANC', t = 'ABC'
Output: 'BANC'
Explanation: The minimum window substring 'BANC' includes 'A', 'B', and 'C' from string t.

Input: s = 'a', t = 'aa'
Output: ''
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

def minWindow(s: str, t: str) -> str:
    count_freq, window = {}, {}
    curr_sub = [-1, -1]
    curr_length = float('infinity')
    
    for c in t:
        count_freq[c] = 1 + count_freq.get(c, 0)

    required = len(count_freq)
    formed = 0 
    
    l = 0
    r = 0
    while r < len(s):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in t and window[c] == count_freq[c]:
            formed += 1
        
        # increment the left pointer when window has all elts from t
        while required == formed and l<=r:
            # maintain the smallest sub
            if (r - l + 1) < curr_length:
                curr_sub = [l, r]
                curr_length = r - l + 1
            
            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in t and window[s[l]] < count_freq[s[l]]:
                formed -= 1
            l += 1
        
        r += 1
    l, r = curr_sub
    return s[l : r + 1]

def main():
    s = [ 'ADOBECODEBANC', 'PATTERN', 'LIFE', 'ABRACADABRA', 'STRIKER', 'DFFDFDFVD', 'a']
    t = ['ABC', 'TN', 'I', 'ABC', 'RK', 'VDD', 'aa']
    
    for i in range(len(s)):
        print(i + 1, '.\ts: ', s[i], '\n\tt: ', t[i], 
            '\n\tThe minimum substring containing ', 
            t[i], ' is: ', '"', minWindow(s[i], t[i]), '"', sep='')
        print('-' * 55)


if __name__ == '__main__':
    main()

'''
TC -> The time complexity for the solution shown above is O(n+m), where n and m are the lengths of the arrays s and t, respectively.
SC -> The space complexity is O(n+m) since we create two additional hash maps to store the frequency of the characters encountered.
'''