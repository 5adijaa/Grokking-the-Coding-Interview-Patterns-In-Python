'''
Leetcode: 93. Restore IP Addresses
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/gxDVoNQZ1jY

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, '0.1.2.201' and '192.168.1.1' are valid IP addresses, but '0.011.255.245', '192.168.1.312' and '192.168@1.1' are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

Example 1:
Input: s = '25525511135'
Output: ['255.255.11.135','255.255.111.35']

Example 2:
Input: s = '0000'
Output: ['0.0.0.0']

Example 3:
Input: s = '101023'
Output: ['1.0.10.23','1.0.102.3','10.1.0.23','10.10.2.3','101.0.2.3']
'''
from typing import List


def restoreIpAddresses(s: str) -> List[str]:
    result = []

    if len(s) > 12: return result 

    def dfs(start, segments):
        if len(segments) == 4 and start == len(s): #We've found 4 segments & used all the chars of 's'
            result.append('.'.join(segments))
            return

        if len(segments) == 4: #We've found 4 segments but there are still unused chars in 's'
            return
        
        for i in range(start, min(start+3, len(s))): #Try adding one segment at a time
            segmnt = s[start:i+1]
            if int(segmnt) < 256 and (segmnt[0] != '0' or len(segmnt) == 1):
                segments.append(segmnt)
                dfs(i+1, segments)
                segments.pop()

    dfs(0, [])
    return result


def main():
    ip_addresses = ['25525511135', '0000', '101023', '12121212', '113242124', '199219239', '121212', '25525511335']

    for i in range(len(ip_addresses)):
        print(i + 1, '.\t Input addresses: '', ip_addresses[i], ''', sep='')
        print('\t Possible valid IP Addresses are: ',
              restoreIpAddresses(ip_addresses[i]), sep='')
        print('-' * 100)


if __name__ == '__main__':
    main()

'''
TC -> O(3^4) which simplifies to O(1): because the maximum length of each segment is 3 and we have 4 segments. Therefore, the maximum number of possibilities for each segment is 3 (0-255), and we have 4 segments. ie. The maximum number of combinations for 4 segments each of length <= 3 is 3^4 = 81 which is a constant value.
SC -> O(1) since the only extra space used is for storing the results in the 'segments' list, which can contain at most 9 IP addresses (since there are 12 digits and at least 3 dots separating them), which is a constant value.
'''