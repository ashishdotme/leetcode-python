# Created by Ashish Patel at 2025/01/15 00:06
# leetgo: 1.4.13
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

"""
1491. Average Salary Excluding the Minimum and Maximum Salary (Easy)
You are given an array of **unique** integers `salary` where `salary[i]` is the salary of the `iᵗʰ`
employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within
`10⁻⁵` of the actual answer will be accepted.

**Example 1:**

```
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
```

**Example 2:**

```
Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
```

**Constraints:**

- `3 <= salary.length <= 100`
- `1000 <= salary[i] <= 10⁶`
- All the integers of `salary` are **unique**.

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
    def average(self, salary: List[int]) -> float:
        min_salary, max_salary = min(salary), max(salary)
        total = 0
        for i in range(len(salary)):
            if salary[i] is not min_salary and salary[i] is not max_salary:
                total += salary[i]
        return total/(len(salary)-2)
# @lc code=end

if __name__ == "__main__":
    salary = [4000,3000,1000,2000]
    ans = Solution().average(salary)
    print("\noutput:", serialize(ans, "double"))
