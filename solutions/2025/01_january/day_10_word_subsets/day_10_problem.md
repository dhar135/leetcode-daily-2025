# Day 10 - [916. Word Subsets](https://leetcode.com/problems/word-subsets/description/?envType=daily-question&envId=2025-01-10)
Date: 2025-01-10

Difficulty: Medium

## Problem Description
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

<br>

**Example 1:**
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

Output: ["facebook","google","leetcode"]

**Example 2:**

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

Output: ["leetcode"]

**Example 3:**

Input: words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

Output: ["cccbb"]

 
**Constraints:**

- 1 <= words1.length, words2.length <= 104
- 1 <= words1[i].length, words2[i].length <= 10
- words1[i] and words2[i] consist only of lowercase English letters.
- All the strings of words1 are unique.


## Approach
The solution uses character frequency counting to efficiently determine universal strings. 

Here's the step-by-step approach:

1. Create a maximum frequency array (max_freq) to track the highest frequency needed for each character across all words in words2:

    - Initialize array of size 26 (a-z)
    - For each word in words2, count character frequencies
    - Update max_freq with maximum frequency for each character


2. Check each word in words1 against the requirements:

    - Count character frequencies in current word
    - Compare against max_freq
    - If word has sufficient frequency for all required characters, add to result

## Complexity Analysis


- Time Complexity: O(N*M + K), where:

    - N = length of words1
    - M = max length of any word in words1
    - K = total length of all words in words2


- Space Complexity: O(1)

    - Uses fixed-size arrays (26 elements) for character frequencies
    - Result array not counted as per convention

## Learning Points
- Efficient character frequency tracking using fixed-size arrays
- Combining multiple requirements into a single check
- Using ASCII values for array indexing
- Handling frequency requirements vs simple presence checks

## Similar Problems
[Related problems you can practice]