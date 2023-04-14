# Modified Binary Search Pattern:

## Overview:
The **modified binary search pattern** uses the binary search algorithm to search for a target value in an array.

Binary search is a searching algorithm that repeatedly divides an array in half, and searches for the target value in these subarrays. This process is achieved through the use of start, end, and middle pointers, which initially point to the k-th, last, and middle index of the array, respectively. The element at the middle index is compared with the target value. If it’s greater than the target value, the end pointer is moved one position to the left of the middle pointer to focus on the first half of the array. If it’s less than the target value, the start pointer is moved one position to the right of the middle pointer to focus on the second half of the array. This process is repeated until the element at the middle pointer points to the target value. However, if the entire array is traversed, that is, if the start and end pointer point to the same value, the target value is not present in the array.

Note: We’re assuming the array is sorted in ascending order. If it’s sorted in descending order, we’ll do the opposite when changing the positions of the start and end pointers.

Binary search reaches the target value in O(logn) time since we divide the array into two halves at each step. Had we opted for the brute-force approach, we would have to traverse the entire array, without any partitioning, to search for the target value, which would take O(n) in the worst case.

## Does my problem match this pattern?
- Yes, if either of these conditions is fulfilled:
    - The problem requires us to find a target value (or its first or last occurrence) in a sorted list, or in a sequential range.
    - We may use this pattern when portions of an input list are sorted, even if the whole list does not seem to be sorted. For example, an array has two different sorted sections.

- No, if either of these conditions is fulfilled:
    - The data to search is not sorted according to criteria relevant to the search.
    - We are not searching for a particular value in the data.

## Real-world problems:
Many problems in the real world use the modified binary search pattern. Let’s look at some examples.

- *Dictionary*: A dictionary contains words that are alphabetically sorted. Therefore, we can use binary search to get to the required word quickly.

- *Debugging with minimal support*: Let’s suppose that a code script consists of n lines, and that there is a bug somewhere in the script. Binary search is performed to find the bug by dividing the code based on the line numbers. For example, if the code doesn't run for the first n/2 lines, we further divide the code & check if it runs for the first n/4 lines and so on.

- *Student documents*: Sort the documents in order of the students’ roll numbers and apply binary search to search for a particular student’s document.

 