# Created by Ashish Patel at 2025/01/15 23:56
# leetgo: 1.4.13
# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

"""
1725. Number Of Rectangles That Can Form The Largest Square (Easy)
You are given an array `rectangles` where `rectangles[i] = [lᵢ, wᵢ]` represents the `iᵗʰ` rectangle
of length `lᵢ` and width `wᵢ`.

You can cut the `iᵗʰ` rectangle to form a square with a side length of `k` if both `k <= lᵢ` and `k
<= wᵢ`. For example, if you have a rectangle `[4,6]`, you can cut it to get a square with a side
length of at most `4`.

Let `maxLen` be the side length of the **largest** square you can obtain from any of the given
rectangles.

Return the **number** of rectangles that can make a square with a side length of  `maxLen`.

**Example 1:**

```
Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
Output: 3
Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.
```

**Example 2:**

```
Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
Output: 3
```

**Constraints:**

- `1 <= rectangles.length <= 1000`
- `rectangles[i].length == 2`
- `1 <= lᵢ, wᵢ <= 10⁹`
- `lᵢ != wᵢ`

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
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        lengths = []
        for rectangle in rectangles:
            a, b = rectangle
            lengths.append(min(a,b))
        counts = Counter(lengths).most_common()
        counts.sort(key=lambda x: x[0],reverse=True)
        return counts[0][1]

# @lc code=end

if __name__ == "__main__":
    rectangles = [[5,8],[3,9],[5,12],[16,5]]
    ans = Solution().countGoodRectangles(rectangles)
    print("\noutput:", serialize(ans, "integer"))
