# Cyclic Sort Pattern

## Overview:
**Cyclic sort** is an in-place comparison sort algorithm. It is based on the idea that the array can be divided into cycles, and each element is rotated to create a sorted array. 
-> This pattern deals with problems involving arrays that contain numbers in a given range. Mostly, cyclic sort problems involve unique unsorted elements. 
-> This pattern is mostly used where we need to find the missing number or duplicate number in a given range.

To solve the cyclic sort problems, we place the elements at their respective index since the elements are given in a specific range.

## Example:
Let’s look at the following example to understand how a cyclic sort is used to sort an array: input = [3, 1, 2, 5, 4]
- We have an unsorted array. Let's sort it using cyclic sort. We'll keep elements at their correct index: Correct index = index_value - 1.
- We’ve found that 3 isn’t at its correctposition, so we can swap it with the element at index 2 => [2, 1, 3, 5, 4]
- We’ve placed 3 at its correct position, but we need to check if the swapped element 2 is now at its correct position. 
- We’ve found that 2 is not at its correct position, so we can swap it with the elementat index 1. => [1, 2, 3, 5, 4]
- We’ve placed 2 at its correct position, but we need to check if the swapped element 1 is now at its correct position.
- Since 1 is already at its correct position, so we can traverse the array until we find a number that isn't. => [1, 2, 3, 5, 4] => We’ve found that 5 is not at its correct position, so we can swap it with the elementat index 4.
- We’ve placed 5 at its correct position,but we need to check if the swapped element4 is now at its correct position => [1, 2, 3, 4, 5]
- 4 is also at its correct index. We now have a sorted array.

## Does my problem match this pattern?
- Yes, if either of these conditions is fulfilled:
    - The input array has a cycle, that is, there are duplicate numbers.
    - The problem asks us to find the missing number in the given range, that is, [1−n]

- No, if any of these conditions is fulfilled:
    - The problem is not based on integer numbers.
    - The input data is not originally in an array and also can’t be mapped to an array.
    - The given data is not in the [1−n] range, where n is the size of the array.

## Real-world problems:
Many problems in the real world share the cyclic sort pattern. Let’s look at some examples.

- Computational Biology: The species on a planet have n distinct genes numbered 1…n. Find the kth missing​​ gene in a given DNA sequence.

- Error checking: Network transmission errors cause a number in a known range to be misinterpreted as a different number from the same range. Find the number that is caused by the error, along with the number that is misinterpreted.