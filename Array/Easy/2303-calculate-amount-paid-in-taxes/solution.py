# Created by Ashish Patel at 2025/01/16 11:11
# leetgo: 1.4.13
# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

"""
2303. Calculate Amount Paid in Taxes (Easy)
You are given a **0-indexed** 2D integer array `brackets` where `brackets[i] = [upperᵢ, percentᵢ]`
means that the `iᵗʰ` tax bracket has an upper bound of `upperᵢ` and is taxed at a rate of
`percentᵢ`. The brackets are **sorted** by upper bound (i.e. `upperᵢ₋₁ < upperᵢ` for `0 < i <
brackets.length`).

Tax is calculated as follows:

- The first `upper₀` dollars earned are taxed at a rate of `percent₀`.
- The next `upper₁ - upper₀` dollars earned are taxed at a rate of `percent₁`.
- The next `upper₂ - upper₁` dollars earned are taxed at a rate of `percent₂`.
- And so on.

You are given an integer `income` representing the amount of money you earned. Return the amount of
money that you have to pay in taxes. Answers within `10⁻⁵` of the actual answer will be accepted.

**Example 1:**

```
Input: brackets = [[3,50],[7,10],[12,25]], income = 10
Output: 2.65000
Explanation:
Based on your income, you have 3 dollars in the 1ˢᵗ tax bracket, 4 dollars in the 2ⁿᵈ tax bracket,
and 3 dollars in the 3ʳᵈ tax bracket.
The tax rate for the three tax brackets is 50%, 10%, and 25%, respectively.
In total, you pay $3 * 50% + $4 * 10% + $3 * 25% = $2.65 in taxes.
```

**Example 2:**

```
Input: brackets = [[1,0],[4,25],[5,50]], income = 2
Output: 0.25000
Explanation:
Based on your income, you have 1 dollar in the 1ˢᵗ tax bracket and 1 dollar in the 2ⁿᵈ tax bracket.
The tax rate for the two tax brackets is 0% and 25%, respectively.
In total, you pay $1 * 0% + $1 * 25% = $0.25 in taxes.
```

**Example 3:**

```
Input: brackets = [[2,50]], income = 0
Output: 0.00000
Explanation:
You have no income to tax, so you have to pay a total of $0 in taxes.
```

**Constraints:**

- `1 <= brackets.length <= 100`
- `1 <= upperᵢ <= 1000`
- `0 <= percentᵢ <= 100`
- `0 <= income <= 1000`
- `upperᵢ` is sorted in ascending order.
- All the values of `upperᵢ` are **unique**.
- The upper bound of the last tax bracket is greater than or equal to `income`.

"""

from typing import *
from leetgo_py import *

import bisect
import collections 
import functools
import heapq 
import itertools 
import operator
import math 
import string

# @lc code=begin

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        prev = 0
        tax = 0
        for bracket in brackets:
            if income > prev:
                upper, rate = bracket
                taxableIncome = min(upper, income)
                tax +=(taxableIncome - prev)* (rate/100)
                prev = upper
            if income <= prev:
                break
        return tax

# @lc code=end

if __name__ == "__main__":
    brackets = [[3,50],[7,10],[12,25]]
    income = 10
    ans = Solution().calculateTax(brackets, income)
    print("\noutput:", serialize(ans, "double"))
