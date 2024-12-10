# Created by Ashish Patel at 2024/11/19 13:20
# leetgo: 1.4.11
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

"""
3318. Find X-Sum of All K-Long Subarrays I (Easy)
You are given an array `nums` of `n` integers and two integers `k` and `x`.

The **x-sum** of an array is calculated by the following procedure:

- Count the occurrences of all elements in the array.
- Keep only the occurrences of the top `x` most frequent elements. If two elements have the same
number of occurrences, the element with the **bigger** value is considered more frequent.
- Calculate the sum of the resulting array.

**Note** that if an array has less than `x` distinct elements, its **x-sum** is the sum of the array.

Return an integer array `answer` of length `n - k + 1` where `answer[i]` is the **x-sum** of the
subarray `nums[i..i + k - 1]`.

**Example 1:**

**Input:** nums = \[1,1,2,2,3,4,2,3\], k = 6, x = 2

**Output:**\[6,10,12\]

**Explanation:**

- For subarray `[1, 1, 2, 2, 3, 4]`, only elements 1 and 2 will be kept in the resulting array.
Hence, `answer[0] = 1 + 1 + 2 + 2`.
- For subarray `[1, 2, 2, 3, 4, 2]`, only elements 2 and 4 will be kept in the resulting array.
Hence, `answer[1] = 2 + 2 + 2 + 4`. Note that 4 is kept in the array since it is bigger than 3 and 1
which occur the same number of times.
- For subarray `[2, 2, 3, 4, 2, 3]`, only elements 2 and 3 are kept in the resulting array. Hence,
`answer[2] = 2 + 2 + 2 + 3 + 3`.

**Example 2:**

**Input:** nums = \[3,8,7,8,7,5\], k = 2, x = 2

**Output:**\[11,15,15,15,12\]

**Explanation:**

Since `k == x`, `answer[i]` is equal to the sum of the subarray `nums[i..i + k - 1]`.

**Constraints:**

- `1 <= n == nums.length <= 50`
- `1 <= nums[i] <= 50`
- `1 <= x <= k <= nums.length`

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
import leetcode as lc

# @lc code=begin

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def findXFrequentItems(subArray, x):
            dict = {}
            for i in range(len(subArray)):
                dict[subArray[i]] = dict.get(subArray[i], 0) + 1
            heap = [[value, key] for key, value in dict.items()]
            xFrequent = heapq.nlargest(x, heap)
            return xFrequent
        
        result = []
        for i in range(len(nums) - k + 1):
            xFrequent = findXFrequentItems(nums[i:i+k], x)
            sum = 0
            for i in range(len(xFrequent)):
                sum += xFrequent[i][0] * xFrequent[i][1]
            result.append(sum)
        return result

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    # nums, k, x = [9,2,2], 3, 3
    ans = Solution().findXSum(nums, k, x)
    print("\noutput:", serialize(ans, "integer[]"))
