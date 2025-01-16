# Day 16 - [2425. Bitwise XOR of All Pairings](https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=daily-question&envId=2025-01-16)
#### Date: 2025-01-16

##### Difficulty: Medium

## Problem Description
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.

 

**Example 1:**

**Input**: nums1 = [2,1,3], nums2 = [10,2,5,0]

**Output**: 13

**Explanation**:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.

**Example 2:**

**Input**: nums1 = [1,2], nums2 = [3,4]

**Output**: 0

**Explanation**:
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].

Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
 

**Constraints**:

- 1 <= nums1.length, nums2.length <= 105
- 0 <= nums1[i], nums2[j] <= 109

## Approach
### Intial Approach

- For each number in nums1, we need to XOR it with every number in nums2
- This creates a new array (nums3) with all these XOR results
- Finally, we need to XOR all numbers in nums3 together

This approach did not work because the memory limit exceed the compacity

### Optimal Approach
One of the best data structures to count the frequency of an element is a hash map. 
We iterate through the elements of nums1 and nums2 and add their total occurrences to the map. 
Once the frequencies are determined, we initialize a variable ans to store the XOR result. 
For each key in the map, we XOR it with ans if its total occurrence is odd. 
The final value of ans is returned as our required answer.


## Complexity Analysis
- Time Complexity: O(?)
- Space Complexity: O(?)

## Learning Points
[What you learned today]

## Similar Problems
[Related problems you can practice]