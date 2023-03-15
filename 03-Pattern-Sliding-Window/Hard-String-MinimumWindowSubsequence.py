'''
Leetcode Premium: 727. Minimum Window Subsequence
https://www.educative.io/courses/grokking-coding-interview-patterns-python/3wNEnrZ2qRA

Given strings S and T, find the minimum (contiguous) substring W of S, so that every character in T (including duplicates) is included in the subsequence of W.

Input: S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.

Input: S="jmeqksfrsdcmsiwvaovztaqenprpvnbstl", T="u"
Output: ""
Explanation: unable to match
'''

def minWindow(S: str, T: str):
    len_S = len(S)
    len_T = len(T)
    ps, pt = 0, 0 # 1. We initialize 2 pointers where: 'ps' will point at start of S and 'pt' will point at start of T
    length = float('inf')
    min_subsequence = ''

    if len_S < len_T: return ''

    while ps < len_S:
        # 2. Process every character of S, to find a subSequence. We have 2 cases: if 'ps' and 'pt' both are eq => we increment both of them, else, we increment only 'ps'. At same time, we have to check if st is out of bound
        while ps < len_S and  pt < len_T:
            if S[ps] == T[pt]:
                ps += 1
                pt += 1
            else:
                ps += 1
        
        
        if pt == len_T:
            # 3. When 'pt' reaches the len(T). We have to make a reverse loop to get the subSequence from string S and get its length. for that we need 2 pointers 'start' and 'end' where start points at next char of subsequnce
            start = ps - 1
            end = ps
            pt = len_T - 1
            while pt >= 0:
                if S[start] == T[pt]:
                    pt -= 1
                    start -= 1
                else:
                    start -= 1
            
            # Now, we're out the 2nd loop with 'start' points at the start of subsequence, and 'end' at end+1 of our curr subsequence
            # The next step is to check if the length of this current subsequence between the pointers start and end is less than our existing minimum length =. if so update the length and subsequence to point at min_subsequence
            if end - start < length:
                length = end - start
                min_subsequence = S[start+1:end]
        
        ps += 1
    
    return min_subsequence


print(minWindow("abcdebdde" , "bde")) #expected: 'bcde'
print(minWindow('azjskfztf', 'sz')) #expected: 'skfz'
print(minWindow('abababa', 'ba')) #expected: 'ba'
print(minWindow("fgrqsqsnodwmxzkzxwqegkndaa" , "kzed")) #expected: 'kzxwqegknd'
print(minWindow("michmznaitnjdnjkdsnmichmznait" , "michmznait")) #'michmznait'
