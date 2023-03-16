'''
Leetcode: 187. Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'. For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Problem:
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
'''

from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    seen, repeated = set(), set()

    i=0
    while i < len(s)-9:
        window = s[i:i+10]
        if window in seen: #before adding the window to 'seen' check for repetition 
            repeated.add(window)
        seen.add(window)
        i+=1

    return list(repeated)


print(findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
print(findRepeatedDnaSequences('AAAAAAAAAAAAA'))

'''
TC -> O(n-9) because we iterate over we iterate over n-10+1 substrings of length 10, n is the length of the input string 's'
SC -> O(2(n-9)) becaue we uses 2 sets of n-10+1 length each.
'''