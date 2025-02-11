# Created by Ashish Patel at 2025/01/23 15:39
# leetgo: 1.4.11
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

"""
82. Remove Duplicates from Sorted List II (Medium)
Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only
distinct numbers from the original list. Return the linked list **sorted** as well.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg)

```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)

```
Input: head = [1,1,1,2,3]
Output: [2,3]
```

**Constraints:**

- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be **sorted** in ascending order.

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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                duplicate = curr.next
                duplicate_value = curr.next.val
                while duplicate and duplicate.val == duplicate_value:
                    duplicate = duplicate.next
                curr.next = duplicate
            else:
                curr = curr.next
        return dummy.next
# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().deleteDuplicates(head)
    print("\noutput:", serialize(ans, "ListNode"))
