# Created by Ashish Patel at 2025/01/07 15:32
# leetgo: 1.4.11
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

"""
1700. Number of Students Unable to Eat Lunch (Easy)
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers
`0` and `1` respectively. All students stand in a queue. Each student either prefers square or
circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are
placed in a **stack**. At each step:

- If the student at the front of the queue **prefers** the sandwich on the top of the stack, they
will **take it** and leave the queue.
- Otherwise, they will **leave it** and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to
eat.

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of
the `iᵗʰ` sandwich in the stack ( `i = 0` is the top of the stack) and `students[j]` is the
preference of the `jᵗʰ` student in the initial queue ( `j = 0` is the front of the queue). Return
the number of students that are unable to eat.

**Example 1:**

```
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students =
[1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students =
[0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches =
[1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches =
[0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches =
[1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
```

**Example 2:**

```
Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
```

**Constraints:**

- `1 <= students.length, sandwiches.length <= 100`
- `students.length == sandwiches.length`
- `sandwiches[i]` is `0` or `1`.
- `students[i]` is `0` or `1`.

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
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = 0
        while(len(students) != 0):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                result = 0
            else:
                student = students.pop(0)
                result += 1
                students.append(student)
            if result == len(students):
                return result
        return result

# @lc code=end

if __name__ == "__main__":
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]
    ans = Solution().countStudents(students, sandwiches)
    print("\noutput:", serialize(ans, "integer"))
