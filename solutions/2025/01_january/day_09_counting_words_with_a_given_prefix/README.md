# Day 09 - [2185. Counting Words With a Given Prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix/submissions/?envType=daily-question&envId=2025-01-09)
Date: 2025-01-09

Difficulty: Easy

## Problem Description
You are given an array of `strings` words and a string `pref`.

Return the ***number of strings in words that contain pref as a prefix.***

A **prefix** of a string `s` is any leading contiguous substring of `s`.

## Examples

### Example 1
**Input:**  words = ["pay","<u>at</u>tention","practice","<u>at</u>tend"], `pref` = "at"

**Output:** 2

**Explanation:** The 2 strings that contain "at" as a prefix are: "attention" and "attend".

## Approach
1. Iterate through each word in the array
2. Use Python's built-in startswith() method to check prefix
3. Increment counter for matches
4. Return final count

## Complexity Analysis
- Time Complexity: O(n * m)
    - n = number of words
    - m = length of prefix
- Space Complexity: O(1)
    - Only using a single counter variable

## Learning Points
1. startswith() is more efficient than string slicing
2. No need to implement prefix checking manually
3. Early return optimizations aren't necessary due to needing full count
