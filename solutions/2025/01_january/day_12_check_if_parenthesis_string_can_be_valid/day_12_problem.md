# Day 12 - [Check if a Parentheses String Can Be Valid](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/?envType=daily-question&envId=2025-01-12)
Date: 2025-01-12

Difficulty: Medium, ***but it should be a hard lol***

## Problem Description
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

- It is ().
- It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
- It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

- If locked[i] is '1', you cannot change s[i].

- But if locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. Otherwise, return false.

Example 1:

    Input: s = "))()))", locked = "010100"
    Output: true
    Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
    We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

Example 2:

    Input: s = "()()", locked = "0000"
    Output: true
    Explanation: We do not need to make any changes because s is already valid.

Example 3:

    Input: s = ")", locked = "0"
    Output: false
    Explanation: locked permits us to change s[0]. 
    Changing s[0] to either '(' or ')' will not make s valid.
 

### Constraints:

`n == s.length == locked.length`

`1 <= n <= 105`

`s[i] is either '(' or ')'.`

`locked[i] is either '0' or '1'.`

## Initial Approach Analysis

The initial approach focuses on counting and balancing parentheses through direct manipulation of counts. Here's a detailed breakdown:

### Core Strategy
The approach attempts to solve the problem by maintaining counts of left and right parentheses and determining if transformations are possible based on these counts:

```
1. Check if length is even (base case)
2. Calculate target number (n/2)
3. Count current parentheses
4. Calculate required transformations
5. Verify if transformations are possible with unlocked positions
```

### Limitations
While this approach seems intuitive, it has several significant limitations:

1. **Position Sensitivity**: It doesn't account for the position of parentheses. A string could have the correct total counts but still be invalid due to ordering.
2. **Local Validity**: It fails to verify if the string is valid at each intermediate position.
3. **Transformation Complexity**: The approach of calculating num_to_reduce_to and num_to_increase_to might overcomplicate the solution.

## Enhanced Approach Analysis

The enhanced approach uses a range-based validation strategy that provides more robust validation:

### Core Strategy
Instead of counting totals, this approach maintains a valid range of possible open parentheses at each position:

```python
1. Initialize range tracking (min_open, max_open)
2. For each position:
   - Locked '(': Increase both min and max
   - Locked ')': Decrease both min and max
   - Unlocked: Expand range (decrease min, increase max)
3. Validate ranges never invalidate string
4. Ensure final state can be balanced
```

### Key Advantages

1. **Position-Aware**: Validates the string at every position, ensuring no invalid intermediate states.
2. **Range Tracking**: By maintaining a range of possible values, it accurately represents all possible transformations.
3. **Early Detection**: Can detect invalid cases early, improving efficiency.
4. **Simpler State Management**: Eliminates need for complex transformation calculations.

### Implementation Details

The enhanced approach manages state through two key variables:
- `min_open`: Minimum possible number of open parentheses
- `max_open`: Maximum possible number of open parentheses

For each character:
1. Locked positions force specific changes to both min and max
2. Unlocked positions expand the range of possibilities
3. Negative max_open indicates an invalid state
4. Final state must include 0 in its range

## Complexity Analysis

### Time Complexity
Both approaches are O(n) where n is the string length, but the enhanced approach:
- Makes fewer passes through the string
- Has simpler operations at each position
- Can exit early on invalid cases

### Space Complexity
Both approaches use O(1) extra space, but the enhanced approach:
- Requires fewer variables
- Has more straightforward state management
- Eliminates need for transformation tracking

## Conclusion

The enhanced approach provides several significant improvements:
1. More accurate validation
2. Better handling of position-dependent cases
3. Simpler implementation
4. More efficient state management
5. Clearer reasoning about correctness

The key insight of tracking ranges rather than absolute counts makes the solution both more elegant and more robust, while also simplifying the implementation.