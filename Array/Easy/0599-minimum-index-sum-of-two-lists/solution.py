# Created by Ashish Patel at 2024/12/28 22:07
# leetgo: 1.4.13
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

"""
599. Minimum Index Sum of Two Lists (Easy)
Given two arrays of strings `list1` and `list2`, find the **common strings with the least index
sum**.

A **common string** is a string that appeared in both `list1` and `list2`.

A **common string with the least index sum** is a common string such that if it appeared at
`list1[i]` and `list2[j]` then `i + j` should be the minimum value among all the other **common
strings**.

Return all the **common strings with the least index sum**. Return the answer in **any order**.

**Example 1:**

```
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at
Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".
```

**Example 2:**

```
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger
King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
```

**Example 3:**

```
Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".
```

**Constraints:**

- `1 <= list1.length, list2.length <= 1000`
- `1 <= list1[i].length, list2[i].length <= 30`
- `list1[i]` and `list2[i]` consist of spaces `' '` and English letters.
- All the strings of `list1` are **unique**.
- All the strings of `list2` are **unique**.
- There is at least a common string between `list1` and `list2`.

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
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = math.inf
        min_words = []
        dict = { word : idx  for idx, word in enumerate(list1)}
        print(dict)
        for idx2, word2 in enumerate(list2):
            if word2 in dict:
                print("heeeee")
                if dict.get(word2) + idx2 < min_sum:
                    min_sum = dict.get(word2) + idx2
                    min_words = [word2]
                elif dict.get(word2) + idx2 == min_sum:
                    min_words.append(word2)
        return min_words
# @lc code=end

if __name__ == "__main__":
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    ans = Solution().findRestaurant(list1, list2)
    print("\noutput:", serialize(ans, "string[]"))
